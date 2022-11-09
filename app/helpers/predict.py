from app.models import Prediction, User

def parse_predict_form(form):
    X_predict = {}
    for var in ['BsmtFin SF 1', 'Gr Liv Area', 'House Area', 'Neighborhood', 'Fireplaces', 'Overall Qual', 'Bsmt Qual', 'Kitchen Qual', 'Year Built', 'Year Remod/Add']:
        # TODO: throw error if a var doesn't is equal to ''
        if form[var] == "None":
            X_predict[var] = None
        elif var in ["Neighborhood", "Bsmt Qual", "Kitchen Qual"]:
            X_predict[var]= form[var]
        else:
            X_predict[var]= int(form[var])

    return X_predict


def save_prediction(inputs, output, user_email):
    Prediction(
        user_id=user_email,
        year_remod_add=inputs["Year Remod/Add"],
        overall_qual=inputs["Overall Qual"],
        bsmtfin_sf_1=inputs["BsmtFin SF 1"],
        gr_liv_area=inputs["Gr Liv Area"],
        house_area=inputs["House Area"],
        fireplaces=inputs["Fireplaces"],
        year_built=inputs["Year Built"],
        neighborhood=inputs["Neighborhood"],
        kitchen_qual=inputs["Kitchen Qual"],
        bsmt_qual=inputs["Bsmt Qual"],
        predicted_price=output
    ).save_to_db()