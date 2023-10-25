import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from joblib import load

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

# Load the models
tfidf = load('vectorizer.joblib')
model = load('model.joblib')

import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_sms = flask.request.form['input_text']
    transformed_sms = transform_text(input_sms)
    vector_input = tfidf.transform([transformed_sms])
    result = model.predict(vector_input)[0]
    if result == 1:
        prediction = "Spam"
    else:
        prediction = "Not Spam"
    return flask.jsonify({'result': prediction})

if __name__ == '__main__':
    app.run(debug=True)


