#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 18:22:52 2020

@author: lorenzomarini

Program that counts the relative frequencies of letters in all text in 
a folder given in input and make the histogram of the frequencies.

website: https://www.gutenberg.org/files/997/997.txt
"""

import argparse 
import logging  
import time     
import string
import glob 

import matplotlib.pyplot as plt

logging.basicConfig(level=logging.INFO)

def counter_letters(file_path):
	""" Reads a text file and compile the letter statistics.
    
        Input:  path of the file 
        
        Output: dictionary containing letters as keys and letter 
                relative frequencies as values.
    """
    # Measure of execution time
	start_time = time.time()

	logging.info("Reading input file %s", file_path) 

	number_of_lines = 0
	number_of_words = 0 
       
	with open(file_path) as input_file:   
		text = input_file.read()
		number_of_chars = len(text)
        
		for line in text:
 		    line  = line.strip("\n") # Do not want to count "\ n" as a character
 		    words = line.split()     # Divide the words among them. 
 		    number_of_lines += 1
 		    number_of_words += len(words) 
    
    # Total number of lines
	print(f"Total number of lines: {number_of_lines}")
    # Total number of words
	print(f"Total number of words: {number_of_words}")
    # Total number of characters
	#logging.info("Done, %d characters found.", number_of_chars)
	print(f"Total number of characters: {number_of_chars}")

	# Create dictionary of the characters
	char_dict = {ch: 0 for ch in string.ascii_lowercase}  

	for ch in text:
		try:                         
			char_dict[ch.lower()] += 1    
		except KeyError:                  
			pass                          

    # Measure of execution time
	elapsed_time = time.time() - start_time
	logging.info("Done in %.3f seconds", elapsed_time)  

    # Count the number of letters (I will use it for normalization)
	number_of_letters = sum(char_dict.values()) 
	print(f"Total number of letters {number_of_letters}")

	for ch, num in char_dict.items():
        #prints the analysis result 
		print(f"{ch} --> {num / number_of_letters: .3%}") # 

def histogram(file_path):
	number_of_lines = 0
	number_of_words = 0 
       
	with open(file_path) as input_file:   
		text = input_file.read()
		number_of_chars = len(text)
        
		for line in text:
 		    line  = line.strip("\n") # Do not want to count "\ n" as a character
 		    words = line.split()     # Divide the words among them. 
 		    number_of_lines += 1
 		    number_of_words += len(words) 
    
    # Total number of lines
	print(f"Total number of lines: {number_of_lines}")
    # Total number of words
	print(f"Total number of words: {number_of_words}")
    # Total number of characters
	#logging.info("Done, %d characters found.", number_of_chars)
	print(f"Total number of characters: {number_of_chars}")
	# Create dictionary of the characters
	char_dict = {ch: 0 for ch in string.ascii_lowercase}  

	for ch in text:
		try:                         
			char_dict[ch.lower()] += 1    
		except KeyError:                  
			pass  
                        
    # Count the number of letters (I will use it for normalization)
	number_of_letters = sum(char_dict.values()) 
	print(f"Total number of letters {number_of_letters}")
    
	for ch, num in char_dict.items():
        	#prints the analysis result 
		print(f"{ch} --> {num / number_of_letters: .3%}") # 

    # Create Histogram
	list_keys_dict   = list(char_dict.keys())
	list_values_dict = list(char_dict.values())
	list_items_dict  = list(char_dict.items())
    
	xvalues = range(len(list_items_dict))
	yvalues = [val[1]/number_of_letters for val in list_items_dict]
	fig = plt.figure(file_path, figsize=(10,6))
	plt.bar(xvalues, yvalues, facecolor="g", edgecolor="black", width=0.3)    
	ax = plt.axes()
	plt.gcf().set_size_inches(10, 6)
	# Print the %values of the letters above each value in the histogram.
	for i in xvalues:
		if yvalues[i] > 0.0:
			ax.text(xvalues[i]-0.5, yvalues[i]+0.001, "%.2f%%" %round((yvalues[i]*100),2), fontsize=8)

	# Bellurie
	ax.set_title("Histogram of letter frequencies - %s " %file_path)
	ax.set_xlabel("Letters")
	ax.set_ylabel("Frequencies")
	#plt.minorticks_on()
	plt.xticks(range(len(list_items_dict)), [val[0] for val in list_items_dict])
	ax.plot([],[], color="white", marker=".", linestyle="None", label=r"Total number of letters: %.i" %sum(list_values_dict))
	ax.plot([],[], color="white", marker=".", linestyle="None", label=r"Total number of lines: %.i" %number_of_lines)
	ax.plot([],[], color="white", marker=".", linestyle="None", label=r"Total number of words: %.i" %number_of_words)
	ax.legend(frameon=False, fancybox=True, loc="best", prop={"size": 10})
	#plt.savefig(f"histogram_freq_letters.pdf", bbox_inches="tight")
	plt.show()
	return fig

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Program that counts the relative frequencies of letters in all text in a folder given in input.")
    
    # Positional argument
    parser.add_argument("infolder", type=str, help="Path to the input folder.")
    # Opzional argument
    parser.add_argument("-hist", "--histogram", help="Display histogram of the letter frequencies.", action="store_true")
    args = parser.parse_args()
    
    #counter_letters(args.infolder)
    if args.histogram:
        #counter_letters(args.infolder)
        for file in glob.glob(args.infolder+"/*.txt"): # For all .txt file in the given folder.
			#print("\n========================================")
            print(f"{file}")
            print("========================================")
            histogram(file)
			
    '''
	else:
		#print("\n========================================")
        print(f"{file}")
        print("========================================")
        counter_letters(args.infolder)
	'''
    
    
    
    
    
    
    
    