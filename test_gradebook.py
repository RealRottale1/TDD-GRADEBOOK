from gradebook import letterGrade

@pytest.mark.parametrize("grade, expected", [
    (90, "A"),
    (80, "B"),
    (70, "C"),
    (60, "D"),
    (50, "F")
])

def test_ticket_tiers(grade, expected):
    assert letterGrade(grade) == expected