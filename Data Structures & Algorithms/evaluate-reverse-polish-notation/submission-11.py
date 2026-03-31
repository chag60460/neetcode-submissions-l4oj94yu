import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #Either a number or an operator
        operator_hashmap = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }
        number_stack = []
        for token in tokens:
            #If it's a number, add to the stack
            if token not in operator_hashmap:
                number_stack.append(int(token))
            #If it's an operator, perform the operation, then add result to stack
            else:
                operand2 = number_stack.pop(-1)
                operand1 = number_stack.pop(-1)
                operation = operator_hashmap[token]
                result = int(operation(operand1, operand2))
                number_stack.append(result)
        
        return number_stack.pop(-1)
