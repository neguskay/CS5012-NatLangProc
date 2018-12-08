import math

#this class contains is used to calculate the state
#observation likelihoods for a given state
class StateClass:
  def __init__(self):
    self.StateClass = {}
    self.totWords = 0.0
    self.learningAlpha = .000001 
  
  def insertWord(self, word):
    self.totWords = self.totWords + 1.0
    try:
      self.StateClass[word] = self.StateClass[word] + 1
    except:
      self.StateClass[word] = 1

#Calculates and returns probability of word
  def probOfWord(self, word):
    divDenom = self.totWords+self.learningAlpha
    try:
      return math.log(float(self.StateClass[word])/divDenom, 2)
    except:
      #Smooth/Return small probability if word is unknown
      if self.totWords > 0.0:
        return math.log(self.learningAlpha/divDenom, 2)
      else:
        return -float("inf")