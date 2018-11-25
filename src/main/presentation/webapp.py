from flask import Flask, render_template, url_for
from flask import request
import datetime
from src.main.data.elasticsearch.Config import Config
from src.main.data.elasticsearch.QuestionIndex import QuestionIndex
from src.main.data.elasticsearch.model.CosineSearchModel import CosineSearchModel
from src.main.data.elasticsearch.model.RecSysSearchModel import RecSysSearchModel
from flask_cors import CORS, cross_origin

app = Flask(__name__)
config = Config("localhost", "9200")
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

index = QuestionIndex(config, RecSysSearchModel())

@app.route("/search/<page>")
def search(page: str):
    page = int(page) * 10
    query: str = request.args.get('query', None)
    if query:
        hits, results = index.query_info(query, page, page + 10)
        print(query)
        return render_template('search.html', query=results, search=query, hit_count=hits, page=page)


@app.route("/")
@cross_origin()
def home():
    url_for('static', filename='static/icon.png')
    return render_template('home.html')


@app.route("/question/<id>")
def question(id : str):
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

    def date(d):
        return "{:%d %b %Y}".format(datetime.datetime.strptime(d, "%Y-%m-%dT%H:%M:%S.%fZ"))

    def tags(t):
        t = re.sub('<', '', t).split('>')[:-1]
        res = ""
        if len(t) > 0:
            res = t[0]
            t = t[1:]
            for i in t:
                res += ", " + i
        return res

    def solved(question_a):
        status = "Solved"
        if question_a['accepted_answer_id'] is None:
            status = ""
        return status

    return dict(filter2=filter2, date=date, tags=tags, solved=solved)



app.run(port=3000, host= '0.0.0.0')
