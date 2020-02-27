import pickle

import numpy as np

from flask import Flask, render_template, request

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import StandardScaler


app = Flask(__name__)

# model components
with open('pickle/word2token.pickle', 'rb') as f:
    word2token = pickle.load(f)

with open('pickle/transformer.pickle', 'rb') as f:
    transformer = pickle.load(f)

with open('pickle/scaler.pickle', 'rb') as f:
    scaler = pickle.load(f)

with open('pickle/model.pickle', 'rb') as f:
    model = pickle.load(f)

# app contents
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # get text
    text = request.form['text']

    # tokenize
    tokens = map(lambda w: word2token.get(w), text.split())
    
    # # count occurences
    X = np.zeros(len(word2token))
    print(X)
    for token in tokens:
        if token:
            X[token] += 1

    # transform to tf-idf
    X = transformer.transform(X.reshape(1, -1))

    # standardize
    X = scaler.transform(X.todense())
    print(np.max(X))

    # predict
    y = model.predict(X)

    # form output
    prediction = f'Predicted date: {int(y)}'

    return render_template('index.html', prediction_text=prediction)

# entry point
if __name__ == '__main__':
    app.run(debug=True)
