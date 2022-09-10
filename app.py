from flask import Flask, render_template, request
from joblib import load

app = Flask(__name__)

model = load('floods.save')
sc = load('transform.save')

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/predict')
def index():
    return render_template("index.html")

@app.route('/data_predict', methods=['POST'])
def predict():
    cc = request.form['cc']
    ar = request.form['ar']
    jfr = request.form['jfr']
    mmr = request.form['mmr']
    jsr = request.form['jsr']

    data = [[float(cc),float(ar),float(jfr),float(mmr),float(jsr)]]
    prediction = model.predict(sc.transform(data))
    output = prediction[0]
    if(output==0):
        return render_template('noChance.html', prediction='No possibility of severe flood')
    else:
        return render_template('chance.html', prediction='possibility of severe flood')

if __name__ == '__main__':
    app.run(debug=True)
