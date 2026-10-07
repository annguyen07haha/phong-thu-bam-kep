import hashlib

def custom_hash_modulo(password: str) -> int:
    MOD = 1000003
    base = 257
    h = 0
    for c in password:
        h = (h * base + ord(c)) % MOD

    for i in range(100):
        h = ((h << 5) ^ (h >> 3) ^ 12345) % MOD
    return h

def hash_sha256(password: str) -> str:
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

if __name__ == "__main__":
    pw1 = input("Mật khẩu từ hồ sơ: ")
    pw2 = input("Mật khẩu sinh ngẫu nhiên: ")
    pw1_modulo = custom_hash_modulo(pw1)
    pw1_sha256 = hash_sha256(pw1)
    pw2_modulo = custom_hash_modulo(pw2)
    pw2_sha256 = hash_sha256(pw2)
    
    
    print("Mật khẩu 1 (Dựa trên hồ sơ):")
    print(f" - Modulo Hash: {pw1_modulo}")
    print(f" - SHA-256    : {pw1_sha256}")  
    print("-" * 55)
    print("Mật khẩu 2 (Ngẫu nhiên):")
    print(f" - Modulo Hash: {pw2_modulo}")
    print(f" - SHA-256    : {pw2_sha256}")
