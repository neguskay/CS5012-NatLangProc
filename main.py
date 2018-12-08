'''
UNIVERSITY OF ST ANDREWS
CS5012 - LANGUAGE AND COMPUTATION
PRACTICAL 2 - GRAMMAR ENGINEERING
STUDENT ID: 170027939
'''
# TO-DO
# - Complete unification
# - Do Testing and checking for parsing to return boolean
## Run the NLTK Parser

from nltk import CFG, ChartParser, grammar, FeatureChartParser

# Init CFG form
# RS = Rest of the sentence i.e main sentence

cf_grammar = CFG.fromstring("""\
S -> NP VP | CON NP VP | ADV V NP VP 
NP -> ProperNoun | ProperNoun CON ProperNoun | ADJ NN | ProperNoun VP | NN | ADV NN | NN PP NN | DET NN
CON -> ConjunctiveWord | ConjunctiveWord NP VP
VP -> V | V NN | V NP | DET ADJ NN | V ProperNoun | VP NN | ADV V | V ProperNoun VP | VP NP PP
ADJ -> Adjective | Adjective Adjective
DET -> Determinant
ADV -> Adverb  
PP -> PP NP | Preposition DET NN | Preposition DET



ProperNoun -> 'Bart' | 'Homer' | 'Lisa' 
V -> 'laughs' | 'laughed' | 'drink' | 'wears' | 'serves' | 'drinks' | 'thinks' | 'does' | 'do' | 'wear' | 'laugh'
ConjunctiveWord -> 'and' | 'when'
NN -> 'milk' | 'shoes' | 'salad' | 'kitchen' | 'midnight' | 'table'
Adjective -> 'blue' | 'healthy' | 'green'
Determinant -> 'a' | 'the'
Adverb -> 'always' | 'never' | 'before' | 'when'
Preposition -> 'in' | 'on'
""")

#NP -> ProperNoun 
#ProperNoun -> 'Homer' | 'Bart' 
#VP -> V
#V -> 'laughs' | 'laughed' | 

# Produce Trees for Step 2


# Init Parser
cf_parser = ChartParser(cf_grammar)

# Init Sentences to test
correct_grammar_sents = """\
Bart laughs
Homer laughed
Bart and Lisa drink milk
Bart wears blue shoes
Lisa serves Bart a healthy green salad
Homer serves Lisa
Bart always drinks milk
Lisa thinks Homer thinks Bart drinks milk
Homer never drinks milk in the kitchen before midnight
when Homer drinks milk Bart laughs
when does Lisa drink the milk on the table
when do Lisa and Bart wear shoes
"""
# Example texts So far, it looks just like a slightly more verbose alternative to what was specified i


# print("Printing Trees")
def _parse_and_print_cfg(sents):
    for i in range(len(sents)):
        parses = cf_parser.parse(sents[i].split())
        print("\r\n")
        print"Sentence",i+1," : ", 
        print(sents[i])
        for tree in parses:
            print(tree)


# Split all lines into lists and check for structuew
sents_split = correct_grammar_sents.splitlines()
_parse_and_print_cfg(sents_split)

#'''
# Part 4, with features [number? singular/plural] and subcategorisation
# base = third plural, vbz = singular, pret = past
# sg = singular, pl = plural
grammar_feature = grammar.FeatureGrammar.fromstring("""\
S -> NP[NUM=?sg] VP[FORM=?vbz] | NP[NUM=?pl] VP[FORM=?base] | CON[T=?gen] NP[NUM=?sg] VP[FORM=?vbz] | CON[T=?gen] VP[FORM=?vbz] 
NP[NUM=?sg] -> ProperNoun[NUM=?sg] | ADJ[T=?gen] NN[NUM=?sg] | ProperNoun[NUM=?sg] NN[NUM=?sg] | ProperNoun[NUM=?sg] VP[FORM=?vbz] | NN[NUM=?sg] VP[FORM=?vbz] | NN[NUM=?sg] NP[NUM=?sg] | NN[NUM=?sg] PP[T=?cpd] | ADV[T=?des] NN[NUM=?sg] 
NP[NUM=?pl] -> ProperNoun[NUM=?sg] CON[T=?gen] ProperNoun[NUM=?sg]
NN[NUM=?sg] -> NN[NUM=?sg] | DET[NUM=?sg] ADJ[T=?gen] NN[NUM=?sg] | DET[NUM=?sg] NN[NUM=?sg]
VP[FORM=?vbz] -> V[FORM=?vbz] | V[FORM=?vbz] NP[NUM=?sg]| V[FORM=?pret] | VP[FORM=?vbz] NP[NUM=?sg] | ADV[T=?des] V[FORM=?vbz] | V[FORM=?vbz] ProperNoun[NUM=?sg] VP[FORM=?vbz]
VP[FORM=?base] -> V[FORM=?base] | V[FORM=?base] NN[NUM=?pl]
ADJ[T=?gen] -> Adjective[CAT=?col] | Adjective[CAT=?des] Adjective[CAT=?col]
ADV[T=?des] -> Adverb[T=?des]
PP[T=?cpd] -> Preposition[T=?gen] DET[NUM=?sg] | PP[T=?cpd] NP[NUM=?sg] | PP[T=?cpd] NN[NUM=?sg]
CON[T=?gen] -> ConjuctiveJoin[NUM=?pl] | ConjuctiveConditional[T=?con] NP[NUM=?sg] | CON[T=?gen] NP[NUM=?sg] VP[FORM=?vbz] | ConjuctiveConditional[T=?quest] VP[FORM=?vbz]


ProperNoun[NUM=?sg] -> 'Bart' | 'Homer' | 'Lisa'
V[FORM=?vbz] -> 'laughs' | 'wears' | 'serves' | 'drinks' | 'thinks' | 'does' | 'do'
V[FORM=?pret] -> 'laughed'
V[FORM=?base] -> 'drink' | 'wear' | 'laugh'
DET[NUM=?sg] -> 'a' | 'the'
Adjective[CAT=?des] -> 'healthy'
Adjective[CAT=?col] -> 'blue' | 'green'
Adverb[T=?des] -> 'always' | 'never' | 'before'
Preposition[T=?gen] -> 'in' | 'on' 
NN[NUM=?sg] -> 'shoes' | 'salad' | 'milk' | 'kitchen' | 'midnight' | 'table'
NN[NUM=?pl] -> 'milk' | 'shoes'
ConjuctiveJoin[NUM=?pl] -> 'and'
ConjuctiveConditional[T=?con] -> 'when'
ConjuctiveConditional[T=?quest] -> 'when'
""")

grammar_feature_parser = FeatureChartParser(grammar_feature)
#'''

def _parse_and_print_unification(sents):
    for i in range(len(sents)):
        parses = grammar_feature_parser.parse(sents[i].split())
        print("\r\n")
        print"Sentence",i+1," : ", 
        print(sents[i])
        for tree in parses:
            print(tree)

_parse_and_print_unification(sents_split)


wrong_grammar_sents = """\
Bart laugh
when do Homer drinks milk
Bart laughs the kitchen
"""
wrong_sents_split = wrong_grammar_sents.splitlines()
def _test_wrong_grammar_sents():
    print("\n\r")
    print("TESTING WRONG GRAMMAR SENTENCES")
    print("********************************************")
    print("CONTEXT-FREE TEST")
    _parse_and_print_cfg(wrong_sents_split)
    print("\n\r")
    print("TESTING WRONG GRAMMAR SENTENCES")
    print("********************************************")
    print("UNIFICATION GRAMMAR TEST")
    _parse_and_print_unification(wrong_sents_split)


_test_wrong_grammar_sents()
