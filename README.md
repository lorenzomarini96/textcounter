# textcounter

<img src="https://user-images.githubusercontent.com/55988954/110457149-9ebf0500-80ca-11eb-88ed-6170e939f6b7.png" width="700" /> 

Suppose we want to count how many times a given letter is used in a text file. The fastest way (at least compared to a human being) can be to create a program that, reading an input file, scrolls through all the lines and is able to count the number of words, letters and characters in the text.

We also would also like to be able to count the relative frequency between the various objects analyzed and show a histogram of the frequencies in a more easily readable way.
It may seem like a useless and somewhat tedious operation (certainly for my friends :)), but it can be a useful exercise to learn how to use python for data analysis purposes.

The textcounter package aims to read an input file and create:

- the histogram of the occurrences of the **letters**
- the histogram of the occurrences of the **words**
- the histogram of the occurrences of the **N** (integer value chosen by the user) **most used words**
- the histogram of only the **words chosen** by the user


# Table of Contents
* [Getting Started](https://github.com/lorenzomarini96/textcounter#getting-started)
    * [Prerequisites](https://github.com/lorenzomarini96/textcounter#prerequisites)

* [textcounter package](https://github.com/lorenzomarini96/textcounter#textcounter-package)
    * [Count number of letters](https://github.com/lorenzomarini96/textcounter#count-number-of-letters)

    * [Count number of words](https://github.com/lorenzomarini96/textcounter#count-number-of-words)

    * [Count specific words](https://github.com/lorenzomarini96/textcounter#count-specific-words)

    * [Count top N words](https://github.com/lorenzomarini96/textcounter#count-top-n-words)

* [Repo structure](https://github.com/lorenzomarini96/textcounter#repo-structure)

* [Contributing]()

* [Author]()

* [License]()

* [Acknowledgments]()


## Getting Started

### Prerequisites

## textcounter package

### Count number of letters

#### Example

```
python3 count_letters.py -hist texts/infinito.
```

<img src="https://user-images.githubusercontent.com/55988954/110463026-b2219e80-80d1-11eb-8188-e0eac2a4aea6.png" width="800" /> 

Output on command line:

### Count number of words

#### Example

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


### Count specific words

#### Example

```
python count_words_find.py texts/infinito.txt
```

<img src="https://user-images.githubusercontent.com/55988954/110457149-9ebf0500-80ca-11eb-88ed-6170e939f6b7.png" width="700" /> 

### Count top N words

#### Example

```
python count_words_topN.py texts/infinito.txt
```

<img src="https://user-images.githubusercontent.com/55988954/110457149-9ebf0500-80ca-11eb-88ed-6170e939f6b7.png" width="700" /> 

## Repo structure
```
textcounter/
├── LICENSE
├── README.md
├── docs
├── tests
│   ├── README.md
│   ├── __init__.py
│   └── texts
│       ├── infinito.txt
│       ├── test.txt
│       └── yellow_submarine.txt
└── textcounter
    ├── README.md
    ├── __init__.py
    ├── count_letters.py
    ├── count_words.py
    ├── count_words_find.py
    ├── counts_words_topN.py
    ├── figures_count_letters
    ├── figures_count_words
    ├── figures_find_words
    ├── figures_topN_words
    ├── text_DantesInferno
    └── texts
```

## Contributing

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.

## Author
- Lorenzo Marini - *Initial work*


## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/lorenzomarini96/textcounter/blob/main/LICENSE) file for details.

## Acknowledgments