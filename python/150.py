class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens.pop())
        operator = {'+', '-', '*', '/'}
        operands_stack = []
        for token in tokens:
            if token not in  operator:
                operands_stack.append(int(token))
            else:
                operand_1 = operands_stack.pop()
                operand_2 = operands_stack.pop()
                # print("{}{}{}".format(operand_2, token, operand_1))
                if token == "/" and operand_2 < 0 and operand_1 > 0:
                    result = -1 * (abs(operand_2) // operand_1)
                elif token == "/" and ( operand_2 > 0 and operand_1 < 0):
                    result = -1 * (operand_2 // abs(operand_1))
                elif token == "/":
                    result = operand_2 // operand_1
                elif token == "+":
                    result = operand_2 + operand_1
                elif token == "-":
                    result = operand_2 - operand_1
                elif token == "*":
                    result = operand_2 * operand_1
                operands_stack.append(result)
        return operands_stack.pop()
                
        
