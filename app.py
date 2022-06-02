
import os
from flask import Flask,render_template,request,send_from_directory
import tensorflow as tf
import numpy as np





app = Flask(__name__)



@app.route('/')
def home():
    return render_template("/home.html")

@app.route('/home.html')
def homepage():
    return render_template("/home.html")



    
if __name__ == '__main__':
    app.run(debug=True)