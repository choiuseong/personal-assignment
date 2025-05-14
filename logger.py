class LogService:
    def log_transaction(self, user_id, receiver_id, amount, status):
        print(f"[LogService] {user_id} → {receiver_id} : {amount}원, 상태: {status}")


