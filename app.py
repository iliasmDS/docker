
from flask import Flask, render_template_string
import pymongo
from pymongo import MongoClient
import pandas as pd
import matplotlib.pyplot as plt
import os
import matplotlib

matplotlib.use('Agg')

app = Flask(__name__)

def get_db():

    client = MongoClient(

                         host='container_as_db',
                         port=27017, 
                         username='root', 
                         password='pass',
                         authSource="admin"
                        
                        )
    
    db = client["mongodb"]

    return db

def plot_as_html():

    db = get_db()

    data = db.data.find({})

    data = pd.DataFrame(data)

    plt.scatter(x = data['x'], y = data['y'])

    os.makedirs(os.path.join('static', 'images'), exist_ok=True)

    plt.savefig(os.path.join('static', 'images', 'plot.png')) 

@app.route('/')

def plot():

    plot_as_html()

    return render_template_string("""
        <h3> OUTPUT: </h3>
        <img src="{{ url_for('static', filename='images/plot.png') }}" class="image" />
    """)

if __name__=='__main__':

    app.run(host="0.0.0.0", port=5000)