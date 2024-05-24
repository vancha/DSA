'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:

    0 <= nums.length <= 105
    -109 <= nums[i] <= 109



'''

def longestConsecutive(self, nums: List[int]) -> int:
    if not nums:
        return 0
    if len(nums) == 1:
        return 1

    maxi = 1
    streak = 1

    previous = min(nums)

    for num in sorted(nums)[1:]:
        if num == previous + 1:
            streak += 1
        elif not num == previous:
            streak = 1
        
        if streak > maxi:
            maxi = streak

        previous = num

    return maxi
