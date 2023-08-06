from scikeras.wrappers import KerasClassifier
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import EarlyStopping
from sklearn.metrics import classification_report
import pandas as pd
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import FakeNewsClassifier.process_text as pt
from datetime import datetime
import dill as pickle

""" 
Sequential neural network (FFNN) algorithm implementation.

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

def snn_model(X_train, X_test, y_train, y_test, verbose):
    """ Function to train and test models, optional confusion matrix plotting."""
    
    def make_model(shape, verbose):
        model = Sequential()  # Model initialization.

        model.add(Dense(128, input_shape=shape,
                  activation='relu'))  # shape input
        model.add(Dense(64, activation='relu'))
        model.add(Dense(2, activation='softmax'))  # FAKE/REAL
        model.compile(
            optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        if verbose:
            print(model.summary())
        return model

    pipeline_snn = Pipeline([
        # strings to token integer counts
        ('bow', CountVectorizer(analyzer=pt.process_text)),
        # integer counts to weighted TF-IDF scores
        ('tfidf', TfidfTransformer())
    ])

    # text fitting
    pipeline_snn.fit(X_train, y_train)

    # matrix creating
    tfidf_var = pipeline_snn.transform(X_train)

    # model initializing
    snn_model = KerasClassifier(model=make_model(tfidf_var.shape[1:], verbose), verbose=1,
                                epochs=10, batch_size=10, callbacks=EarlyStopping(monitor='loss', mode='min', verbose=1))

    # model training
    snn_model.fit(tfidf_var, y_train)

    # test text transforming
    test_var = pipeline_snn.transform(X_test)

    # model testing
    predictions_snn = snn_model.predict(test_var)

    # results
    print('SNN - test')
    print(classification_report(predictions_snn, y_test))

    # saving new model
    while True:
        user_input = input(
            'New model was trained, would you like to save it? (Y/N): ')

        if user_input.lower() == 'y' or 'yes':
            filename = 'model_snn.pk'
            with open(os.path.join(saved_model_dir,filename), 'wb') as file:
                pickle.dump(pipeline_snn, file)
            snn_model.model.save(os.path.join(saved_model_dir,'model_snn.hdf5'))
            break
        elif user_input.lower() == 'n' or 'no':
            break
        else:
            print('Invalid option, please, type yes or no.')

    # additional statistics
    if verbose:

        cm = confusion_matrix(y_test, predictions_snn)
        class_label = [0, 1]
        df_cm = pd.DataFrame(cm, index=class_label, columns=class_label)
        sns.heatmap(df_cm, annot=True, fmt='d', cmap="crest")
        plt.title("Confusion Matrix - Sequential NN")
        plt.xlabel("Predicted Label")
        plt.ylabel("True Label")
        plt.savefig('figures/snn_' +
                    str(datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + '.png')
