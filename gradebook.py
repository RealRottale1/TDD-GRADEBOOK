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
    return sum(scores)/len(scores)

def curved_score(score, bonus):
    pass

