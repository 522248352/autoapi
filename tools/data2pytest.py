import pytest


def dataToPytest(datas):
    data = []
    for i in datas:
        data.append(pytest.param(*i[:-1], marks=i[-1]))
    return data