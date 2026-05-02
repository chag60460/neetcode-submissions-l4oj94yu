class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        min_speed = right

        while left <= right:
            midpoint_speed = (left + right) // 2
            estimated_time = 0

            for pile in piles:
                estimated_time += math.ceil(pile / midpoint_speed)
            
            if estimated_time > h:
                left = midpoint_speed + 1
            else:
                min_speed = midpoint_speed
                right = midpoint_speed - 1
        
        return min_speed