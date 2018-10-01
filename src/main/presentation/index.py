from flask import Flask, render_template
from flask import request

from src.main.data.elasticsearch.Config import Config
from src.main.data.elasticsearch.QuestionIndex import QuestionIndex

app = Flask(__name__)


@app.route("/")
def search():
    query: str = request.args.get('query', None)
    if query:
        print("Query exists")
        index = QuestionIndex(Config("localhost", "9200")._connection)
        query = index.query(query)
    return render_template('search.html', query=query)


app.run(port=3000)