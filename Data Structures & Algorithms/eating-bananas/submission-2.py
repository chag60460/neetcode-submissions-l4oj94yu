class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        min_valid_speed = right

        while left <= right:
            time = 0
            mid_point = (left + right) // 2
            
            for pile in piles:
                time += math.ceil(pile/mid_point)
            
            if time > h:
                left = mid_point + 1
            else:
                min_valid_speed = mid_point
                right = mid_point - 1
        
        return min_valid_speed
                