"""
Bài tập 01: Biến trong Python 📦
=================================
Mục tiêu: Hiểu cách khai báo và sử dụng biến
"""

# TODO 1: Tạo 4 biến lưu thông tin cá nhân
# ten = ???       (str)
# tuoi = ???      (int)
# diem_tb = ???   (float)
# dang_hoc = ???  (bool)
# In ra giá trị và kiểu dữ liệu của mỗi biến bằng type()

print("--- Thông tin cá nhân ---")
ten = "Trinh"
tuoi = 19
diem_tb = 7.0
dang_hoc = True

print(ten, type(ten))
print(tuoi, type(tuoi))
print(diem_tb, type(diem_tb))
print(dang_hoc, type(dang_hoc))

# TODO 2: Hoán đổi giá trị 2 biến KHÔNG dùng biến tạm
# a = 10
# b = 20
# Sau hoán đổi: a = 20, b = 10
# Gợi ý: Python cho phép a, b = b, a

print("\n--- Hoán đổi giá trị 2 biến ---")
a = 10
b = 20
print(f"Trước: a = {a}, b = {b}")
a, b = b, a
print(f"Sau:   a = {a}, b = {b}")

# TODO 3: Augmented assignment
# Cho x = 100. Dùng +=, -=, *=, //= để biến đổi x qua 4 bước
# In ra x sau mỗi bước
print("\n--- Augmented assignment ---")
x = 100
print("x ban đầu:", x)
x += 20      # 100 + 20 = 120
print("Sau x += 20: ", x)

x -= 30      # 120 - 30 = 90
print("Sau x -= 30: ", x)

x *= 2       # 90 * 2 = 180
print("Sau x *= 2:  ", x)

x //= 7      # 180 // 7 = 25
print("Sau x //= 7: ", x)

# TODO 4 (Thử thách): Multiple assignment
# Gán 3 biến trên 1 dòng: ho, ten, tuoi = ???
# In ra: "Họ tên: [ho] [ten], [tuoi] tuổi"
print("\n--- Multiple assignment ---")
ho, ten, tuoi = "Nguyễn Phi", "Trinh", 19
print(f"Họ tên: {ho} {ten}, {tuoi} tuổi")