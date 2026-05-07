class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        min_valid_speed = right

        while left <= right:
            time = 0
            midpoint_speed = (left + right) // 2

            for pile in piles:
                time += math.ceil(pile / midpoint_speed)
            
            if time > h:
                left = midpoint_speed + 1
            else:
                min_valid_speed = midpoint_speed
                right = min_valid_speed - 1
        
        return min_valid_speed