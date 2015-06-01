import os
import random
from flask import Flask, render_template

app = Flask(__name__)

choices = ['1.html', '2.html']

@app.route('/')
def hello():
        choice = random.choice(choices)
        return render_template(choice) 
