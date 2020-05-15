from flask import Flask,render_template,url_for,request, jsonify
import sys
import os
from flask_cors import CORS

sys.path.append(os.path.abspath('src'))
import generate_unconditional_samples

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict')
def predict():
    response = generate_unconditional_samples.sample_model(nsamples=1, model_name='anime')[0]
    rawText = response.split('<|endoftext|>')[1].split('\n')
    rawText = [x for x in rawText if x != '']

    title = rawText[0]
    synopsis = '\n'.join(rawText[1:])

    print('Title', title)
    print('Synopsis', synopsis)
    return jsonify({"title": title, "synopsis": synopsis})

if __name__ == '__main__':
    app.run(debug=True)