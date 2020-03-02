import pickle

from flask import Flask, render_template, request, url_for

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer, StandardScaler

app = Flask(__name__)

# load model components
with open('pickle/tokenizer.pickle', 'rb') as f:
    tokenizer = pickle.load(f)

with open('pickle/word2token.pickle', 'rb') as f:
    word2token = pickle.load(f)

with open('pickle/transformer.pickle', 'rb') as f:
    transformer = pickle.load(f)

with open('pickle/scaler.pickle', 'rb') as f:
    scaler = pickle.load(f)

with open('pickle/predictor.pickle', 'rb') as f:
    predictor = pickle.load(f)

# build pipeline components

tolist = FunctionTransformer(lambda x: [x])

todense = FunctionTransformer(lambda x: x.todense())

def tok(text):
    return [str(t) for t in tokenizer(text)]

cv = CountVectorizer(vocabulary=word2token, tokenizer=tok)

# build prediction pipeline
pipe = Pipeline([('tolist', tolist),
                 ('count', cv),
                 ('tfidf', transformer),
                 ('densify', todense),
                 ('scale', scaler),
                 ('predict', predictor)])

# app contents
@app.route('/')
def home():
    with open('static/moby-dick.txt', 'r') as f:
        text = f.read()
    return render_template('index.html', text=text)

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['text']
    y = int(pipe.predict(text)[0])
    return render_template('index.html', prediction=y, text=text)

# entry point
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
