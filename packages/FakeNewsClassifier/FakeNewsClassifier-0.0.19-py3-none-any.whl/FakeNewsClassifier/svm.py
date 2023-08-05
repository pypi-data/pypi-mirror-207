from sklearn.metrics import classification_report
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import FakeNewsClassifier.process_text as pt
from sklearn.metrics import confusion_matrix
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import dill as pickle
from datetime import datetime

""" 
Support Vector Machine algorithm implementation.

Detection of Fake News Using Machine learning 
Bachelor's thesis
@author: Matej Koreň
@date: 2023/05/10
"""

# Tensorflow warning silencer
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# package directory
saved_model_dir = os.path.join(os.path.dirname(__file__), 'saved_models/')


def sv_model(X_train, X_test, y_train, y_test, verbose):
    """ Function to train and test models, optional confusion matrix plotting."""
    
    pipeline_sv = Pipeline([
        # strings to token integer counts
        ('bow', CountVectorizer(analyzer=pt.process_text)),
        # integer counts to weighted TF-IDF scores
        ('tfidf', TfidfTransformer()),
        # train w/ Support Vectors classifier
        ('classifier', SVC(C=1.0, kernel='linear', gamma='auto', probability=True)),
    ])

    #training
    pipeline_sv.fit(X_train, y_train)

    #testing
    predictions_SVM = pipeline_sv.predict(X_test)

    #results
    print('SVM - test')
    print(classification_report(predictions_SVM, y_test))

    # saving new model
    while True:
        user_input = input('New model was trained, would you like to save it? (Y/N): ')

        if user_input.lower() == 'y' or 'yes':
            filename = 'model_svm.pk'
            with open(os.path.join(saved_model_dir,filename), 'wb') as file:
                pickle.dump(pipeline_sv, file)
            break
        elif user_input.lower() == 'n' or 'no':
            break
        else:
            print('Invalid option, please, type yes or no.')

    # additional statistics
    if verbose:

        # confusion matrix
        cm = confusion_matrix(y_test, predictions_SVM)
        class_label = [0, 1]
        df_cm = pd.DataFrame(cm, index=class_label, columns=class_label)
        sns.heatmap(df_cm, annot=True, fmt='d', cmap="crest")
        plt.title("Confusion Matrix - Support vectors")
        plt.xlabel("Predicted Label")
        plt.ylabel("True Label")
        plt.savefig('figures/svm' +
                    str(datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + '.png')

