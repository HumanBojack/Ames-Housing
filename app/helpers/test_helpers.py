from .predict import *
from werkzeug.datastructures import ImmutableMultiDict

def test_form_parser():
    test_data = [
        ImmutableMultiDict([('BsmtFin SF 1', 192.0), ('Gr Liv Area', 888), ('House Area', 2048.0), ('Neighborhood', 'NAmes'), ('Fireplaces', 0), ('Overall Qual', 5), ('Bsmt Qual', 'TA'), ('Kitchen Qual', 'TA'), ('Year Built', 1961), ('Year Remod/Add', 1961)]),

        ImmutableMultiDict([('BsmtFin SF 1', 0.0), ('Gr Liv Area', 1710), ('House Area', 2789.0), ('Neighborhood', 'OldTown'), ('Fireplaces', 0), ('Overall Qual', 7), ('Bsmt Qual', 'TA'), ('Kitchen Qual', 'TA'), ('Year Built', 1921), ('Year Remod/Add', 1950)]),

        ImmutableMultiDict([('BsmtFin SF 1', 0.0), ('Gr Liv Area', 1710), ('House Area', 2789.0), ('Neighborhood', 'OldTown'), ('Fireplaces', 0), ('Overall Qual', 7), ('Bsmt Qual', 'TA'), ('Kitchen Qual', 'TA'), ('Year Built', 1921), ('Year Remod/Add', 1950)]),

        ImmutableMultiDict([('BsmtFin SF 1', 846.0), ('Gr Liv Area', 1342), ('House Area', 3269.0), ('Neighborhood', 'NridgHt'), ('Fireplaces', 1), ('Overall Qual', 8), ('Bsmt Qual', 'Gd'), ('Kitchen Qual', 'Gd'), ('Year Built', 2006), ('Year Remod/Add', 2007)]),

        ImmutableMultiDict([('BsmtFin SF 1', 0.0), ('Gr Liv Area', 1513), ('House Area', 2656.0), ('Neighborhood', 'BrkSide'), ('Fireplaces', 0), ('Overall Qual', 5), ('Bsmt Qual', 'None'), ('Kitchen Qual', 'TA'), ('Year Built', 1920), ('Year Remod/Add', 2004)])
    ]
    for form in test_data:
        parsed_form = parse_predict_form(form)
        for col in ['Neighborhood', 'Kitchen Qual']:
            assert type(parsed_form[col]) is str

        for col in ['BsmtFin SF 1', 'Gr Liv Area', 'House Area', 'Fireplaces', 'Overall Qual', 'Year Built', 'Year Remod/Add']:
            assert type(parsed_form[col]) is int

        for col in ['Bsmt Qual']:
            assert (parsed_form[col] is None) | (type(parsed_form[col]) is str)