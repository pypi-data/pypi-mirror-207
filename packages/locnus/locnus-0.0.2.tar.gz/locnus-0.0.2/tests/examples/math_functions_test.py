# test_math_functions.py
from .math_functions import pizza_volume


def test_pizza_volume_half_stack():
    z = 5  # radius (z) = 5 units
    a = 2  # height (a) = 2 units
    num_pizzas = 3  # Number of pizzas in the stack
    cut_in_half = True  # Stack is cut in half

    single_pizza_volume = 157.07963267948966  # Precomputed volume of a single pizza using the formula
    expected_half_stack_volume = single_pizza_volume * num_pizzas * 0.5

    assert round(pizza_volume(z, a, num_pizzas, cut_in_half), 8) == round(
        expected_half_stack_volume, 8
    ), f"Arr, with a radius of {z}, a height of {a}, and {num_pizzas} pizzas cut in half, the half pizza stack's volume should be {expected_half_stack_volume} cubic units!"  # noqa
