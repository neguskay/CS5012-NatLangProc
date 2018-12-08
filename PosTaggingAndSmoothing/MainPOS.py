"""
    CS5012
    PRACTICAL 1
    UNIVERSITY OF ST ANDREWS
    STUDENT ID: 170027939
    
    POS TAGGER
"""

import HMM

import nltk
import nltk.util
import nltk.book
import nltk.corpus
import nltk.tag
import collections

from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from nltk.book import FreqDist

from nltk.corpus import brown, conll2000, alpino, floresta, gutenberg

from nltk.tag import hmm
from nltk.util import unique_list
from nltk.probability import *
from nltk import ConditionalProbDist
from nltk import ConditionalFreqDist
from collections import Counter

from HMM import *

# Load the Training and Test Sentences
print("Downloading Training Sentences from Corpus")
trainingSentences_brown = brown.tagged_sents(tagset = "universal")[:10000]
trainingSentences_conll2000 = conll2000.tagged_sents()[:10000]
trainingSentences_alpino = alpino.tagged_sents()[:10000]
trainingSentences_floresta = floresta.tagged_sents()[:10000]
print "Done!"

print("Downloading Test Sentences from Corpus")
testSentences_brown = brown.tagged_sents(tagset = "universal")[10000:10500]
testSentences_conll2000 = conll2000.tagged_sents()[10000:10500]
testSentences_alpino = alpino.tagged_sents()[10000:10500]
testSentences_floresta = floresta.tagged_sents()[10000:10500]
print "Done!"

# Extracts words and tags from Sentences
def extractWords_and_Tags(sentences):
  words = {}
  tags = {}
  for sentence in sentences:
    for word, tag in sentence:
      words[word] = 0
      tags[tag] = 0
  return words.keys(), tags.keys()

# Extract and Separate words and tags
print("Separating Words and Tags")
words_brown, tags_brown = extractWords_and_Tags(trainingSentences_brown)
words_conll2000, tags_conll2000 = extractWords_and_Tags(trainingSentences_conll2000)
words_alpino, tags_alpino = extractWords_and_Tags(trainingSentences_alpino)
words_floresta, tags_floresta = extractWords_and_Tags(trainingSentences_floresta)
print "Done!"

# Train Model with Tagsets
print("Creating HMMs")
hmmModel_brown = HMM(tags_brown)
hmmModel_conll2000 = HMM(tags_conll2000)
hmmModel_alpino = HMM(tags_alpino)
hmmModel_floresta = HMM(tags_floresta)

print("Training HMM Model with POS Tags")
hmmModel_brown.train(trainingSentences_brown)
hmmModel_conll2000.train(trainingSentences_conll2000)
hmmModel_alpino.train(trainingSentences_alpino)
hmmModel_floresta.train(trainingSentences_floresta)
print "Done!"

# Evaluate HMM Models Created
print("Calculating Evaluation: TRAINING Sentences")
print("Brown")
print "{0:.2f}% accuracy".format(hmmModel_brown.evaluate(trainingSentences_brown[:10000])*100.0)
print("Cornell")
print "{0:.2f}% accuracy".format(hmmModel_conll2000.evaluate(trainingSentences_conll2000[:10000])*100.0)
print("Alpino")
print "{0:.2f}% accuracy".format(hmmModel_alpino.evaluate(trainingSentences_alpino[:10000])*100.0)
print("Floresta")
#print "{0:.2f}% accuracy".format(hmmModel_floresta.evaluate(trainingSentences_floresta[:10000])*100.0)

print("Calculating Evaluation: TEST Sentences")
print("Brown")
print "{0:.2f}% accuracy".format(hmmModel_brown.evaluate(testSentences_brown[:500])*100.0)
print("Cornell")
print "{0:.2f}% accuracy".format(hmmModel_conll2000.evaluate(testSentences_conll2000[:500])*100.0)
print("Alpino")
print "{0:.2f}% accuracy".format(hmmModel_alpino.evaluate(testSentences_alpino[:500])*100.0)
print("Floresta")
#print "{0:.2f}% accuracy".format(hmmModel_floresta.evaluate(hmmModel_floresta[:500])*100.0)
