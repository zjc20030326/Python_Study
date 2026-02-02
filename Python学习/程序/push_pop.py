stack = []


def push_stack(stack, item):
    stack.append(item)


def pop_stack(stack):
    return stack.pop()


def print_stack(stack):
    print("栈:")
    for each in stack[::-1]:
        print(each)


while True:
    command = input("请输入指令(push/pop/top/exit):")
    if command == "push":
        item = int(input("请输入将要压入栈中的元素:"))
        push_stack(stack, item)
        print_stack(stack)
    elif command == "pop":
        if stack:
            print(pop_stack(stack))
            print_stack(stack)
        else:
            print("栈已空~")
    elif command == "top":
        if stack:
            print(stack[-1])
        else:
            print("栈已空~")
    elif command == "exit":
        break
    else:
        print("指令输入错误，请重新输入!")
