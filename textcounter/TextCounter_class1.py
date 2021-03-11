import string
import operator
import os

import matplotlib.pyplot as plt
import seaborn 

class TextCounter:
    """Class to analyze characters, letters and words contained in a text given in input."""

    def __init__(self, file):
        self.file = file
     
    def file_to_text(self):
        """Load the input file and compute number of *"""
        with open(file) as input_file:   
            text = input_file.read()
            return text
    
    def summary(self):
        """Compute general information about the statistic of the text"""
        
        text = self.file_to_text()
        # Number of *
        number_of_words   = len(text.split())
        number_of_chars   = len(text) - len(text.split("\n")) + 1 
        number_of_lines   = len(text.split("\n"))
        number_of_letters = len(''.join(e for e in text if e.isalnum()))
        print("----------------------------------------------")
        print(f"Statistics of the text: {self}\n")
        print(f"Total number of letters {number_of_letters}")
        print(f"Total number of lines: {number_of_lines}")
        print(f"Total number of words: {number_of_words}")
        
    
    def counter_letters(self):
        """Method to make histogram of letters frequency"""
        
        text = self.file_to_text()
        # Number of *
        number_of_words   = len(text.split())
        number_of_chars   = len(text) - len(text.split("\n")) + 1 
        number_of_lines   = len(text.split("\n"))
        number_of_letters = len(''.join(e for e in text if e.isalnum()))
        
        # Create dictionary of letters
        letters_dict = {letters: 0 for letters in string.ascii_lowercase}  

        for letters in text:
            try:                         
                letters_dict[letters.lower()] += 1    
            except KeyError:                  
                pass                          
        
        # Create Histogram
        list_keys_dict   = list(letters_dict.keys())
        list_values_dict = list(letters_dict.values())
        list_items_dict  = list(letters_dict.items())

        xvalues = range(len(list_items_dict))
        yvalues = [val[1]/number_of_letters for val in list_items_dict]
        fig = plt.figure(self.file, figsize=(12,8))
        plt.bar(xvalues, yvalues, edgecolor="black", width=0.5)    
        plt.gcf().set_size_inches(10, 6)
        for i in xvalues:
            if yvalues[i] > 0.0:
                plt.text(xvalues[i]-0.5, yvalues[i]+0.001, "%.2f%%" %round((yvalues[i]*100),2), fontsize=9)
        plt.title("Letter frequencies - %s " %self.file, fontsize=18)
        plt.xlabel("Letters", fontsize=15)
        plt.ylabel("Frequencies [%]", fontsize=15)
        plt.xticks(range(len(list_items_dict)), [val[0] for val in list_items_dict])
        plt.plot([],[], color="white", marker=".", linestyle="None", label=r"Total number of letters: %.i"    %sum(list_values_dict))
        plt.plot([],[], color="white", marker=".", linestyle="None", label=r"Total number of lines: %.i"      %number_of_lines)
        plt.plot([],[], color="white", marker=".", linestyle="None", label=r"Total number of words: %.i"      %number_of_words)
        plt.plot([],[], color="white", marker=".", linestyle="None", label=r"Total number of characters: %.i" %number_of_chars)
        plt.legend(frameon=False, fancybox=True, loc="best", prop={"size": 15})
        plt.savefig(f"histogram_freq_letters_"+os.path.basename(self.file)+".png", bbox_inches="tight")
        plt.show()
        
        print("----------------------------------------------")
        print("Frequency of letters")
        print("----------------------------------------------")
        for number, (lett, num) in enumerate(letters_dict.items()):
            print(f"{number + 1}) {lett:15} --> {num / number_of_letters: .3%}")

        return letters_dict
        
    def counter_words(self):
        """Method to make histogram of words frequency"""
            
        text = self.file_to_text()
        # Number of *
        number_of_words   = len(text.split())
        number_of_chars   = len(text) - len(text.split("\n")) + 1 
        number_of_lines   = len(text.split("\n"))
        number_of_letters = len(''.join(e for e in text if e.isalnum()))
        
        words_dict = {}
        
        for word in text.split():
            if word.lower() in words_dict:
                words_dict[word.lower()] += 1
            else:
                words_dict[word.lower()] = 1
    
        # Orded dict.
        words_dict = dict(sorted(words_dict.items(), key=operator.itemgetter(1), reverse=True))                              
        
    
        # Create Histogram
        list_words_dict   = list(words_dict.keys())
        list_values_dict  = list(words_dict.values())
        list_items_dict   = list(words_dict.items())
        xvalues = range(len(list_items_dict))
        yvalues = [val[1]/number_of_words*100 for val in list_items_dict]
        fig = plt.figure(self.file, figsize=(12,8))
        plt.gcf().set_size_inches(10, 6)
        plt.bar(xvalues, yvalues, facecolor="g", edgecolor="black", width=0.5)    
        for i in xvalues:
            if yvalues[i] > 0.0:
                plt.text(xvalues[i]-0.15, yvalues[i]*(1 + 0.01), "%.2f%%" %round((yvalues[i]),2), fontsize=10)   
        plt.title(r"Words frequencies - %s " %self.file, fontsize=18)
        plt.xlabel(r"$Words$", fontsize=15)
        plt.ylabel(r"$Frequencies$ [%]", fontsize=15)
        plt.ylim(0, 1.5*max(yvalues))
        plt.minorticks_on()
        plt.tick_params(axis='x', which='minor', bottom=False)
        plt.xticks(range(len(list_items_dict)), [val[0] for val in list_items_dict])
        plt.plot([],[], color="white", marker=".", linestyle="None", label=r"Total number of letters letters: %.i" %(number_of_letters))
        plt.plot([],[], color="white", marker=".", linestyle="None", label=r"Total number of letters lines: %.i" %number_of_lines)
        plt.plot([],[], color="white", marker=".", linestyle="None", label=r"Total number of letters words: %.i" %number_of_words)
        plt.plot([],[], color="white", marker=".", linestyle="None", label=r"Total number of letters characters: %.i" %number_of_chars)
        plt.legend(frameon=False, fancybox=True, loc="best", prop={"size": 15})
        plt.savefig("histogram_freq_words_"+os.path.basename(self.file)+".png", bbox_inches="tight")
        plt.show()
        
        print("----------------------------------------------")
        print("Frequency of words")
        print("----------------------------------------------")
        for number, (word, num) in enumerate(words_dict.items()):
            print(f"{number + 1}) {word:15} --> {num / number_of_words: .3%}")
    
        return words_dict
    

    def counter_top_N_words(self, N):
        """Method to make histogram of top N words frequency"""
            
        text = self.file_to_text()
        # Number of *
        number_of_words   = len(text.split())
        number_of_chars   = len(text) - len(text.split("\n")) + 1 
        number_of_lines   = len(text.split("\n"))
        number_of_letters = len(''.join(e for e in text if e.isalnum()))
        
        words_dict = {}
        
        for word in text.split():
            if word.lower() in words_dict:
                words_dict[word.lower()] += 1
            else:
                words_dict[word.lower()] = 1
    
        # Orded dict.
        words_dict = dict(sorted(words_dict.items(), key=operator.itemgetter(1), reverse=True))                              
        words_dict_top_N = dict(list(words_dict.items())[:N])
        
        # Create Histogram
        list_words_dict   = list(words_dict_top_N.keys())
        list_values_dict  = list(words_dict_top_N.values())
        list_items_dict   = list(words_dict_top_N.items())
        xvalues = range(len(list_items_dict))
        yvalues = [val[1]/number_of_words*100 for val in list_items_dict]
        fig = plt.figure(self.file, figsize=(12,8))
        plt.gcf().set_size_inches(10, 6)
        plt.bar(xvalues, yvalues, facecolor="g", edgecolor="black", width=0.5)    
        for i in xvalues:
            if yvalues[i] > 0.0:
                plt.text(xvalues[i]-0.05, yvalues[i]*(1 + 0.01), "%.2f%%" %round((yvalues[i]),2), fontsize=15)   
        plt.title(f"Top {N} words frequencies - {self.file:s} ", fontsize=18)
        plt.xlabel(r"$Words$", fontsize=15)
        plt.ylabel(r"$Frequencies$ [%]", fontsize=15)
        plt.ylim(0, 1.5*max(yvalues))
        plt.minorticks_on()
        plt.tick_params(axis='x', which='minor', bottom=False)
        plt.xticks(range(len(list_items_dict)), [val[0] for val in list_items_dict])
        plt.plot([],[], color="white", marker=".", linestyle="None", label=r"Total number of letters letters: %.i" %(number_of_letters))
        plt.plot([],[], color="white", marker=".", linestyle="None", label=r"Total number of letters lines: %.i" %number_of_lines)
        plt.plot([],[], color="white", marker=".", linestyle="None", label=r"Total number of letters words: %.i" %number_of_words)
        plt.plot([],[], color="white", marker=".", linestyle="None", label=r"Total number of letters characters: %.i" %number_of_chars)
        plt.legend(frameon=False, fancybox=True, loc="best", prop={"size": 15})
        plt.savefig(f"histogram_freq_top_{N}_words_"+os.path.basename(self.file)+".png", bbox_inches="tight")
        plt.show()
        
        for number, (word, num) in enumerate(words_dict_top_N.items()):
            print(f"{number + 1}) {word:15} --> {num / number_of_words: .3%}")
    
        return words_dict_top_N

    def counter_search_words(self, list_search_word):
        """Method to make histogram of words frequency"""
            
        text = self.file_to_text()
        # Number of *
        number_of_words   = len(text.split())
        number_of_chars   = len(text) - len(text.split("\n")) + 1 
        number_of_lines   = len(text.split("\n"))
        number_of_letters = len(''.join(e for e in text if e.isalnum()))
        
        words_dict = {}
        
        for word in text.split():
            if word.lower() in words_dict:
                words_dict[word.lower()] += 1
            else:
                words_dict[word.lower()] = 1
    
        list_find_keys   = []
        list_find_values = []
    
        for word in list_search_word:
            for key in words_dict:
                if  key == word:
                    list_find_keys.append(key)
                    list_find_values.append(words_dict[key])
           
        search_word_dict = dict(zip(list_find_keys, list_find_values))
        # Orded dict.
        #words_dict = dict(sorted(words_dict.items(), key=operator.itemgetter(1), reverse=True))                              
        
    
        # Create Histogram
        list_words_dict   = list(search_word_dict.keys())
        list_values_dict  = list(search_word_dict.values())
        list_items_dict   = list(search_word_dict.items())
        xvalues = range(len(list_items_dict))
        yvalues = [val[1]/number_of_words*100 for val in list_items_dict]
        fig = plt.figure(self.file, figsize=(12,8))
        plt.gcf().set_size_inches(10, 6)
        plt.bar(xvalues, yvalues, facecolor="g", edgecolor="black", width=0.1)    
        for i in xvalues:
            if yvalues[i] > 0.0:
                plt.text(xvalues[i]-0.15, yvalues[i]*(1 + 0.01), "%.2f%%" %round((yvalues[i]),2), fontsize=10)   
        plt.title(r"Searched words frequencies - %s " %self.file, fontsize=18)
        plt.xlabel(r"$Words$", fontsize=15)
        plt.ylabel(r"$Frequencies$ [%]", fontsize=15)
        plt.ylim(0, 1.5*max(yvalues))
        plt.minorticks_on()
        plt.tick_params(axis='x', which='minor', bottom=False)
        plt.xticks(range(len(list_items_dict)), [val[0] for val in list_items_dict])
        plt.plot([],[], color="white", marker=".", linestyle="None", label=r"Total number of letters letters: %.i" %(number_of_letters))
        plt.plot([],[], color="white", marker=".", linestyle="None", label=r"Total number of letters lines: %.i" %number_of_lines)
        plt.plot([],[], color="white", marker=".", linestyle="None", label=r"Total number of letters words: %.i" %number_of_words)
        plt.plot([],[], color="white", marker=".", linestyle="None", label=r"Total number of letters characters: %.i" %number_of_chars)
        plt.legend(frameon=False, fancybox=True, loc="best", prop={"size": 15})
        plt.savefig("histogram_freq_search_words_"+os.path.basename(self.file)+".png", bbox_inches="tight")
        plt.show()
        
        print("----------------------------------------------")
        print("Frequency of searched words")
        print("----------------------------------------------")
        for number, (word, num) in enumerate(search_word_dict.items()):
            print(f"{number + 1}) {word:15} --> {num / number_of_words: .3%}")
    
        return search_word_dict

if __name__ == "__main__":
    #file = "testo.txt"
    file = "texts/infinito.txt"
    # Creo l'istanza della classe
    istanza = TextCounter(file)
    print(istanza.summary())

    dizionario_lettere = istanza.counter_letters()
    dizionario_parole  = istanza.counter_words()
    dizionario_parole_top_N = istanza.counter_top_N_words(3)
    dizionario_cerca_parole = istanza.counter_search_words("sempre" "e")
