#!/usr/bin/env python
# encoding: utf-8
"""
wordcounting.py

Created by Arasy on 2019-01-06.
Copyright (c) 2019 ACT. All rights reserved.
"""


from nltk import *
from nltk.util import ngrams
import sys

global unigram_fd, bigram_fd, trigram_fd

def show():
    print("unigram list :")
    for i in unigram_fd:
        print(i)

    print("\nbigram list :")
    for i in bigram_fd:
        print(i)

    print("\ntrigram list :")
    for i in trigram_fd:
        print(i)

    menu()

def save():
    namafile = input("\n\nthe file will be saved as :\n1. <filename>-unigram.txt,\n2. <filename>-bigram.txt, and\n3. <filename>-trigram.txt\nwhat shall the filename be?")
    hasil1 = open(namafile+"-unigram.txt","w")
    hasil2 = open(namafile+"-bigram.txt","w")
    hasil3 = open(namafile+"-trigram.txt","w")

    for i in unigram_fd:
        hasil1.write("%s \n" % str(i))
        #print(i)

    for i in bigram_fd:
        hasil2.write("%s \n" % str(i))
        #print(i)

    for i in trigram_fd:
        hasil3.write("%s \n" % str(i))
        #print(i)

    hasil1.close()
    hasil2.close()
    hasil3.close()

    menu()


def quit():
    sys.exit()


def menu():
    print("\nmenu :\n")
    print("1. show\n")
    print("2. save to file!\n")
    print("3. exit\n")
    choice = int(input("what is your choice?"))
    switcher = {1:show, 2:save, 3:quit}
    if choice in [1,2,3]:
        return switcher.get(choice,"nothing")()
    else:
        menu()


def count(filename):
    artikel = open(filename,"r").read()

    # tanda baca koma dan titik dihilangkan, stopword the, a dihilangkan
    for sym in ["\n","\t","(",")","``","/","''","\\",".",",", " the ", " a ", "-"]:
        artikel = artikel.replace(sym," ")

    kalimat = sent_tokenize(artikel)
    token = []
    for klm in kalimat:
        token.append(word_tokenize(klm))

    listunigram = []
    listbigram = []
    listtrigram = []
    for tk in token:
    #    unigram = ngrams(tk, 1, pad_right=True, pad_left=True, left_pad_symbol="<s>", right_pad_symbol="</s>")
    #    bigram = ngrams(tk, 2, pad_right=True, pad_left=True, left_pad_symbol="<s>", right_pad_symbol="</s>")
    #    trigram = ngrams(tk, 3, pad_right=True, pad_left=True, left_pad_symbol="<s>", right_pad_symbol="</s>")

    # tanda baca koma dan titik dihilangkan, tanpa padding
        unigram = ngrams(tk, 1)
        bigram = ngrams(tk, 2)
        trigram = ngrams(tk, 3)

        for gram in unigram:
            listunigram.append(gram)
        for gram in bigram:
            listbigram.append(gram)
        for gram in trigram:
            listtrigram.append(gram)

    global unigram_fd, bigram_fd, trigram_fd
    unigram_fd = FreqDist(listunigram)
    bigram_fd = FreqDist(listbigram)
    trigram_fd = FreqDist(listtrigram)

    #sorting
    unigram_fd = list(unigram_fd.items())
    unigram_fd.sort(key=lambda item: item[-1], reverse=True)
    bigram_fd = list(bigram_fd.items())
    bigram_fd.sort(key=lambda item: item[-1], reverse=True)
    trigram_fd = list(trigram_fd.items())
    trigram_fd.sort(key=lambda item: item[-1], reverse=True)
    print("counting finished!")
    menu()


if __name__ == '__main__':
    if len(sys.argv)<2:
        print("please specify a file to count!\nuse this format : python wordcounting.py <filename>")
    elif len(sys.argv)>2:
        print("too much argument!\n")
    else:
        if os.path.isfile(sys.argv[1]):
            print("counting file %s begin!\n" % sys.argv[1])
            count(sys.argv[1])
        else:
            print("file %s not found!!\n" % sys.argv[1])
