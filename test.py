# 这是一个给初学者练习用的小程序。
# 目标：让你可以反复选择功能，而不是运行一次就结束。

# 使用 while True 可以让程序一直循环运行。
# 只有当用户选择“退出”时，才会跳出循环。
while True:
    # 每次循环开始时，先打印菜单，让用户知道可以做什么。
    print("\n====== 功能菜单 ======")
    print("1. 显示欢迎信息")
    print("2. 计算两个数字的和")
    print("3. 退出程序")

    # input() 会等待用户输入内容。
    # strip() 的作用是去掉输入前后的空格，避免误输入。
    choice = input("请输入功能编号（1/2/3）：").strip()

    # 如果用户输入 1，就执行欢迎信息功能。
    if choice == "1":
        # 这里演示最基础的变量。
        name = input("请输入你的名字：").strip()

        # 如果用户没有输入名字，就给一个默认名字。
        if name == "":
            name = "同学"

        # 打印欢迎信息。
        print(f"你好，{name}！欢迎继续学习 Python。")

    # 如果用户输入 2，就执行“两个数字相加”的功能。
    elif choice == "2":
        # 提示用户输入第一个数字。
        first_text = input("请输入第一个数字：").strip()

        # 提示用户输入第二个数字。
        second_text = input("请输入第二个数字：").strip()

        # 用 try/except 处理“输入不是数字”的情况，避免程序崩溃。
        try:
            # float() 可以把文本转换成数字（支持整数和小数）。
            first_number = float(first_text)
            second_number = float(second_text)

            # 计算两个数字的和。
            total = first_number + second_number

            # 把结果打印出来。
            print(f"计算结果：{first_number} + {second_number} = {total}")
        except ValueError:
            # 如果转换失败，说明输入的内容不是有效数字。
            print("输入有误：请确保你输入的是数字，例如 3 或 3.5。")

    # 如果用户输入 3，就结束循环并退出程序。
    elif choice == "3":
        print("程序结束，欢迎下次再来！")
        break

    # 如果输入不是 1/2/3，就提示重新输入。
    else:
        print("无效选择：请输入 1、2 或 3。")
