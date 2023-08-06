import PySimpleGUI as Sg


def inner_demo():
    inner_demo_test()
    Sg.popup_ok("示例")
    return 0


def inner_demo_test():
    print("测试相关功能！")


if __name__ == '__main__':
    inner_demo()
