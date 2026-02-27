def total_score(scores):
    return sum(scores)


def average_score(scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)


def highest_score(scores):
    if len(scores) == 0:
        return None
    return max(scores)


def lowest_score(scores):
    if len(scores) == 0:
        return None
    return min(scores)