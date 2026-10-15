

def main():
    while True:
        print("===记账本===")
        print("1. 记一笔")
        print("2. 查看所有记录")
        print("3. 查看余额")
        print("4. 退出")
        choice = input("选择：")

        if choice == '1':
            add_record()
        elif choice == '2':
            show_record()
        elif choice == '3':
            check_balance()
        elif choice == '4':
            print("再见~")
            break
        else:
            print("输入无效，请重新输入！")


def add_record():
    choice = input("收入还是支出？(r/z):").lower()
    if choice == 'r':
        num = input("金额：")
        remark = input("备注：")

        with open("zhangben.txt", "a", encoding="utf-8") as f:
            f.write(f"+{num} 收入 备注:{remark}\n")
        print("记录成功")
            
    elif choice == 'z':
        num = input("金额：")
        remark = input("备注：")
        
        with open("zhangben.txt", "a", encoding="utf-8") as f:
            f.write(f"-{num} 支出 备注:{remark}\n")
        print("记录成功")
    else:
        print("输入错误")
        return
    

def show_record():
    try:
        with open("zhangben.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()  # 读取所有行，返回列表
        if len(lines) == 0:
            print("还没有记录")
        else:
            for line in lines:
                print(line, end="")  # end=""是因为每行已经有\n了
    except FileNotFoundError:
        print("还没有记录")


def check_balance():
    try:
        with open("zhangben.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
        if len(lines) == 0:
            print("还没有记录")
        else:
            balance = 0
            for line in lines:
                if line[0] == "+":
                    balance += int(line[1:].split()[0])
                else:
                    balance -= int(line[1:].split()[0])
            print(f"余额为{balance}")
    except FileNotFoundError:
        print("还没有记录")

main()