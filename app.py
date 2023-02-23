from dotenv import dotenv_values
import openai
from flask import Flask
from flask import request,abort,render_template
import codex_completion as codex

secrets = dotenv_values(".env")
openai.api_key = secrets.get('OPENAI_API_KEY')

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        try:
            response = codex.execute_completion(prompt=request.form['input'])
        except:
            abort(401)
        else:
            return response,200
