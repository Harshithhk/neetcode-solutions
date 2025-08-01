def twoSum(nums, target):
    nums_dict = {}

    for index, num in enumerate(nums):

        diff = target - num
        if diff in nums_dict:
            return [nums_dict[diff], index]
        if num not in nums_dict:
            nums_dict[num] = index

    return []


print(twoSum([2, 7, 11, 15], 26))
