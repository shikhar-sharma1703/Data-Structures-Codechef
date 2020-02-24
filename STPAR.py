def answer(size, list1):
    need = 1
    status = True
    stack = []
    for e in list1:
        while (bool(len(stack)) and stack[-1] == need):
            need += 1
            stack.pop()

        if e == need:
            need += 1

        elif bool(len(stack)) and e > stack[-1]:
            status = False
            return status

        else:
            stack.append(e)

    return status


def main():
        n = input()
        list1 = map(int, (input().split()))

        if answer(n, list1):
            print("yes")
        else:
            print("no")


main()
