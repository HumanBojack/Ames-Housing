from flask import render_template, request, Blueprint, redirect, url_for, flash
from flask_login import login_required, current_user

from app.models import Prediction, User

predictions = Blueprint("predictions", __name__)

@login_required
@predictions.route("/")
def index():
    return render_template("predictions.html", predictions=current_user.predictions)

@login_required
@predictions.route("/<int:id>") # TODO: use methods=["DELETE"])
def delete_prediction(id):
    prediction = Prediction.query.filter_by(id=id).first()
    if prediction:
        prediction.delete_from_db()
        flash(f"Successfully deleted prediction {id}", "info")
    else:
        flash(f"Cannot find prediction with id {id}", "error")

    return redirect(url_for('predictions.index'))