class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speed = [x for _, x in sorted(zip(position, speed), reverse=True)]
        position.sort(reverse=True)
        time_taken = [(target-curr_pos)/curr_speed for curr_pos, curr_speed in zip(position, speed)]

        fleet = 1
        for i in range(1, len(time_taken)):
            if (time_taken[i] > time_taken[i-1]):
                fleet += 1
            else:
                time_taken[i] = time_taken[i-1]
        
        return fleet
        
