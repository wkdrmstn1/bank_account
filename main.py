# 1. 클래스 정의: 계좌 정보를 담는 데이터 컨테이너 역할
class Account:
    def __init__(self, account_id, name, balance):
        self.account_id = account_id
        self.name = name
        self.balance = balance
    
    # 계좌 정보를 깔끔하게 출력하는
    def __str__(self):
        return f"계좌 ID: {self.account_id}\n이름: {self.name}\n잔액: {self.balance}원"

# --- 기능별 함수 정의 ---

def make_account(account_list):
    """(1) 계좌 개설 함수"""
    print("\n[계좌개설]")
    try:
        acc_id = int(input("계좌 ID (숫자로 입력): "))
        
        # 계좌 ID 중복 확인
        for acc in account_list:
            if acc.account_id == acc_id:
                print("이미 존재하는 계좌 ID입니다.")
                return # 함수 종료
        
        name = input("이름: ")
        initial_deposit = int(input("초기 입금액: "))

        if initial_deposit < 0:
            print("초기 입금액은 0 이상이어야 합니다.")
            return

        # Account 객체를 생성하여 리스트에 추가
        new_account = Account(acc_id, name, initial_deposit)
        account_list.append(new_account)
        print(f"\n{name}님, 계좌 개설이 완료되었습니다.")

    except ValueError:
        print("계좌 ID와 입금액은 숫자로만 입력해야 합니다.")

def deposit(account_list):
    """(2) 입금 함수"""
    print("\n[입  금]")
    try:
        acc_id = int(input("계좌 ID: "))
        amount = int(input("입금액: "))

        if amount <= 0:
            print("입금액은 0보다 커야 합니다.")
            return
            
        # 계좌 찾기
        for acc in account_list:
            if acc.account_id == acc_id:
                acc.balance += amount
                print(f"\n입금 완료. 현재 잔액: {acc.balance}원")
                return # 입금 완료 후 함수 종료
        
        print("해당 계좌 ID가 존재하지 않습니다.")

    except ValueError:
        print("계좌 ID와 입금액은 숫자로만 입력해야 합니다.")

def withdraw(account_list):
    """(3) 출금 함수"""
    print("\n[출  금]")
    try:
        acc_id = int(input("계좌 ID: "))
        amount = int(input("출금액: "))

        if amount <= 0:
            print("출금액은 0보다 커야 합니다.")
            return

        # 계좌 찾기
        for acc in account_list:
            if acc.account_id == acc_id:
                if acc.balance < amount:
                    print(f"\n잔액이 부족합니다. 현재 잔액: {acc.balance}원")
                else:
                    acc.balance -= amount
                    print(f"\n출금 완료. 현재 잔액: {acc.balance}원")
                return # 출금 시도 후 함수 종료
        
        print("해당 계좌 ID가 존재하지 않습니다.")

    except ValueError:
        print("계좌 ID와 출금액은 숫자로만 입력해야 합니다.")

def print_all_accounts(account_list):
    """(4) 전체 계좌 출력 함수"""
    print("\n[계좌 전체 출력]")
    if not account_list:
        print("개설된 계좌가 없습니다.")
    else:
        for acc in account_list:
            print(acc) # Account 클래스의 __str__ 메서드가 호출됨

# --- 메인 프로그램 ---

accounts = [] # Account 객체들을 저장할 리스트

while True:
    print("\n------MENU------")
    print("1. 계좌개설")
    print("2. 입금")
    print("3. 출금")
    print("4. 계좌 전체 출력")
    print("5. 프로그램 종료")
    
    try:
        menu_select = int(input("선택(1~5까지의 숫자만 입력): "))
    except ValueError:
        print("잘못된 입력입니다. 1~5 사이의 숫자만 입력해주세요.")
        continue

    if menu_select == 1:
        make_account(accounts)
        
    elif menu_select == 2:
        deposit(accounts)

    elif menu_select == 3:
        withdraw(accounts)
            
    elif menu_select == 4:
        print_all_accounts(accounts)

    elif menu_select == 5:
        print("프로그램을 종료합니다.")
        break

    else:
        print("1~5 사이의 숫자만 입력해주세요.")