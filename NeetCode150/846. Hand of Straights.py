class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)% groupSize != 0:
            return False
        counts = {}
        for card in hand:
            counts[card] = counts.get(card, 0) + 1
        count_heap = [[i, j] for i, j in counts.items()]
        heapq.heapify(count_heap)
        while count_heap and len(count_heap) >= groupSize:
            temp = []
            for i in range(groupSize):
                num, count = heapq.heappop(count_heap)
#                 print(temp, [num, count])
                if temp and temp[-1][0] != num-1:
                    return False
                temp.append([num, count-1])
            for item in temp:
                if item[1]:
                    heapq.heappush(count_heap, item)
                    
        return False if count_heap else True
