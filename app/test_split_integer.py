from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    result_1 = split_integer(8, 1)
    assert sum(result_1) == 8
    assert len(result_1) == 1

    result_2 = split_integer(6, 2)
    assert sum(result_2) == 6
    assert len(result_2) == 2


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(9, 3) == [3, 3, 3]
    assert split_integer(12, 6) == [2, 2, 2, 2, 2, 2]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(1, 1) == [1]
    assert split_integer(33, 1) == [33]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result_1 = split_integer(17, 4)
    assert result_1 == sorted([4, 4, 4, 5])
    assert max(result_1) - min(result_1) <= 1

    result_2 = split_integer(32, 6)
    assert result_2 == sorted([5, 5, 5, 5, 6, 6])
    assert max(result_2) - min(result_2) <= 1


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(1, 3) == [0, 0, 1]
    assert split_integer(2, 5) == [0, 0, 0, 1, 1]
