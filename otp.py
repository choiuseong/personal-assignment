import random

class OTPService:
    def __init__(self):
        self.generated = None

    def send_otp(self, user_id):
        self.generated = str(random.randint(100000, 999999))
        print(f"[OTPService] {user_id}에게 OTP 전송: {self.generated}")

    def verify_otp(self, input_otp):
        print("[OTPService] OTP 검증 중...")
        return input_otp == self.generated
