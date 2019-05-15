from flask import Flask, render_template, request, redirect, url_for
from textblob import TextBlob

app=Flask(__name__,template_folder='template')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/',methods = ['POST', 'GET'])

def result():
    if request.method == 'POST':
        result = request.form
        sentiment = TextBlob(str(result)).sentiment.polarity
        return render_template('result.html',sentiment= sentiment, result = result)

    return "None"

if __name__ == '__main__' :
    app.run(debug = True)
