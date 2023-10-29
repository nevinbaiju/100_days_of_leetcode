class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        t1, t2, t3 = target
        filtered = []
        for triplet in triplets:
            if t1 >= triplet[0] and t2 >= triplet[1] and t3 >= triplet[2]:
                filtered.append(triplet)
        a1 = a2 = a3 = 0
        
        for triplet in filtered:
            a1 = max(a1, triplet[0])
            a2 = max(a2, triplet[1])
            a3 = max(a3, triplet[2])
        return True if a1 == t1 and a2 == t2 and a3 == t3 else False
