from julia_set.julia import calc_pure_python


def test_sum_of_julia_set():
    # This sum is expected for a 1000^2 grid with 300 iterations
    # It ensures that our code evolves exactly as we'd intended
    _, output = calc_pure_python(desired_width=1000, max_iterations=300)
    assert sum(output) == 33219980
