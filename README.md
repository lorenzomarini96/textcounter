# textcounter

<img src="https://user-images.githubusercontent.com/55988954/110457149-9ebf0500-80ca-11eb-88ed-6170e939f6b7.png" width="700" /> 

Suppose we want to count **how many times a given letter is used in a text file**. The fastest way (at least compared to a human being) can be to create a program that, reading an input file, scrolls through all the lines and is able to count the number of words, letters and characters in the text. 
We also would also like to be able to **count the relative frequency** between the various objects analyzed and show a histogram of the frequencies in a more easily readable way.

It may seem like a useless and somewhat tedious operation, but it can be a useful exercise in learning how to use python for data analysis purposes.
# Table of Contents

[Count number of letters](https://github.com/lorenzomarini96/textcounter#count-number-of-letters)

[Count number of words](https://github.com/lorenzomarini96/textcounter#count-number-of-words)

[Count specific words](https://github.com/lorenzomarini96/textcounter#count-specific-words)

[Count top N words](https://github.com/lorenzomarini96/textcounter#count-top-n-words)


## Count number of letters

### Example

```
python3 count_letters.py -hist texts/infinito.
```

<img src="https://user-images.githubusercontent.com/55988954/110463026-b2219e80-80d1-11eb-8188-e0eac2a4aea6.png" width="800" /> 

Output on command line:


## Count number of words

### Example

```
python count_words.py texts/test.txt
```

<img src="https://user-images.githubusercontent.com/55988954/110466240-cd8ea880-80d5-11eb-85a3-af386e349ef8.png" width="700" /> 

Output on command line:
```
-------------------------------------
Statistics of the text:

number of words:         13
number of lines:          3
number of letters:       52
number of characters:    75
-------------------------------------
Frequencies of words:

1) questo          -->  23.08%
2) testo           -->  23.08%
3) è               -->  15.38%
4) un              -->  15.38%
5) non             -->  7.69%
6) test            -->  7.69%
7) invece          -->  7.69%
-------------------------------------
```


## Count specific words

### Example

```
python count_words_find.py texts/infinito.txt
```

<img src="https://user-images.githubusercontent.com/55988954/110457149-9ebf0500-80ca-11eb-88ed-6170e939f6b7.png" width="700" /> 

## Count top N words

### Example

```
python count_words_topN.py texts/infinito.txt
```

<img src="https://user-images.githubusercontent.com/55988954/110457149-9ebf0500-80ca-11eb-88ed-6170e939f6b7.png" width="700" /> 
