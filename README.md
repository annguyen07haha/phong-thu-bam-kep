# Demo thuật toán băm kép Dual-Hash

Đây là mã nguồn phần phòng thủ thuộc đồ án môn An toàn thông tin. Code dùng để demo cơ chế băm mật khẩu qua 2 lớp (Modulo và SHA-256) nhằm chống lại kỹ thuật tấn công từ điển.

## Danh sách file mã nguồn
- **`mã hóa mật khẩu.py`**: Chứa thuật toán băm tùy chỉnh `custom_hash_modulo` (chia dư cho 1000003 + xáo trộn bit) và hàm `hash_sha256`. Khi chạy, file sẽ yêu cầu nhập vào mật khẩu hồ sơ và mật khẩu ngẫu nhiên để in ra so sánh kết quả mã hóa.
- **`sinh ngẫu nhiên mật khẩu.py`**: Script sử dụng thư viện `secrets` và `string` để sinh ra mật khẩu ngẫu nhiên độ dài 14 ký tự (bao gồm chữ cái, chữ số và ký tự đặc biệt). Code này dùng để tạo ra nhóm mật khẩu đối chứng.

## Hướng dẫn sử dụng
1. Để tạo ra một mật khẩu ngẫu nhiên an toàn, chạy lệnh:
   `python "sinh ngẫu nhiên mật khẩu.py"`
2. Để test thuật toán băm 2 lớp, chạy lệnh dưới đây và nhập lần lượt mật khẩu hồ sơ và mật khẩu ngẫu nhiên vào terminal:
   `python "mã hóa mật khẩu.py"`
