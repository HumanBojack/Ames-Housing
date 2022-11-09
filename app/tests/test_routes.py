from . import client, user, form_inputs

def test_register(client, user):
    # Test that we're redirected to the login page after a successful register
    response = client.post('/register', data=user, follow_redirects=True)
    assert response.request.path == "/login"

def test_login(client, user):
    # Test that we're redirected to the /predict page after logging in
    response = client.post('/login', data=user, follow_redirects=True)
    assert response.request.path == "/predict"

def test_access(client):
    # Test that a logged user can access some ressources
    response = client.get('/predict', follow_redirects=True)
    assert response.request.path == "/predict"

    response = client.get('/predictions', follow_redirects=True)
    assert response.request.path == "/predictions/"

def test_prediction(client, form_inputs):
    # Test that a prediction can be done when a user is logged
    form = dict(form_inputs[0])
    response = client.post('/predict', data=form, follow_redirects=True)
    assert response.request.path == '/predict'
    assert response.status_code == 200

def test_history(client, form_inputs):
    # Test if the inserted prediction is in the history
    form = dict(form_inputs[0])
    response = client.get('/predictions', follow_redirects=True)
    assert response.request.path == '/predictions/'

    # Check that all the values passed in the /predict method are present here
    for value in form.values():
        assert str(value) in str(response.data)