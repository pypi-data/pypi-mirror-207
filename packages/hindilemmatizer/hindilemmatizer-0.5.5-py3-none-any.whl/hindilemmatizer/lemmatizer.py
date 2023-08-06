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

suffixes = {
  1: ["ो","े","ू","ु","ी","ि","ा"],
  2: ["कर","ाओ","िए","ाई","ाए","ने","नी","ना","ते","ीं","ती","ता","ाँ","ां","ों","ें"],
  3: ["ाकर","ाइए","ाईं","ाया","ेगी","ेगा","ोगी","ोगे","ाने","ाना","ाते","ाती","ाता","तीं","ाओं","ाएं","ुओं","ुएं","ुआं"],
  4: ["ाएगी","ाएगा","ाओगी","ाओगे","एंगी","ेंगी","एंगे","ेंगे","ूंगी","ूंगा","ातीं","नाओं","नाएं","ताओं","ताएं","ियाँ","ियों","ियां"],
  5: ["ाएंगी","ाएंगे","ाऊंगी","ाऊंगा","ाइयाँ","ाइयों","ाइयां"],
}


rule1 = suffixes[4][17]
rule2 = suffixes[4][16]
rule3 = suffixes[1][1]
rule4 = suffixes[1][6]
rule5 = suffixes[1][4]
rule6 = suffixes[5][4]
rule7 = suffixes[5][5]
rule8 = suffixes[5][6]

# Here comes real algorithm
class WordLemmatizer:
  
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

    flag = 0
    for l in range(2,len(self.word)):
      if self.word[l:] in globalSuffixWordsSet and len(self.word[l:])>1 and (self.word[:l] in directRoots):
        self.possibleRootWords.add(WordLemmatizer(directRoots[self.word[:l]]).lemmatize()) 
        flag=1   

    if flag:
      pass
    elif self.word.endswith(rule1):
      self.possibleRootWords.add(WordLemmatizer(self.word[:self.word.rindex(rule1)] + suffixes[1][4]).lemmatize())
    
    elif self.word.endswith(rule2):
      self.possibleRootWords.add(WordLemmatizer(self.word[:self.word.rindex(rule2)] + suffixes[1][4]).lemmatize())

    elif self.word.endswith(rule3):
      self.possibleRootWords.add(WordLemmatizer(self.word[:self.word.rindex(rule3)] + suffixes[1][6]).lemmatize())
    
    elif self.word.endswith(rule4):
      self.possibleRootWords.add(WordLemmatizer(self.word[:self.word.rindex(rule4)] + suffixes[1][6]).lemmatize())
    
    elif self.word.endswith(rule5):
      self.possibleRootWords.add(WordLemmatizer(self.word[:self.word.rindex(rule5)] + suffixes[1][4]).lemmatize())
    
    elif self.word.endswith(rule6):
      self.possibleRootWords.add(WordLemmatizer(self.word[:self.word.rindex(rule6)] + suffixes[3][2]).lemmatize())
    
    elif self.word.endswith(rule7):
      self.possibleRootWords.add(WordLemmatizer(self.word[:self.word.rindex(rule7)] + suffixes[3][2]).lemmatize())
    
    elif self.word.endswith(rule8):
      self.possibleRootWords.add(WordLemmatizer(self.word[:self.word.rindex(rule8)] + suffixes[3][2]).lemmatize())
    else:
      for l in range(2,len(self.word)):
        if self.word[l:] in globalSuffixWordsSet and len(self.word[l:])>1 and (self.word[:l] in totalWords or self.word[:l] in globalRootWordsSet):
          self.possibleRootWords.add(WordLemmatizer(self.word[:l]).lemmatize())    

    if(len(self.possibleRootWords)):
      return self.finalReturn()

    return self.word

  def step3(self):

    for r in range(1,len(self.inflectedWord)-1):
      if self.word[:r] in globalPrefixWordsSet and (self.word[r:] in totalWords or self.word[r:] in globalRootWordsSet):
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
  return re.sub(r'\s+', ' ', re.sub(r'[{}[\]:;_<>?@!#$%^&*()\u0964\u0965,\']', ' ', line.encode("utf-8").decode("utf-8"))).split()

def processWord(word):

  if word in directRoots:
    alreadyLemmatizedWords[word] = directRoots[word]

  if word in alreadyLemmatizedWords:
    return alreadyLemmatizedWords[word]

  lemma= WordLemmatizer(word).lemmatize()
  alreadyLemmatizedWords[word]=lemma
  return lemma

def is_hindi_word(word):
  hindi_pattern = re.compile(r'^[\u0900-\u097F]+$')
  return bool(hindi_pattern.match(word))

def lemmatize(line):
  # this is the function that will be called by the user to lemmatize hindi text, it can accept both word and a line
  words = sanitizeLine(line)
  result = []
  for word in words:
    if is_hindi_word(word):
      result.append(processWord(word))
    else:
      result.append(word)

  return " ".join(result)