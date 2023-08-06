# Detection of Fake News Using Machine Learning
## Bachelor's thesis
### Author: Matej Koreň, 2022
### Brno University of Technology
### Faculty of Information Technology

## Introduction

This project focuses on the use of machine learning in fake news detection. For this purpose, four models have been selected -- Bayesian, Decision Tree, Support Vector Machine and a Neural network. In five experiments on various datasets, these models were trained, tested, evaluated and compared with state-of-the-art methods. Final implementation is in the form of a package (or console application), which allows it's users to replicate this procedure with their own data.

## Installing final product directly

1. Unzip FakeNewsCLassifier project package
2. Open terminal
3. Install requirements
> pip3 install -r requirements.txt

note: additional NLP libraries will install automatically with first run.

## Alternative - installing FakeNewsClassifier package

To use these models in different project, this package can be installed from official PyPi index:

> pip3 install FakeNewsClassifier

which checks for dependencies and loads all needed modules. Importing the module

> from FakeNewsClassifier import models


## Running scripts directly

To run the program, input arguments must be used:

- -m / -–model = model selection, options:
    - SNN = Sequential neural network,
    - NB = Naive Bayes,
    - SVM = Support vector machine,
    - DT = Decision tree,
- -p / -–pretrained = skips the training, pretrained model is used,
- -url / -–url [Online article] = article to parse and evaluate,
- –v / –-verbose = verbose mode, showing graphs and explanations.


## Using the FakeNewsClassifier package

1. Object initialization, which takes two arguments

    > classifier = FakeNewsClassifier.models.FakeNewsClassifier(model:str, dataset:str)
    
    where **model** is one of [SNN, NB, SVM, DT],
    and **dataset** is a relative path to dataset in csv format (by default it's Dezinfo SK included in the package).

2. Model training, which has optional "verbose" parameter:
    > classifier.train(verbose:bool)

3. Article evaluation, also with "verbose" and "url" argument:
    > classifier.evaluate(verbose:bool, url:str)
    
    where **url** is a link to an online article or full-text to evaluate.


## Code snippets and commands

Minimalistic python script to achieve functionality would look like this:

```
from FakeNewsClassifier import models as FNC

article_url="https://www.ta3.com/clanok/265328/na-matovica-podali-pre-potycku-na-pochode-za-prava-trans-udi-trestne-oznamenie"

lol = FNC.FakeNewsClassifier('NB')  # unused argument 'dataset=' is by default looking for dezinfo_sk dataset within package
lol.train(verbose=True)             # specified model training, optional verbosity
lol.evaluate(verbose=True,url=article_url)  # article evluation on trained model, optional verbosity

```
If the train() method is not called, evaluate() will use default pretrained models within package.

When running scripts directly, same funcionality can be obtained like this:

> python3 main.py -m NB -v

which trains NB model on default dezinfo_sk dataset within package. Alternatively, you can specify it using: **-d path/data.csv**.

> python3 main.py -m NB -v -p -url https://www.ta3.com/clanok/265328/na-matovica-podali-pre-potycku-na-pochode-za-prava-trans-udi-trestne-oznamenie

which evaluates article from **-url** argument.

Note: if verbosity is allowed, matrices are stored in *figures/* folder and Lime analytics in *html/* folder.

## Additional requirements and warnings

### Dataset structure

Datasets to perform training on need to be in a standard *csv* file format and must contain collumns
- **label** with two values, e.g. "Fake"/"True" or "0/1",
- **text** or **title** (or both) with article titles and bodies.

Other collumns are neglected.

#### Recomended english datasets

WELFake dataset (Saurabh Shahane):
https://www.kaggle.com/datasets/saurabhshahane/fake-news-classification

Fake and Real news dataset (Clément Bisaillon):
https://kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset

Real & Fake news (nop.ai):
https://www.kaggle.com/datasets/nopdev/real-and-fake-news-dataset

### Online articles

When provided with url, buiilt-in scraper will try to parse given page and extract the title and body. However,
many websites are protected against automated scraping and bot attacks, which makes the online evaluation impossible.
Alternatively, full-text can be used as the article to evaluate.