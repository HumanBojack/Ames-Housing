from . import parse_predict_form, form_inputs

def test_form_parser(form_inputs):
    for form_input in form_inputs:
        parsed_form = parse_predict_form(form_input)
        for col in ['Neighborhood', 'Kitchen Qual']:
            assert type(parsed_form[col]) is str

        for col in ['BsmtFin SF 1', 'Gr Liv Area', 'House Area', 'Fireplaces', 'Overall Qual', 'Year Built', 'Year Remod/Add']:
            assert type(parsed_form[col]) is int

        for col in ['Bsmt Qual']:
            assert (parsed_form[col] is None) | (type(parsed_form[col]) is str)