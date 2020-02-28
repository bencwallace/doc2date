import pickle

from flask import Flask, render_template, request, url_for

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import StandardScaler


app = Flask(__name__)

# model components
with open('pickle/tokenizer.pickle', 'rb') as f:
    tokenizer = pickle.load(f)

# convert SpaCy tokenizer to a function str -> list of str
def tok(text):
    return [str(t) for t in tokenizer(text)]

with open('pickle/word2token.pickle', 'rb') as f:
    word2token = pickle.load(f)

# build vectorizer from vocabulary and tokenizer
vectorizer = CountVectorizer(vocabulary=word2token, tokenizer=tok)

with open('pickle/transformer.pickle', 'rb') as f:
    transformer = pickle.load(f)

with open('pickle/scaler.pickle', 'rb') as f:
    scaler = pickle.load(f)

with open('pickle/predictor.pickle', 'rb') as f:
    predictor = pickle.load(f)

# app contents
@app.route('/')
def home():
    with open('static/moby-dick.txt', 'r') as f:
        text = f.read()
    return render_template('index.html', text=text)

@app.route('/predict', methods=['POST'])
def predict():
    # get text
    text = request.form['text']

    # count occurences
    X = vectorizer.transform([text])

    # transform to tf-idf
    X = transformer.transform(X)

    # standardize
    X = scaler.transform(X.todense())

    # predict
    y = predictor.predict(X)

    return render_template('index.html', prediction=int(y))

# entry point
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
