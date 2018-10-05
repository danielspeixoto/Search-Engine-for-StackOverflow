from flask import Flask, render_template
from flask import request

from src.main.data.elasticsearch.Config import Config
from src.main.data.elasticsearch.QuestionIndex import QuestionIndex

app = Flask(__name__)
config = Config("localhost", "9200")


@app.route("/")
def home():
    query: str = request.args.get('query', None)
    if query:
        index = QuestionIndex(config)
        query = index.query(query)
    return render_template('search.html', query=query)


@app.route("/question/<id>")
def question(id : str):
    index = QuestionIndex(config)
    question = None
    for i in index.id(id):
        question = i
    return render_template('question.html', question=question)


app.run(port=3000)