import argparse
import sys
import FakeNewsClassifier.models as models

"""
Main script to run the program.

Detection of Fake News Using Machine learning 
Bachelor's thesis
@author: Matej Koreň
@date: 2023/05/10
"""

# command line arguments
parser = argparse.ArgumentParser(
    description='Python program to train NB, SVM, DT and SNN models')


parser.add_argument("-m", "--model", action="store",
                    dest="model", help='Model to be used, available: NB, SVM, DT, SNN', required=True)

parser.add_argument("-p", "--pretrained", action="store_true",
                          dest="use_saved", help='Use pre-trained model')

parser.add_argument("-d", "--data", action="store",
                    default='FakeNewsClassifier/datasets/dezinfo_sk.csv',  dest="dataset", help='Path to dataset')

parser.add_argument("-url", "--url", action="store",
                    dest="url", default=None, help='Article url')

parser.add_argument("-v", "--verbose", action="store_true",
                    dest="verbose", help='Toggle verbosity')

arguments = parser.parse_args()

if str(arguments.model) not in ["SNN", "DT", "NB", "SVM"]:
    print('Wrong model, see -h / --help .', file=sys.stderr)


#  Create Fake News Classifier object
exp = models.FakeNewsClassifier(str(arguments.model), str(arguments.dataset))

# use pretrained
if arguments.use_saved:
    exp.evaluate(arguments.verbose, str(arguments.url))

# train new model
else:
    exp.train(arguments.verbose)
