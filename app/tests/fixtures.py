import pytest
import uuid
from werkzeug.datastructures import ImmutableMultiDict

from . import create_app

@pytest.fixture
def form_inputs():
    return [
        ImmutableMultiDict([('BsmtFin SF 1', 192), ('Gr Liv Area', 888), ('House Area', 2048), ('Neighborhood', 'NAmes'), ('Fireplaces', 0), ('Overall Qual', 5), ('Bsmt Qual', 'TA'), ('Kitchen Qual', 'TA'), ('Year Built', 1961), ('Year Remod/Add', 1961)]),
        ImmutableMultiDict([('BsmtFin SF 1', 0.0), ('Gr Liv Area', 1710), ('House Area', 2789.0), ('Neighborhood', 'OldTown'), ('Fireplaces', 0), ('Overall Qual', 7), ('Bsmt Qual', 'TA'), ('Kitchen Qual', 'TA'), ('Year Built', 1921), ('Year Remod/Add', 1950)]),
        ImmutableMultiDict([('BsmtFin SF 1', 0.0), ('Gr Liv Area', 1710), ('House Area', 2789.0), ('Neighborhood', 'OldTown'), ('Fireplaces', 0), ('Overall Qual', 7), ('Bsmt Qual', 'TA'), ('Kitchen Qual', 'TA'), ('Year Built', 1921), ('Year Remod/Add', 1950)]),
        ImmutableMultiDict([('BsmtFin SF 1', 846.0), ('Gr Liv Area', 1342), ('House Area', 3269.0), ('Neighborhood', 'NridgHt'), ('Fireplaces', 1), ('Overall Qual', 8), ('Bsmt Qual', 'Gd'), ('Kitchen Qual', 'Gd'), ('Year Built', 2006), ('Year Remod/Add', 2007)]),
        ImmutableMultiDict([('BsmtFin SF 1', 0.0), ('Gr Liv Area', 1513), ('House Area', 2656.0), ('Neighborhood', 'BrkSide'), ('Fireplaces', 0), ('Overall Qual', 5), ('Bsmt Qual', 'None'), ('Kitchen Qual', 'TA'), ('Year Built', 1920), ('Year Remod/Add', 2004)])
    ]


@pytest.fixture(scope='module')
def client():
    app = create_app()
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://db_login@localhost/app_db"
    with app.test_client() as client:
        yield client


@pytest.fixture(scope='module')
def user():
    return {
        "email": f"{uuid.uuid4()}@gmail.com",
        "password": str(uuid.uuid4())
    }