#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 21:48:21 2020

@author: lorenzomarini

Program that counts the relative frequencies of words in all text in 
a folder given in input.

website: https://www.gutenberg.org/files/997/997.txt
"""

import argparse 
import logging
import glob 
import os
import operator 

import matplotlib.pyplot as plt

logging.basicConfig(level=logging.INFO)

def counter_words(file_path):
    """Read a text file and compile the words statistics.
    

    Parameters
    ----------
    file_path : path of the file 

    Returns
    -------
    dictionary containing words as keys and letter 
    relative frequencies as values..

    """

    with open(file_path) as input_file: 
        text = input_file.read()
        
        # Compute total number of characters in the file.
        number_of_characters = len(text)
        
        # Compute total number of words.
        translate_text  = text.maketrans({char: None for char in ""'!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'""})
        clean_text      = text.lower().translate(translate_text)     
        number_of_words = len(clean_text.split())
        
        # Compute the number of lines in the file.
        number_of_lines = text.count("\n") + 1
        
        # Compute the number of letters in the file.
        letters = ''.join(e for e in text if e.isalnum())
        number_of_letters= len(letters)
     
    words_dictonary = {}
        
    for word in clean_text.split():
        if word.lower() in words_dictonary:
            words_dictonary[word.lower()] += 1
        else:
            words_dictonary[word.lower()] = 1
    
    # Orded dict.
    words_dictonary = dict(sorted(words_dictonary.items(), key=operator.itemgetter(1), reverse=True))                              
    #print(words_dictonary)
    
    #for i, (word, value) in enumerate(words_dictonary.items()):
        #print(f"{i}) {word} --> {value/number_of_words: .2%}")
    
    # Create Histogram
    #list_words_dict   = list(words_dictonary.keys())
    #list_values_dict  = list(words_dictonary.values())
    list_items_dict   = list(words_dictonary.items())
     
    xvalues = range(len(list_items_dict))
    yvalues = [(val[1]/number_of_words)*100 for val in list_items_dict]
    fig = plt.figure(file_path, figsize=(12,8))
    plt.bar(xvalues, yvalues, facecolor="g", edgecolor="black", width=0.3)    
    # Bellurie
    # Print the %values of the letters above each value in the histogram.
    for i in xvalues:
        if yvalues[i] > 0.0:
            plt.text(xvalues[i]-0.15, yvalues[i]*(1 + 0.01), "%.2f%%" %round((yvalues[i]),2), fontsize=14)   
    plt.title(r"%s " %file_path, fontsize=14)
    plt.suptitle(r"Histogram of words frequencies", fontsize=14)
    plt.xlabel(r"$Words$", fontsize=14)
    plt.ylabel(r"$Frequencies$ [%]", fontsize=14)
    plt.ylim(0, 1.5*max(yvalues))
    plt.minorticks_on()
    plt.tick_params(axis='x', which='minor', bottom=False)
    plt.xticks(range(len(list_items_dict)), [val[0] for val in list_items_dict])
    plt.plot([],[], color="white", marker=".", linestyle="None", label=r"# letters:    %6.i" %(number_of_letters))
    plt.plot([],[], color="white", marker=".", linestyle="None", label=r"# lines:      %6.i" %number_of_lines)
    plt.plot([],[], color="white", marker=".", linestyle="None", label=r"# words:      %6.i" %number_of_words)
    plt.plot([],[], color="white", marker=".", linestyle="None", label=r"# characters: %6.i" %number_of_characters)
    plt.legend(frameon=False, fancybox=True, loc="best", prop={"size": 10})
    #plt.savefig("FIGURE_COUNT_WORD/histogram_freq_words_"+os.path.basename(file_path)+".pdf", bbox_inches="tight")
    plt.show()
    print("-------------------------------------")
    print("Statistics of the text:\n")
    print(f"number of words:      {number_of_words:5}")
    print(f"number of lines:      {number_of_lines:5}")
    print(f"number of letters:    {number_of_letters:5}")
    print(f"number of characters: {number_of_characters:5}")
    print("-------------------------------------")
    print("Frequencies of words:\n")
    for number, (word, value) in enumerate(words_dictonary.items()):
        print(f"{number + 1}) {word:15} --> {value/number_of_words: 3.2%}")
    print("-------------------------------------")

    return fig

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Program that counts the relative frequencies of words in all text in a folder given in input.")
    # Positional argument:
    parser.add_argument("infolder", type=str, help="Path to the input folder.")
    # Opzional argument 
    parser.add_argument("-hist", "--histogram", help="Display histogram of the words frequencies.", action="store_true")
    args = parser.parse_args()
    
    #fig = counter_words(args.infile)
    if args.histogram:
        for file in glob.glob(args.infolder+"/*.txt"): # For all .txt file in the given folder.
            print("\n========================================")
            print(f"{file}")
            print("========================================")
        
            fig = counter_words(file)
            plt.show()
            
    else:
        for file in glob.glob(args.infolder+"/*.txt"): # For all .txt file in the given folder.
            print("\n========================================")
            print(f"{file}")
            print("========================================")
            fig = counter_words(file)
   

