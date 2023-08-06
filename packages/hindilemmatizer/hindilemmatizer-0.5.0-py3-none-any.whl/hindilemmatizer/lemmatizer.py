import csv
import re
import pkg_resources

globalPrefixWordsSet = set()
globalRootWordsSet = set()
globalSuffixWordsSet = set()

data_path = pkg_resources.resource_filename('hindilemmatizer', 'data/data.csv')
with open(data_path, encoding='utf-8') as f:
  reader=csv.reader(f)
  for row in reader:
    globalPrefixWordsSet.add(row[1])
    globalRootWordsSet.add(row[2])
    globalSuffixWordsSet.add(row[3])

  f.close()


directRoots = dict()

direct_path = pkg_resources.resource_filename('hindilemmatizer', 'data/direct.csv')
with open(direct_path, encoding='utf-8') as f:
  reader=csv.reader(f)
  for row in reader:
    directRoots[row[0]] = row[1]

  f.close()


totalWords = set()

total_path = pkg_resources.resource_filename('hindilemmatizer', 'data/totalWords.txt')
with open(total_path, encoding='utf-8') as f:
  data = f.readlines()
  for i in range(len(data)):
    totalWords.add(data[i].strip())
  f.close()


globalPrefixWordsSet.discard("")
globalRootWordsSet.discard("")
globalSuffixWordsSet.discard("")

alreadyLemmatizedWords = dict()
# Here comes real algorithm
class WordLemmatizer:
  rootWords = []
  
  def __init__(self, word):
    self.word = word
    self.inflectedWord = list(word)
    self.possibleRootWords = set()
  
  def lemmatize(self):
    if (len(self.word)<3):
      '''
        done this because बुरा is giving बु which is not a root word, so length check is made
      '''
      return self.word

    return self.step1()
  
  def step1(self):

    for r in range(1,len(self.word)):
      tempWord = self.word[:r+1]
      if tempWord in globalRootWordsSet and len(tempWord)>1:
        self.possibleRootWords.add(tempWord)

    if(len(self.possibleRootWords)):
      return self.finalReturn()
    
    return self.step2()
  
  def step2(self):
    for l in range(2,len(self.word)):
      if self.word[l:] in globalSuffixWordsSet and len(self.word[l:])>1 and self.word[:l] in totalWords:
        self.possibleRootWords.add(WordLemmatizer(self.word[:l]).lemmatize())

    if(len(self.possibleRootWords)):
      return self.finalReturn()

    return self.word

  def step3(self):

    for r in range(1,len(self.inflectedWord)-1):
      if self.word[:r] in globalPrefixWordsSet and self.word[r:] in totalWords:
        self.possibleRootWords.add(WordLemmatizer(self.word[r:]).lemmatize())
    if(len(self.possibleRootWords)):
      return self.finalReturn()

    return self.word

  def finalReturn(self):
    # currently here returning longest one
    possibleRootWords = list(self.possibleRootWords)
    possibleRootWords.sort(key = lambda x: -len(x))

    if possibleRootWords and len(possibleRootWords[0])>2:
      return possibleRootWords[0]

    return self.word

def sanitizeLine(line):
  return re.sub(r'\s+', ' ', re.sub(r'[{}[\]:;?@!#$%^&*()-_\'\"<>\u0964\u0965,]', ' ', line.encode("utf-8").decode("utf-8"))).split()

def processWord(word):

  if word in directRoots:
    alreadyLemmatizedWords[word] = directRoots[word]

  if word in alreadyLemmatizedWords:
    return alreadyLemmatizedWords[word]

  lemma= WordLemmatizer(word).lemmatize()
  alreadyLemmatizedWords[word]=lemma
  return lemma

def lemmatize(line):
  # this is the function that will be called by the user to lemmatize hindi text, it can accept both word and a line
  words = sanitizeLine(line)

  return " ".join([processWord(word) for word in words if word])