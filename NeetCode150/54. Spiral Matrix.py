class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l_lim, up_lim = -1, -1
        r_lim, down_lim = len(matrix[0]), len(matrix)
        
        ans = []
        total_items = r_lim*down_lim
        #print(total_items, ans)
        
        while len(ans) != total_items:
            #print("right")
            for i in range(l_lim+1, r_lim):
                ans.append(matrix[up_lim+1][i])
                #print(matrix[up_lim+1][i])
            up_lim += 1
            #print("down")
            
            if len(ans) == total_items:
                #print(ans)
                break
            for j in range(up_lim+1, down_lim):
                ans.append(matrix[j][r_lim-1])
                #print(matrix[j][r_lim-1])
            r_lim -= 1
            #print('left')
            
            if len(ans) == total_items:
                #print(ans)
                break
            for i in range(r_lim-1, l_lim, -1):
                ans.append(matrix[down_lim-1][i])
                #print(matrix[down_lim-1][i])
            down_lim -= 1
            #print('up')
            
            if len(ans) == total_items:
                #print(ans)
                break
            for j in range(down_lim-1, up_lim, -1):
                ans.append(matrix[j][l_lim+1])
                #print(matrix[j][l_lim+1])
            l_lim += 1
            #print("ans")
            #print(ans)
        return ans
            
