class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        minimum_valid_speed = right

        while left <= right:
            midpoint = (left + right) // 2
            time = 0

            for banana_pile in piles:
                time += math.ceil(banana_pile / midpoint)

            if time > h:
                left = midpoint + 1
            else:
                minimum_valid_speed = midpoint
                right = midpoint - 1
            
        return minimum_valid_speed