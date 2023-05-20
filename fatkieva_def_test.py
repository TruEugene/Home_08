import unittest
from fatkieva_def import count_passengers_by_sex_and_status


class TestCountPassengersBySexAndStatus(unittest.TestCase):

    def test_count_passengers_by_male_and_survived(self):
        assert count_passengers_by_sex_and_status('male', 1) == 109

    def test_count_passengers_by_male_and_not_survived(self):
        assert count_passengers_by_sex_and_status('male', 0) == 468

    def test_count_passengers_by_female_and_survived(self):
        assert count_passengers_by_sex_and_status('female', 1) == 233

    def test_count_passengers_by_female_and_not_survived(self):
        assert count_passengers_by_sex_and_status('female', 0) == 81

    def test_total_passengers_by_male(self):
        assert count_passengers_by_sex_and_status('male', 1) + \
               count_passengers_by_sex_and_status('male', 0) == 577

    def test_total_passengers_by_female(self):
        assert count_passengers_by_sex_and_status('female', 1) + \
               count_passengers_by_sex_and_status('female', 0) == 314
