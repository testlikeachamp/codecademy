lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}


# Add your function below!
def average(numbers):
    assert isinstance(numbers, (list, tuple)), "{} error type, please enter integer".format(numbers)
    total = sum(numbers)
    total = float(total)
    return round(total / len(numbers), 2)


def get_average(student):
    if type(student) != dict:
        raise TypeError("{} Passed the wrong data type".format(student))
    for key in student:
        if set(student) != set(tyler):
            raise KeyError("{} Please check student key name".format(student))
        homework = average(student["homework"])
        quizzes = average(student["quizzes"])
        tests = average(student["tests"])
        return 0.1 * homework + 0.2 * quizzes + 0.5 * tests


def get_letter_grade(score):
    assert type(score) in (float, int) and 0 <= score <= 100, "{} was not int or float".format(score)
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def get_class_average(students):
    if type(students) != list:
        raise TypeError("{} Passed the wrong data type".format(students))
    result = []
    for student in students:
        result.append(get_average(student))
    return average(result)


