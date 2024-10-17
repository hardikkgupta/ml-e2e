import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from utils import validate_input
# from app.utils import validate_input

def test_validate_input_success():
    features = {
        'Pclass': 3,
        'Age': 22.0,
        'SibSp': 1,
        'Parch': 0,
        'Fare': 7.25,
        'Sex_female': 0,
        'Sex_male': 1,
        'Embarked_Q': 0,
        'Embarked_S': 1,
        'FamilySize': 2
    }
    expected = ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare', 'Sex_female', 'Sex_male', 'Embarked_Q', 'Embarked_S', 'FamilySize']
    assert validate_input(features, expected) == [3, 22.0, 1, 0, 7.25, 0, 1, 0, 1, 2]

def test_validate_input_missing_features():
    features = {
        'Pclass': 3,
        'Age': 22.0,
        'SibSp': 1,
        'Fare': 7.25,
        'Sex_female': 0,
        'Sex_male': 1,
        'Embarked_S': 1,
        'FamilySize': 2
    }
    expected = ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare', 'Sex_female', 'Sex_male', 'Embarked_Q', 'Embarked_S', 'FamilySize']
    with pytest.raises(ValueError) as excinfo:
        validate_input(features, expected)
    assert "Missing features: ['Parch', 'Embarked_Q']" in str(excinfo.value)
