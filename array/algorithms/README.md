# Intuition

We can iterate over the entire sorted list. If the current number is equal to the previous number, we increment our streak. If not, we reset the streak.

# Approach

If we can store the current streak and the maximum streak of consecutive numbers as variables like so:
```
streak = 1
maxi = 1
```
We can start by getting the smallest number from the input to start looping:
```
previous = min(nums)
```

make sure the loop starts at index 1 rather than 0, because the value we stored in previous represents the element before the current one:
for num in sorted(nums)[1:]:

from that point on, we check two things:

    1. is the current number consecutive to our previous number
    2. if the current number differs from our previous number

If 1 is true, we want to increment our current streak:
```
if num == previous + 1:
    streak += 1
```
if 2 is true, we want to reset our streak. Because if the current number differs and is not consecutive, our streak is broken:
```
elif not num == previous:
    streak = 1
```
Finally, at the end of each iteration, we just check if the current streak is bigger than our maximum streak, and if so, update our maximum correspondingly. When the loop has finished, maxi will hold the result :)

In the end, the trick to this solution is to just sort the input.
Complexity

    Time complexity:
    O(n), since we need to iterate over the list once

    Space complexity:
    O(n), since we need to duplicate the list to sort it

# Code

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #quick optimization, if nums is empty or 1, just return
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
        
