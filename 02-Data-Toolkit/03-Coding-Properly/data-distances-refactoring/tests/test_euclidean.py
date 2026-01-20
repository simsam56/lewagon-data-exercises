from utils.distances import euclidean

def test_euclidean_distance():
    a = (0, 0)
    b = (3, 4)
    result = euclidean(a, b)
    assert result == 5
