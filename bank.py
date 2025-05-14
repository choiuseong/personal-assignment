class Account:
    def __init__(self, user_id, balance=1000000):
        self.user_id = user_id
        self.balance = balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True, "송금 성공"
        return False, "잔액 부족"


class BankServer:
    def __init__(self):
        self.accounts = {"admin": Account("admin")}

    def transfer(self, user_id, amount):
        account = self.accounts.get(user_id)
        if not account:
            return False, "계좌 없음"
        return account.withdraw(amount)
