from pathlib import Path


def create_files(p, n):
    if n == 0:
        return None
    else:
        # with 可以同时管理多个文件的上下文，当然你分开管理也可以
        # p / f"{n-1}.py" 是拼接源代码的文件名
        with open(__file__, "r", encoding="utf-8") as f1, open(
            p / f"{n-1}.py", "w", encoding="utf-8"
        ) as f2:
            f2.write(f1.read())
        create_files(p, n - 1)  # 递归创建下一个源代码文件


def create_dirs(cwd, n):
    if n == 0:
        return None
    else:
        p = cwd / f"clone {n - 1}"  # 拼接新文件夹的路径
        p.mkdir(exist_ok=True)  # 确保文件夹已存在也不会报错
        create_files(p, 10)  # 创建10个源代码文件拷贝
        create_dirs(cwd, n - 1)  # 递归创建下一个文件夹


create_dirs(Path.cwd(), 2)
