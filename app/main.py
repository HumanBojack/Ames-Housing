import pandas as pd
import joblib

from flask import render_template, request, Blueprint, redirect, url_for, flash
from flask_login import login_required, current_user

from app.helpers import parse_predict_form, save_prediction

NEIGHBORHOODS = ['NAmes', 'Gilbert', 'StoneBr', 'NWAmes', 'Somerst', 'BrDale',
       'NPkVill', 'NridgHt', 'Blmngtn', 'NoRidge', 'SawyerW', 'Sawyer',
       'Greens', 'BrkSide', 'OldTown', 'IDOTRR', 'ClearCr', 'SWISU',
       'Edwards', 'CollgCr', 'Crawfor', 'Blueste', 'Mitchel', 'Timber',
       'MeadowV', 'Veenker', 'GrnHill', 'Landmrk']

main = Blueprint("main", __name__)
model = joblib.load(open('app/model.joblib', 'rb'))

@main.route('/')
@login_required
def index():
    return redirect(url_for('main.predict'))


@main.route('/predict', methods=['GET', 'POST'])
@login_required
def predict():
    pred = 0
    if request.form:
        X_predict = parse_predict_form(request.form)
        pred = int(model.predict(pd.DataFrame(X_predict, index=[0])))
        try:
            save_prediction(X_predict, pred, current_user.email)
            status = 200
        except:
            flash("Error while saving to database", "error")
            status = 500

    return render_template('predict.html', data=pred, neighborhoods=NEIGHBORHOODS), status
