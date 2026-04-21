s = input("请输入测试字符串：")

# 创建一个特殊列表
stack = []

for c in s:
    if c == "(" or c == "[" or c == "{":
        stack.append(c)
    else:
        if len(stack) == 0:
            print("非法T_T")
            break

        if c == ")":
            d = "("
        elif c == "]":
            d = "["
        elif c == "}":
            d = "{"

        if d != stack.pop():
            print("非法T_T")
            break
else:
    if len(stack) == 0:
        print("合法^o^")
    else:
        print("非法T_T")
