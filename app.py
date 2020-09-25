import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from loaddata import normalise_data, ir_trim
import pandas as pd
from flask import Flask, jsonify, request


vectorizer, model = pickle.load(open('spam_model.pkl','rb'))

app = Flask(__name__)

@app.route('/', methods=['POST'])

def predict():

    data = request.get_json(force=True)

    x = [data['text']]
    x = normalise_data(x)
    counts = vectorizer.transform(x)
    result = model.predict(counts)

    output = {'results': int(result[0])}

    # return data
    return jsonify(results=output)


if __name__ == '__main__':
    app.run(port = 5000, debug=True)