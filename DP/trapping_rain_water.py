class Solution:
    def trap(self, height: List[int]) -> int:
        hlen = len(height)
        if(hlen==0):
            return 0
        left = [0 for i in range(hlen)]
        right = [0 for i in range(hlen)]
        left[0] = height[0]
        right[hlen-1] = height[hlen-1]
        for i in range(1, len(height)):
            left[i] = max(height[i], left[i-1])
        for i in range(hlen-2,-1,-1):
            right[i] = max(height[i], right[i+1])
        count = 0
        for i in range(hlen):
            count += (min(left[i],right[i])-height[i])
        return count
        


class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        left_max = 0
        right_max = 0
        ans = 0
        while(left < right):
            if(height[left] < height[right]):
                if(height[left]>=left_max):
                    left_max = height[left]
                else:
                    ans += left_max - height[left]
                left += 1
            if(height[left] >= height[right]):
                if(height[right]>=right_max):
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                right -= 1
        return ans
