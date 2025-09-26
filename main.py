# class 
# try except

class account:
    def __init__(self, account_id, name, in_money):
        self.account_id = account_id
        self.name = name
        self.in_money = in_money

account_info = []
name_info = []
money_info = []


while True:

    print("------MENU------")
    print("1. 계좌개설")
    print("2. 입금")
    print("3. 출금")
    print("4. 계좌번호 전체 출력")
    print("5. 프로그램 종료")
    print("\n")
    menu_select = int(input("선택(1~5까지의 숫자만 입력): "))
    
    if menu_select == 1:
        print("[계좌개설]")
        make_bank_account = int(input("계좌 ID (숫자로 입력) : "))
        account_info.append(make_bank_account)
        name = str(input("이름 : "))
        name_info.append(name)
        in_money = int(input("입금액 : "))
        money_info.append(in_money)
        print("\n")

    elif menu_select == 2:
        print("[입  금]")
        account_ID = int(input("계좌 ID : "))
        if account_ID in account_info:
            add_money = int(input("입금액 : "))
            money_info.insert(0,money_info[0] + add_money) 
            money_info.remove(1)
            print("입금완료 \n")

    elif menu_select == 3:
        print("[출  금]")
        account_ID = int(input("계좌 ID : "))
        if account_ID in account_info:
            minus_money = int(input("출금액 : "))
            money_info.insert(0,money_info[0] - minus_money)
            print("출금 완료\n")

    elif menu_select == 4:
        for i in account_info:
            print("계좌 ID : ", account_info)
            print("이름 : ", name_info)
            print("잔액 : ", money_info)
            print("\n")
    
    elif menu_select == 5:
        break

    else:
        print("다시 입력")



