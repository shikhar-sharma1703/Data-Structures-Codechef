def BracketChecker(abc):
    stack = []

    opening = ['{', '(', '[']
    closing = ['}', ')', ']']
    for i in range(len(abc)):
        ch = abc[i]
        if ch in opening:
            stack.append(ch)
        elif ch in closing:
            if len(stack) > 0:
                chx = stack.pop()
                if (ch == ')' and chx != '(') or (ch == ']' and chx != '[') or (ch == '}' and chx != '{'):
                    print("Error at {} , {} is mismatched".format(i, ch))
            else:
                print("Error at {} , {} is mismatched".format(i, ch))


abc = input()
BracketChecker(abc)
