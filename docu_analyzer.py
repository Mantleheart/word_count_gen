

from random import randrange, randint
from PyQt5.QtWidgets import QProgressDialog, QWidget, QMessageBox
from PyQt5 import QtCore
import docx
import numpy as np
import re
import csv
class loadingScreen(QWidget):
    def __init__(self):
        QWidget.__init__(self)


#Source files for words

def clean(list_of_words):
    for i in range(0, len(list_of_words) -1):
        list_of_words[i] = list_of_words[i].replace('\n','')
    return(list_of_words)

def analyze(path):
    words = []
    word_count = {}
    grammar_count = {'nouns' : 0,
                     'adjectives' : 0,
                     'verbs' : 0,
                     'adverbs' : 0
                     }

    target_file = docx.Document(path)
  

    adj = []
    noun = []
    verb = []
    adv = []



    for para in target_file.paragraphs:
        para_as_string = para.text.replace('\n', '')
        words = words + para_as_string.split(' ')

    #count words
        
    for each in words:
        
        word = each.replace('.','').replace(',','').lower()
        try:
            word_count[word] = word_count[word] + 1
        except:
            word_count[word] = 1

    #classify words

    word_collection = list(word_count.keys())


    for each in word_collection:

        is_noun = False
        is_adj = False
        is_verb = False
        is_adv = False
        if each in noun:

            is_noun = True
            grammar_count['nouns'] = grammar_count['nouns'] + 1
        if each in adj:

            is_adj = True
            grammar_count['adjectives'] = grammar_count['adjectives'] + 1
        if each in adv:

            is_adv = True
            grammar_count['adverbs'] = grammar_count['adverbs'] + 1
        if each in verb:

            is_verb = True
            grammar_count['verbs'] = grammar_count['verbs'] + 1
        if len(each):
            if each[-1] == 's':
                if not is_noun and not is_verb:
                    new_word = each[:-1]
                    if new_word in noun:
                        grammar_count['nouns'] = grammar_count['nouns'] + 1

    text = ""
    for key in grammar_count.keys():
        text += key + ' : ' + str(grammar_count[key]) + '\n'
    text += '\n===============================================\n'

    for pair in word_count.items():
       text += ('').join(str(pair).replace('(','').replace(')',''))
       text += '\n'
    doc_name = path[path.rindex('/')+1:-1]
    with open( doc_name[0:-4] +'.csv','w',newline = '') as csvfile:
        names = ['Word','Count']

        writer = csv.DictWriter(csvfile, fieldnames = names)
        writer.writerow({'Word': doc_name ,'Count': ''})
        writer.writerow({'Word':'Parts of Speech','Count':'Number of Occurrences'})
        writer.writerow({'Word':'Nouns','Count':grammar_count['nouns']})
        writer.writerow({'Word':'Verbs','Count':grammar_count['verbs']})
        writer.writerow({'Word':'Adjectives','Count':grammar_count['adjectives']})
        writer.writerow({'Word':'Adverbs','Count':grammar_count['adverbs']})
        
        for pair in word_count.items():
             writer.writerow({'Word': pair[0],'Count': pair[1]})
    return(text)

