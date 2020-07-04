import pytest

from interview_practice_questions.stacks_and_queues.solutions.largest_rectangle import (
    rectangle_area,
    largest_rectangle,
)


# @pytest.mark.parametrize(
#     "set_input, set_output",
#     (
#             #  case 1:
#             (
#                     [1, 2, 3, 4, 5],
#                     5,
#             )
#             # case 2:
#
#     )
# )
# def test_largest_rectangle(
#         set_input,
#         set_output
# ):
#
#     assert True

@pytest.mark.parametrize(
    "set_input, set_output",
    (
            #  case 1:
            (
                    [1, 2, 3, 4, 5],
                    5,
            ),
            # case 2:
            (
                    [3, 4, 5],
                    9,
            ),
            # case 3:
            (
                    [1, 2, 3],
                    3,
            )

    )
)
def test_rectangle_area(
        set_input,
        set_output,
):
    """
    Tests the rectangle_area calculation for the largest rectangle problem.

    :param set_input: (list): Expected input as per tested function.
    :param set_output: (int): Expected output as per tested function, and the calc involved.

    :return: None, asset test.
    """

    result = rectangle_area(set_input)

    assert result == set_output
