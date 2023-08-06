# Python program to train NB, SVM, DT and SNN models
import pandas as pd
import FakeNewsClassifier.nb as nb
import FakeNewsClassifier.svm as svm
import FakeNewsClassifier.dt as dt
import FakeNewsClassifier.snn as snn
import FakeNewsClassifier.saved_model as saved_model
from sklearn.model_selection import train_test_split
import sys
import os

"""
Controlling script with FakeNewsClassifier class and functions.

Detection of Fake News Using Machine learning 
Bachelor's thesis
@author: Matej Koreň
@date: 2023/05/10
"""

# package directory
sk_dataset = os.path.join(os.path.dirname(
    __file__), 'datasets/dezinfo_sk.csv')

VALID_MODELS = ['NB', 'SNN', 'SVM', 'DT']


class FakeNewsClassifier:
    """ Instantiate and initiate a Fake News classifier object. Available functions : train | evaluate. Available models: 'NB' (default)|'SNN'|'SVM'|'DT'"""

    def __init__(self, model: str = 'NB', dataset: str = sk_dataset) -> None:
        if model not in VALID_MODELS:
            raise ValueError(
                "results: status must be one of %r." % VALID_MODELS)
        self.model = model
        self.dataset = dataset
        self.verbose = False
        self.url = ""

    def __str__(self) -> str:
        return f'Used model: {self.model}, Training on: {self.dataset}, Verbose mode: {self.verbose}, URL: {self.url}'

    def train(self, verbose: bool = False):
        """ Train selected model on chosen dataset. Verbosity is optional."""

        self.verbose = verbose
        splitted = split_data(self.dataset)
        train_models(splitted[0], splitted[1], splitted[2],
                     splitted[3], self.model, self.verbose)

    def evaluate(self, verbose: bool = False, url: str = "",):
        """ Evaluate article or full-text with pre-trained model. Verbosity is optional."""

        self.verbose = verbose
        self.url = url
        evaluate_article(self.model, self.url, self.verbose)


def split_data(dataset: str):
    """ Dataset loading and splitting into test and train splits"""
    
    # sk dataset uses ';' as separator 
    if dataset == sk_dataset:
        file = pd.read_csv(dataset, sep=';')
    else:
        file = pd.read_csv(dataset)

    # column check
    if 'text' and 'title' in file.columns:
        file.dropna(subset=['text', 'title'], inplace=True)
        file['Article'] = file['text'] + ' ' + file['title']

    elif 'text' in file.columns:
        file.dropna(subset=['text'], inplace=True)
        file['Article'] = file['text']

    elif 'title' in file.columns:
        file.dropna(subset=['title'], inplace=True)
        file['Article'] = file['title']

    else:
        print('Missing key values in dataset!', file=sys.stderr)

    if 'label' in file.columns:
        label = file['label']
    else:
        print('Missing key values in dataset!', file=sys.stderr)

    # Data splitting (70:30)
    X_train, X_test, y_train, y_test = train_test_split(
        file['Article'], label, test_size=0.3, random_state=1)

    return X_train, X_test, y_train, y_test


def evaluate_article(model: str, url: str, verbose: bool):
    """ Online article evaluation on saved model."""

    if verbose:
        try:
            os.makedirs('figures', exist_ok=True)
            os.makedirs('html', exist_ok=True)
        except OSError:
            print('Unable to create directories', file=sys.stderr)

    # Using pre-trained
    saved_model.saved_model(model, url, verbose)
    return


def train_models(X_train, X_test, y_train, y_test, model: str, verbose: bool):
    """ Training selected models on given dataset."""
    if verbose:
        try:
            os.makedirs('figures', exist_ok=True)
        except OSError:
            print('Unable to create directories', file=sys.stderr)

    # model selection and function calls
    if model == 'NB':
        nb.nb_model(X_train, X_test, y_train,
                    y_test, verbose)

    elif model == 'SVM':
        svm.sv_model(X_train, X_test, y_train,
                     y_test, verbose)

    elif model == 'DT':
        dt.dt_model(X_train, X_test, y_train,
                    y_test, verbose)

    elif model == 'SNN':
        snn.snn_model(X_train, X_test, y_train,
                      y_test, verbose)
    return
