from auth import AuthServer
from otp import OTPService
from bank import BankServer
from logger import LogService

def main():
    user_id = input("아이디 입력: ")       # id : admin
    password = input("비밀번호 입력: ")    # passward : 1234

    auth = AuthServer()
    otp = OTPService()
    bank = BankServer()
    logger = LogService()

    print("송금 요청 시작")

    if not auth.authenticate(user_id, password):
        print("사용자 인증 실패")
        return

    otp.send_otp(user_id)
    input_otp = input("수신된 OTP를 입력하세요: ")

    if not otp.verify_otp(input_otp):
        print("OTP 인증 실패")
        return
    
    receiver_id = input("송금할 대상 아이디 입력: ")

    try:
        amount = int(input("송금할 금액 입력: "))
    except ValueError:
        print("잘못된 금액 형식입니다.")
        return

    success, message = bank.transfer(user_id, receiver_id, amount)
    print(f"{message}")

    logger.log_transaction(user_id, receiver_id, amount, "성공" if success else "실패")

    if success:
        print(f"{receiver_id}님에게 {amount}원 송금 완료. 영수증 발급됨.")
    else:
        print("송금 실패 - 재시도 가능")

if __name__ == "__main__":
    main()
