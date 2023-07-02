<<<<<<< HEAD
from typing import List

def generateParenthesis(n: int) -> List[str]:
    def generate_recursive(opening_used=0, closing_used=0, output_string=""):
        # print(opening_used, closing_used, output_string)
        if opening_used==n and closing_used==n:
            print(output_string)
            return
        if opening_used < n:
            output_string += '('
            opening_used += 1
            generate_recursive(opening_used, closing_used, output_string)
        if closing_used < opening_used:
            output_string += ')'
            closing_used += 1
            generate_recursive(opening_used, closing_used, output_string)
    
    generate_recursive()

if __name__ == "__main__":
    generateParenthesis(3)
=======
from typing import List

def generateParenthesis2(n: int) -> List[str]:
    temp_str = []
    ans = []
    def generate_recursive(opening_used=0, closing_used=0):
        # print(opening_used, closing_used, temp_str)
        if opening_used==n and closing_used==n:
            ans.append("".join(temp_str))
            return
        if opening_used < n:
            # print("case 2 ", output_string)
            temp_str.append('(')
            generate_recursive(opening_used+1, closing_used)
            temp_str.pop()
        if closing_used < opening_used:
            # print("case 3 ", output_string)
            temp_str.append(')')
            generate_recursive(opening_used, closing_used+1)
            temp_str.pop()
    
    generate_recursive()

    return ans

if __name__ == "__main__":
    print(generateParenthesis2(100))
>>>>>>> 11b3740f71c1eb6d457fe597d24142d93a6cf7bc
