# textcounter

<img src="https://user-images.githubusercontent.com/55988954/110457149-9ebf0500-80ca-11eb-88ed-6170e939f6b7.png" width="700" /> 


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


## Count number of words

### Example

```
python count_words.py texts/test.txt
```

<img src="https://user-images.githubusercontent.com/55988954/110466240-cd8ea880-80d5-11eb-85a3-af386e349ef8.png" width="700" /> 

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
