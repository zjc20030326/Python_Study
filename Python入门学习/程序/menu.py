class Meat:
    nums = 0


class Egg(Meat):
    name = "鸡蛋"
    price = 1


class Beef(Meat):
    name = "牛肉"
    price = 25


class Mutton(Meat):
    name = "羊肉"
    price = 30


class Vegetable:
    nums = 0


class Onion(Vegetable):
    name = "洋葱"
    price = 2


class Tomato(Vegetable):
    name = "番茄"
    price = 2


class Potato(Vegetable):
    name = "土豆"
    price = 3


class Radish(Vegetable):
    name = "萝卜"
    price = 3


class Menu:
    def order(self):
        self.x = []
        print("客官想要吃点什么？")

        dishes = input(
            "1.洋葱炒牛肉；2.洋葱炒羊肉；3.煎蛋；4.番茄炒蛋；5.土豆萝卜炖羊肉："
        )
        dishes = dishes.split()

        while dishes:
            dish = dishes.pop(0)

            if dish == "1":
                onion = Onion()
                onion.num = 1  # type: ignore # 动态添加属性
                beef = Beef()
                beef.num = 1  # type: ignore
                self.x.extend([beef, onion])

            if dish == "2":
                onion = Onion()
                onion.num = 1  # type: ignore
                mutton = Mutton()
                mutton.num = 1  # type: ignore
                self.x.extend([mutton, onion])

            if dish == "3":
                egg = Egg()
                egg.num = 2  # type: ignore
                self.x.append(egg)

            if dish == "4":
                tomato = Tomato()
                tomato.num = 2  # type: ignore
                egg = Egg()
                egg.num = 3  # type: ignore
                self.x.extend([tomato, egg])

            if dish == "5":
                potato = Potato()
                potato.num = 2  # type: ignore
                radish = Radish()
                radish.num = 1  # type: ignore
                mutton = Mutton()
                mutton.num = 2  # type: ignore
                self.x.extend([potato, radish, mutton])

    def pay(self):
        total = 0
        print("\n--- 账单详情 ---")
        for each in self.x:
            print(f"{each.name}: 单价{each.price} * 数量{each.num}")
            total += each.price * each.num

        print(f"----------------")
        print(f"感谢惠顾，您一共消费了 {total} 元，欢迎下次光临~")


# --- 这里是必须添加的程序入口 ---
if __name__ == "__main__":
    m = Menu()  # 1. 创建菜单实例
    m.order()  # 2. 调用点菜方法
    m.pay()  # 3. 调用结账方法
