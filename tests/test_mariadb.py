import pytest
from main import *

def test_index():
    response = app.test_client().get('/')
    assert response.status_code == 400
    