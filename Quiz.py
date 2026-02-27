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

def score_(scores):
    return {
        "total": total_score(scores),
        "average": average_score(scores),
        "highest": highest_score(scores),
        "lowest": lowest_score(scores)
    }


if __name__ == "__main__":
    print("Quiz Scorer")
    print("Enter scores separated by space:")

    user_input = input("|> ")
    scores = list(map(int, user_input.split()))

    result = score_(scores)
    print("\nResults:")
    print("Your Total Score:", result["total"])
    print("Your Average Score:", result["average"])
    print("Your Highest Score:", result["highest"])
    print("Your Lowest Score:", result["lowest"])