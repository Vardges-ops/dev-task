# Solution 1

from typing import Union


def calc_target_sum(nums: list[int], target: int) -> Union[list[int], bool]:
    """
    This function finds two distinct elements in a sorted array of integers such that their sum equals a predetermined target value.
    :param nums: A sorted list of integers
    :param target: The target sum value.
    :return: Indices of the two elements whose sum equals the target value, incremented by one.
             If no such pair exists, an empty list is returned.
    """
    start: int = 0
    end: int = len(nums)-1

    while start < end:
        curr_val = nums[start] + nums[end]
        if curr_val == target:
            return [start+1, end+1]
        elif curr_val < target:
            start += 1
        else:
            end -= 1
    return False


# Solution 2

def calc_target_sum_2(nums: list[int], target: int) -> Union[list[int], bool]:
    """
    This function finds two numbers in a list that sum up to a given target value.
    :param nums: A sorted list of integers
    :param target: The target sum value.
    :return: Indices of the two elements whose sum equals the target value, incremented by one.
             If no such pair exists, an empty list is returned.
    """
    num_indices = {}
    for num_id, num in enumerate(nums):
        remainder = target - num
        if remainder in num_indices:
            return [num_indices[remainder] + 1, num_id + 1]
        num_indices[num] = num_id
    return False


if __name__ == "__main__":

    print(calc_target_sum([2, 7, 11, 15], 9))
    print(calc_target_sum([2, 3, 4], 6))
    print(calc_target_sum([-1, 0], -1))

    print(calc_target_sum_2([2, 7, 11, 15], 9))
    print(calc_target_sum_2([2, 3, 4], 6))
    print(calc_target_sum_2([-1, 0], -1))
