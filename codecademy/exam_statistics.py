def grades_sum(scores):
    assert isinstance(scores, list), "Passed the wrong data type"
    j = 0
    for i in scores:
        assert type(i) in (int, float) and i >= 0, "Passed the wrong data type"
        j += i
    return j


def grades_average(scores):
    a = grades_sum(scores)
    return a / float(len(scores))
# END grades_average


def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
    return round(variance / float(len(scores)), 2)


# 4 7 9 nicolas13sochi part
# the exercises ## 4,7 are duplicated with Sanya's task above
# 4 The sum of scores

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]


def grades_sum_4(scores):
    assert isinstance(scores, list), "Passed the wrong data type"
    total = 0
    for score in scores:
        assert type(score) in (int, float) and score >= 0, "Passed the wrong data type"
        total += score
    return total


# 7 The Variance


def grades_variance_7(scores):
    assert isinstance(scores, list), "Passed the wrong data type"
    average = grades_average(scores)
    variance = 0
    for score in scores:
        assert type(score) in (int, float) and score >= 0, "Passed the wrong data type"
        variance += (average - score) ** 2
    return round(variance/len(scores), 2)


# 9 Review
def grades_std_deviation(scores):
    assert isinstance(scores, list), "Passed the wrong data type"
    variance = grades_variance(scores)
    return round(variance ** 0.5, 2)

print(grades_std_deviation(grades))
