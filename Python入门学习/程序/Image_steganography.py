f1 = open("test.jpg", "ab")
f2 = open("target.zip", "rb")

f1.write(f2.read())

f1.close()
f2.close()

print("完成~")
