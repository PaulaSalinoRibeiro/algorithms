def aux(arr):
    if not arr or len(arr) < 1:
        return False

    arr.sort()
    if type(arr[-1]) is not int:
        return False

    return arr


def find_duplicate(nums):
    if aux(nums):
        for index, number in enumerate(nums[:-1]):
            if number < 0:
                return False
            if number == nums[index + 1]:
                return number

    return False
