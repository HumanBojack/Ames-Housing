import numpy as np

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