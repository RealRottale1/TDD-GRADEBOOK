import pytest
from gradebook import letterGrade, isPassing, average, curved_score

@pytest.mark.parametrize("grade, expected", [
    (90, "A"),
    (80, "B"),
    (70, "C"),
    (60, "D"),
    (50, "F")
])

def test_letterGrade(grade, expected):
    assert letterGrade(grade) == expected

def test_letterGrade_invalidType():
    with pytest.raises(TypeError):
        letterGrade("92")

@pytest.mark.parametrize("grade, expected", [
    (90, True),
    (60, True),
    (50, False)
])

def test_isPassing(grade, expected):
    assert isPassing(grade) == expected

def test_isPassing_invalidType():
    with pytest.raises(TypeError):
        isPassing("92")

@pytest.mark.parametrize("grades, expected", [
    ([90, 90, 90], 90),
    ([100, 50], 75),
    ([], 0),
])

def test_average(grades, expected):
    assert average(grades) == expected

def test_average_invalidType():
    with pytest.raises(TypeError):
        average(92)

@pytest.mark.parametrize("score, bonus, expected", [
    (90, 11, 100),
    (0, 101, 100),
    (25, 25, 50),
])

def test_curved_score(score, bonus, expected):
    assert curved_score(score, bonus) == expected