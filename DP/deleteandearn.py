from collections import defaultdict
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        minimum = min(nums)
        maximum = max(nums)
        print(minimum,maximum)
        for i in nums:
            dic[i] += i
        arr = []
        for i in range(maximum+1):
            arr.append(dic[i])

        dp = [0 for i in range(maximum+1)]

        dp[0] = arr[0]
        dp[1] = arr[1]

        for i in range(2,maximum + 1):
            if(arr[i]==0):
                dp[i] = max(dp[i-1],dp[i-2])
            if(arr[i-1]==0):
                dp[i] = dp[i-1]+arr[i]
            if(arr[i]>0 and arr[i-1]>0):
                dp[i] = max(dp[i-3], dp[i-2]) + arr[i]
        # print(max(dp[maximum], dp[maximum-1]))
        return (max(dp[maximum], dp[maximum-1]))
