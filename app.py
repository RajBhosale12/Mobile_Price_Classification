from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# app = Flask(__name__)
app = Flask(__name__, template_folder='templates')



@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/home', methods=['POST','GET'])
def home():
    int_f=[float(x) for x in request.form.values()]
    final=[np.array(int_f)]
    # print(final)
    prediction=model.predict(final)
    output=prediction[0]
    if(output==0):
        return render_template('index.html',pred=f'output={output} \n Mobile is classified into low price range ')
    elif(output==1):
        return render_template('index.html',pred=f'output={output} \n Mobile is classified into medium price range ')
    elif(output==2):
        return render_template('index.html',pred=f'output={output} \n Mobile is classified into high price range ')
    else:
        return render_template('index.html',pred=f'output={output} \n Mobile is classified into very high price range ')


if __name__ == "__main__":
    print("Starting Python Flask Server For Mobile Price Classification...")
    app.run(debug=True)

