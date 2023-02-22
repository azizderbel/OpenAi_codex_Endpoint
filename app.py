from dotenv import dotenv_values
import openai
from flask import Flask
from flask import request,render_template

secrets = dotenv_values(".env")
openai.api_key = secrets.get('OPENAI_API_KEY')

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        pass
