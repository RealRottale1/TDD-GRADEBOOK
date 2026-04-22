def letterGrade(score):
    if not (type(score) is int):
        raise TypeError
    if (score > 89):
        return "A"
    elif (score > 79):
        return "B"
    elif (score > 69):
        return "C"
    elif (score > 59):
        return "D"
    return "F"

def isPassing(score):
    if not (type(score) is int):
        raise TypeError
    return (score > 59)

def average(scores):
    if not (type(scores) is list):
        raise TypeError
    if not all(type(scores) is int):
        raise TypeError
    if len(scores) == 0:
        return 0
    return sum(scores)/len(scores)

def curved_score(score, bonus):
    newScore = score + bonus
    if newScore < 100:
        return newScore
    else:
        return 100

