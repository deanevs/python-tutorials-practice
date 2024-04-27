import pytest


@pytest.fixture
def example_people_data():
    people = [
        {
            "given_name": "Alfonso",
            "family_name": "Ruiz",
            "title": "Software Engineer"
        },
        {
            "given_name": "Dean",
            "family_name": "Evans",
            "title": "Staff Software Engineer"
        },
    ]
    return people
