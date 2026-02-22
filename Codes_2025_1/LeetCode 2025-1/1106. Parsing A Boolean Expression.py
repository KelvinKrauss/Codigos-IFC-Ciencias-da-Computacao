
class Solution(object):
    def parseBoolExpr(self, expression):
        """
        :type expression: str
        :rtype: bool
        """
        def eval_expr(op, vals):
            if op == '!':
                return not vals[0]
            elif op == '&':
                return all(vals)
            elif op == '|':
                return any(vals)

        stack = []
        for ch in expression:
            if ch == ',':
                continue
            elif ch in ('t', 'f'):
                stack.append(True if ch == 't' else False)
            elif ch in ('!', '&', '|', '('):
                stack.append(ch)
            elif ch == ')':
                vals = []
                while isinstance(stack[-1], bool):
                    vals.append(stack.pop())
                stack.pop()  # remove '('
                op = stack.pop()  # operator
                stack.append(eval_expr(op, vals[::-1]))
        return stack[0]
#input area
s = Solution()
print(s.parseBoolExpr("&(|(v))"))