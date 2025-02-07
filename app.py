import numpy as np
from flask import Flask,request,render_template,jsonify
import pickle

app= Flask(__name__)
model=pickle.load(open("model.pkl","rb"))