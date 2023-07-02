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
