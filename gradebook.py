def letterGrade(score):
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
    return (score > 59)

def average(scores):
    if len(scores) == 0:
        return 0
    return sum(scores)/len(scores)

def curved_score(score, bonus):
    pass

