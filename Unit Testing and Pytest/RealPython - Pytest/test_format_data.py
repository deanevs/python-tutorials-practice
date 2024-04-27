import pytest
from format_data import format_data_for_display, format_data_for_excel


# @pytest.fixture
# def example_people_data():
#     people = [
#         {
#             "given_name": "Alfonso",
#             "family_name": "Ruiz",
#             "title": "Software Engineer"
#         },
#         {
#             "given_name": "Dean",
#             "family_name": "Evans",
#             "title": "Staff Software Engineer"
#         },
#     ]
#     return people


def test_format_data_for_display(example_people_data):

    assert format_data_for_display(example_people_data) == [
        "Alfonso Ruiz: Software Engineer",
        "Dean Evans: Staff Software Engineer"
    ]


def test_format_data_for_excel(example_people_data):
    assert format_data_for_excel(example_people_data) == """given, family, title, Alfonso, Ruiz, Software Engineer, Dean, Evans, Staff Software Engineer"""
