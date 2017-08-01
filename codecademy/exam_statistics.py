def grades_sum(scores):
    assert isinstance(scores, list), "Passed the wrong data type"
    j = 0
    for i in scores:
        assert isinstance(i, int) and type(i) != bool and i >= 0, "Passed the wrong data type"
        j += i
    return j


def grades_average(scores):
    a = grades_sum(scores)
    return a / float(len(scores))
# END grades_average
