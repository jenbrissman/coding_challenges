###** Bounded Ratio **###
# You are given an array of integers a and two integers l and r. You task is to calculate a boolean array b, where b[i] = true if there exists an integer x, such that a[i] = (i + 1) * x and l ≤ x ≤ r. Otherwise, b[i] should be set to false.

# Example

# For a = [8, 5, 6, 16, 5], l = 1, and r = 3, the output should be boundedRatio(a, l, r) = [false, false, true, false, true].

# For a[0] = 8, we need to find a value of x such that 1 * x = 8, but the only value that woul
#print(boundedRatio([8, 5, 6, 16, 5], 1, 3)) # => [false, false, true, false, true]


# For a[0] = 8, we need to find a value of x such that 1 * x = 8, but the only value that would work is x = 8 which doesn't satisfy the boundaries 1 ≤ x ≤ 3, so b[0] = false.
# For a[1] = 5, we need to find a value of x such that 2 * x = 5, but there is no integer value that would satisfy this equation, so b[1] = false.
# For a[2] = 6, we can choose x = 2 because 3 * 2 = 6 and 1 ≤ 2 ≤ 3, so b[2] = true.
# For a[3] = 16, there is no an integer 1 ≤ x ≤ 3, such that 4 * x = 16, so b[3] = false.
# For a[4] = 5, we can choose x = 1 because 5 * 1 = 5 and 1 ≤ 1 ≤ 3, so b[4] = true.

def boundedRatio(a, l, r):
    b=[]
    for i in range(len(a)):
        x = a[i] / (i + 1)
        b.append(l <= x <= r and x== int(x))
    return b
print(boundedRatio([8, 5, 6, 16, 5], 1, 3))



#Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

class Solution:
    def twoSum(self, nums, target: int): 
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
       
        seen = {}

        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target-num], i]
            elif num not in seen:
                seen[num]=i


#Remove Element
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.


class Solution:
    def removeElement(self, nums, val: int) -> int:
        i = -1
        for j in range(len(nums)):
            if nums[j] != val:
                i = i + 1
                nums[i] = nums[j]
        return i + 1
    
    
        