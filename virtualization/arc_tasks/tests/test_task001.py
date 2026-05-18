try:
    from arc_solver import solve
except ImportError:
    from ..arc_solver import solve


def test_task001():
    inp = [[1,0,2],[0,3,0],[4,0,5]]
    out = solve('task001', inp)
    expected = [
        [1,1,1,0,0,0,2,2,2],
        [1,1,1,0,0,0,2,2,2],
        [1,1,1,0,0,0,2,2,2],
        [0,0,0,3,3,3,0,0,0],
        [0,0,0,3,3,3,0,0,0],
        [0,0,0,3,3,3,0,0,0],
        [4,4,4,0,0,0,5,5,5],
        [4,4,4,0,0,0,5,5,5],
        [4,4,4,0,0,0,5,5,5],
    ]
    assert out == expected


if __name__ == '__main__':
    test_task001()
    print('test_task001 passed')
