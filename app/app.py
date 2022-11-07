from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import joblib

NEIGHBORHOODS = ['NAmes', 'Gilbert', 'StoneBr', 'NWAmes', 'Somerst', 'BrDale',
       'NPkVill', 'NridgHt', 'Blmngtn', 'NoRidge', 'SawyerW', 'Sawyer',
       'Greens', 'BrkSide', 'OldTown', 'IDOTRR', 'ClearCr', 'SWISU',
       'Edwards', 'CollgCr', 'Crawfor', 'Blueste', 'Mitchel', 'Timber',
       'MeadowV', 'Veenker', 'GrnHill', 'Landmrk']

app = Flask(__name__)
model = joblib.load(open('model.joblib', 'rb'))


@app.route('/')
def index():
    return render_template('index.html', neighborhoods=NEIGHBORHOODS)


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    X_predict = {}
    for var in ['BsmtFin SF 1', 'Gr Liv Area', 'House Area', 'Neighborhood', 'Fireplaces', 'Overall Qual', 'Bsmt Qual', 'Kitchen Qual', 'Year Built', 'Year Remod/Add']:
        # TODO: throw error if a var doesn't is equal to ''
        if var in ["Neighborhood", "Bsmt Qual", "Kitchen Qual"]:
            X_predict[var]= request.form[var]
        else:
            X_predict[var]= int(request.form[var])

    pred = model.predict(pd.DataFrame(X_predict, index=[0]))

    return render_template('index.html', data=int(pred), neighborhoods=NEIGHBORHOODS)


if __name__ == '__main__':
    app.run(debug=True)
