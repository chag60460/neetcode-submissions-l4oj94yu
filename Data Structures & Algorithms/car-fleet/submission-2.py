class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_array = sorted([(position[i], speed[i])for i in range(len(position))], reverse=True)
        time_stack = []

        for car_position, car_speed in sorted_array:
            car_time = (target - car_position) / car_speed
            if not time_stack or car_time > time_stack[-1]:
                time_stack.append(car_time)
        
        return len(time_stack)
