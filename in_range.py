def in_range(nums, lowest, highest):
    """Print numbers inside range.

    - nums: list of numbers
    - lowest: lowest number to print
    - highest: highest number to print

    For example:

      in_range([10, 20, 30, 40], 15, 30)

    should print:

      20 fits
      30 fits
    """

    # YOUR CODE HERE
    # ! First Attempt
    # nums.sort()
    # first_number = None
    # last_number = None

    # for num in nums:
    #     if num >= lowest:
    #         first_number = num
    #         break

    # for num in nums:
    #     if num >= highest:
    #         last_number = num
    #         break

    # return nums[nums.index(first_number) : nums.index(last_number) + 1]

    # ! Refactored
    nums.sort()
    first_index = next((i for i, num in enumerate(nums) if num >= lowest), None)
    last_index = next((i for i, num in enumerate(nums) if num >= highest), None)
    return nums[first_index : last_index + 1]


print(in_range([10, 20, 30, 40, 50], 5, 40))
print(in_range([50, 30, 40, 20, 10], 15, 30))
