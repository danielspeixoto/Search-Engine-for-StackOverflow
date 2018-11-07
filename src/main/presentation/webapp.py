from flask import Flask, render_template, url_for
from flask import request

from src.main.data.elasticsearch.Config import Config
from src.main.data.elasticsearch.QuestionIndex import QuestionIndex
from src.main.data.elasticsearch.model.CosineSearchModel import CosineSearchModel

app = Flask(__name__)
config = Config("localhost", "9200")


@app.route("/search")
def search():
    query: str = request.args.get('query', None)
    if query:
        index = QuestionIndex(config, CosineSearchModel())
        results = index.query(query, 0, 10)
        print(query)
    return render_template('search.html', query=results, search=query)


@app.route("/")
def home():
    url_for('static', filename='static/icon.png')
    return render_template('home.html')


@app.route("/question/<id>")
def question(id : str):
    index = QuestionIndex(config, CosineSearchModel())
    question = None
    print(question)
    for i in index.id(id):
        question = i
    return render_template('question.html', question=question)


import re

@app.context_processor
def processor():
    def filter2(word):
        word = re.sub("<code>[^<]*</code>", '', word)
        word = re.sub('<[^<]+?>', '', word)
        word = re.sub("&#xA;", '', word)
        size = len(word)
        word = word[:min(size, 500)]
        if size > 500:
            word += '...'
        return word
    return dict(filter2=filter2)



app.run(port=3000)
