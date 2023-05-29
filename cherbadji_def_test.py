import pandas as pd


def test_count_men_women_in_selected_survived():
    grid = {'Survived': [0, 1, 0, 1, 0, 1, 0], 'Sex': ['female', 'male', 'female', 'male', 'female', 'female', 'male']}
    test_data = pd.DataFrame(grid)
    assert test_count_men_women_in_selected_survived(test_data, 1) == (1, 0)


def test_count_men_women_in_selected_survived_if_sex_none():
    grid = {'survived': [0, 1, 0, 0, 0, 1, 1], 'Sex': ['female', 'male', None, 'male', 'female', 'female', 'male']}
    test_data = pd.DataFrame(grid)
    assert test_count_men_women_in_selected_survived(test_data, 1) == (1, 0)


def test_count_men_women_in_selected_survived_if_survived_none():
    grid = {'survived': [0, 1, None, 0, 0, 1, 1],
            'Sex': ['female', 'male', 'female', 'male', 'female', 'female', 'male']}
    test_data = pd.DataFrame(grid)
    assert test_count_men_women_in_selected_survived(test_data, 1) == (1, 0)
