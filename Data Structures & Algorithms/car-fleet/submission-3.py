class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        tracking_stack = []
        sorted_array = sorted([(position[i], speed[i]) for i in range(len(position))], reverse=True)

        for car_position, car_speed in sorted_array:
            time = (target - car_position) / car_speed
            if not tracking_stack or time > tracking_stack[-1]:
                tracking_stack.append(time)

        return len(tracking_stack)