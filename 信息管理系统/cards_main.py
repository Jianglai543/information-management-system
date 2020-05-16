#! C:\Program Files\WindowsApps\20815shootingapp.AirFileViewer_1.4.6.0_x86__xcg28tkrsnqww\FVApp\apps\office\program\python.exe

import cards_tools


cards_tools.show_menu()
while 1:
    str = input("请选操作：")
    print(f"你选了{str}")

    if str in['1', '2', '3', '4']:
        if str == '1':
            cards_tools.add_menu()
        elif str == '2':
            cards_tools.show_all()
        elif str == '3':
            cards_tools.check_menu()
        elif str == '4':
            cards_tools.save_menu()
    elif str == '0':
        print("欢迎下次光临")
        break

    else:
        print("你输的不对!")