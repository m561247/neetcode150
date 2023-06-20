# brute force

def bruteForce(nums):
    maxSum = nums[0]

    for i in range (len(nums)):

        curSum = 0

        for j in range (i, len(nums)):
            curSum += nums[j]
            maxSum = max(maxSum, curSum)


    return maxSum

# two pointer + sliding window
def kadane(nums):
    maxSum = nums[0]
    L = 0
    cur = 0
    maxL, maxR = 0, 0
    for R in range(len(nums)):
        
        if cur < 0:
            cur = 0
            L = R
        cur += nums[R]
        if cur > maxSum:
            maxSum = cur
            maxL, maxR = L, R
    return [maxL, maxR]


