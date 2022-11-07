import os
import pandas as pd
import joblib

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

from helpers import parse_predict_form

NEIGHBORHOODS = ['NAmes', 'Gilbert', 'StoneBr', 'NWAmes', 'Somerst', 'BrDale',
       'NPkVill', 'NridgHt', 'Blmngtn', 'NoRidge', 'SawyerW', 'Sawyer',
       'Greens', 'BrkSide', 'OldTown', 'IDOTRR', 'ClearCr', 'SWISU',
       'Edwards', 'CollgCr', 'Crawfor', 'Blueste', 'Mitchel', 'Timber',
       'MeadowV', 'Veenker', 'GrnHill', 'Landmrk']

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
db = SQLAlchemy(app)

model = joblib.load(open('model.joblib', 'rb'))


@app.route('/')
def index():
    return render_template('index.html', neighborhoods=NEIGHBORHOODS)


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    pred = 0
    if request.form:
        X_predict = parse_predict_form(request.form)
        pred = model.predict(pd.DataFrame(X_predict, index=[0]))
    return render_template('index.html', data=int(pred), neighborhoods=NEIGHBORHOODS)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.environ.get("PORT", 80), debug=True)
