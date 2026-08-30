class Solution:
    def trap(self, height: List[int]) -> int:
        #think how much water is sitting on top of each index
        left = 0
        right = 0
        max_left = [0] * len(height)
        max_right = [0] * len(height)
        water = [0] * len(height)


        for i in range(len(height)):
            j = -i - 1
            max_left[i] = left
            max_right[j] = right
            left = max(left, height[i])
            right = max(right, height[j])
        

        for i in range(len(height)):
            potential = min(max_left[i], max_right[i]) - height[i]
            if potential < 0:
                water[i] = 0
            else:
                water[i] = potential

        sum = 0
        for count in water:
            sum = sum + count
        
        return sum
            


