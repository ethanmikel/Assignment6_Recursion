"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my/our honor, Kavya Chowti and Ethan Mikel, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: kc45736
UT EID 2: etm693
"""

def group_sum(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to the
    given target.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if start >= len(nums):
        return False
    include_current = group_sum(start + 1, nums, target - nums[start])
    exclude_current = group_sum(start + 1, nums, target)
    return include_current or exclude_current

def group_sum_6(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to the
    given target. Additionally, if there is are 6's present in the array, they must all
    be chosen.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if nums[start] == 6:
        return group_sum_6(start + 1, nums, target - nums[start])

    include_current = group_sum_6(start + 1, nums, target - nums[start])
    exclude_current = group_sum_6(start + 1, nums, target)
    return include_current or exclude_current

def group_no_adj(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to
    the given target. Additionally, if a value is chosen, the value immediately after
    (the value adjacent) cannot be chosen.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if start >= len(nums):
        return False
    
    include_current = group_no_adj(start + 2, nums, target - nums[start])
    exclude_current = group_no_adj(start + 1, nums, target)
    return include_current or exclude_current

def group_sum_5(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to
    the given target. Additionally, if a multiple of 5 is in the array, it must be included
    If the value immediately following a multiple of 5 if 1, it must not be chosen

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    current = nums[start]
    if current % 5 == 0:
        if start + 1 < len(nums) and nums[start + 1] == 1:
            return group_sum_5(start + 2, nums, target - current)
        return group_sum_5(start + 1, nums, target - current)

    return group_sum_5(start + 1, nums, target - current) or group_sum_5(start + 1, nums, target)

def group_sum_clump(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to
    the given target. Additionally, if there is a group of identical numbers in succession,
    they must all be chosen, or none of them must be chosen.
    EX: [1, 2, 2, 2, 5, 2], all three of the middle 2's must be chosen, or none of them must be
    chosen to be included in the sum. One loop is allowed to check for identical numbers.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    group_sum = nums[start]
    next_index = start + 1

    while next_index < len(nums) and nums[next_index] == nums[start]:
        group_sum += nums[next_index]
        next_index += 1

    return (
        group_sum_clump(next_index, nums, target - group_sum) or 
        group_sum_clump(next_index, nums, target)
    )

def split_array(nums):
    """
    Given a list of ints, determine if the numbers can be split evenly into two groups
    The sum of these two groups must be equal
    Write a recursive helper to call from this function

    pre: len(nums) >= 0, nums will only contain ints
    post: return True if nums can be split, False otherwise
    """
    total_sum = sum(nums)
    target = total_sum // 2
    n = len(nums)

    def can_split(start, current_sum):
        if current_sum == target:
            return True
        if start >= n or current_sum > target:
            return False
        
        return can_split(start + 1, current_sum + nums[start]) or can_split(start + 1, current_sum)

    return can_split(0, 0)

def split_odd_10(nums):
    """
    Given a list of ints, determine if the numbers can be split evenly into two groups
    The sum of one group must be odd, while the other group must be a multiple of 10
    Write a recursive helper to call from this function

    pre: len(nums) >= 0, nums will only contain ints
    post: return True if nums can be split, False otherwise
    """
    def recursive_split(start, odd_sum, ten_sum):
        if start >= len(nums):
            return odd_sum % 2 != 0 and ten_sum % 10 == 0
        
        return (recursive_split(start + 1, odd_sum + nums[start], ten_sum) or
                recursive_split(start + 1, odd_sum, ten_sum + nums[start]) or
                recursive_split(start + 1, odd_sum, ten_sum))

    return recursive_split(0, 0, 0)

def split_53(nums):
    """
    Given a list of ints, determine if the numbers can be split evenly into two groups
    The sum of these two groups must be equal
    Additionally, all multiples of 5 must be in one group, and all multiples of 3 (and not 5)
    must be in the other group
    Write a recursive helper to call from this function

    pre: len(nums) >= 0, nums will only contain ints
    post: return True if nums can be split, False otherwise
    """
    total = sum(nums)
    if total % 2 != 0: return False

    def can_split(i, sum5, sum3):
        if i == len(nums): return sum5 == sum3
        n = nums[i]
        if n % 5 == 0: return can_split(i + 1, sum5 + n, sum3)
        if n % 3 == 0: return can_split(i + 1, sum5, sum3 + n)
        return (can_split(i + 1, sum5 + n, sum3) or
                can_split(i + 1, sum5, sum3 + n))

    return can_split(0, 0, 0)