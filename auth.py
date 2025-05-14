class AuthServer:
    def authenticate(self, user_id, password):
        print("[AuthServer] 사용자 인증 중...")
        return user_id == "admin" and password == "1234"
