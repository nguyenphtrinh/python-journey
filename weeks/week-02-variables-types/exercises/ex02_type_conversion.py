"""
Bài tập 02: Chuyển đổi kiểu dữ liệu 🔄
=========================================
Mục tiêu: Thành thạo int(), float(), str(), bool()
"""

# TODO 1: Cho so_text = "42"
# Chuyển sang int, cộng thêm 8, in kết quả
print("--- 1. Chuyển đổi chuỗi sang số nguyên ---")
so_text = "42"
so = int(so_text)
print(f"Giá trị ban đầu: '{so_text}', cộng thêm 8: {so + 8}")  # 50

# TODO 2: Cho pi = 3.14159
# Chuyển sang int (sẽ được bao nhiêu?), in kết quả
print("\n--- 2. Chuyển đổi số thực sang số nguyên ---")
pi = 3.14159
pi_int = int(pi)
print(f"pi = {pi} sau khi chuyển int(): {pi_int} (phần thập phân bị cắt bỏ)")

# TODO 3: Kiểm tra bool() của các giá trị sau và in kết quả
# bool(0), bool(1), bool(""), bool("hello"), bool([]), bool([1,2])
print("\n--- 3. Kiểm tra giá trị boolean ---")
print("bool(0):", bool(0))              
print("bool(1):", bool(1))              
print("bool(''):", bool(""))          
print("bool('hello'):", bool("hello"))  
print("bool([]):", bool([]))            
print("bool([1, 2]):", bool([1, 2]))

# TODO 4: Nhập chiều cao (m) và cân nặng (kg) từ người dùng
# Tính BMI = cân_nặng / (chiều_cao ** 2)
# In ra BMI với 1 chữ số thập phân
print("\n--- 4. Tính chỉ số BMI ---")
chieu_cao_text = input("Nhập chiều cao (m): ")
can_nang_text = input("Nhập cân nặng (kg): ")

chieu_cao = float(chieu_cao_text)
can_nang = float(can_nang_text)

bmi = can_nang / (chieu_cao ** 2)
print(f"Chỉ số BMI: {bmi:.1f}")

# TODO 5 (Thử thách): Nhập số giây, chuyển sang giờ:phút:giây
# Ví dụ: 3661 giây → "1 giờ 1 phút 1 giây"
print("\n--- 5. Đổi giây sang giờ, phút, giây ---")
giay_text = input("Nhập tổng số giây: ")
tong_giay = int(giay_text)

gio = tong_giay // 3600
phut = (tong_giay % 3600) // 60
giay = tong_giay % 60

print(f"{tong_giay} giây → {gio} giờ {phut} phút {giay} giây")
