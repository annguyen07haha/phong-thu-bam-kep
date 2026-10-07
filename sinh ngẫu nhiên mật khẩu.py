import secrets
import string

def sinhmatkhau(length=14):
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]|;:,.<>?/~"
    matkhau = ''.join(secrets.choice(alphabet) for _ in range(length))
    return matkhau

if __name__ == "__main__":
    password = sinhmatkhau()
    print(f"Mật khẩu {password}")
