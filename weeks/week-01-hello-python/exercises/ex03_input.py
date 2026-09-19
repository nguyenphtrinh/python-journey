"""
Bài tập 03: Trò chuyện với Python 💬
=====================================
Mục tiêu: Sử dụng input() để nhận dữ liệu từ người dùng
"""

# TODO 1: Hỏi tên người dùng và in lời chào
# Ví dụ: "Xin chào, Minh!"
ten = input("Bạn tên là gì? ").strip()
print(f"Xin chào, {ten}!")

# TODO 2: Hỏi tuổi người dùng, tính và in năm sinh
# Gợi ý: Nhớ chuyển input sang int!
tuoi_text = input("Bạn bao nhiêu tuổi? ").strip()
tuoi = int(tuoi_text)
nam_hien_tai = 2026
nam_sinh = nam_hien_tai - tuoi
print(f"Bạn sinh năm khoảng: {nam_sinh}")

# TODO 3: Hỏi người dùng nhập 2 số, tính và in tổng
# Ví dụ output:
# Nhập số thứ nhất: 15
# Nhập số thứ hai: 27
# Tổng: 15 + 27 = 42
so_1_text = input("Nhập số thứ nhất: ")
so_2_text = input("Nhập số thứ hai: ")
so_1 = float(so_1_text)
so_2 = float(so_2_text)
tong = so_1 + so_2

so_1_hien_thi = int(so_1) if so_1.is_integer() else so_1
so_2_hien_thi = int(so_2) if so_2.is_integer() else so_2
tong_hien_thi = int(tong) if tong.is_integer() else tong
print(f"Tổng: {so_1_hien_thi} + {so_2_hien_thi} = {tong_hien_thi}")

# TODO 4 (Thử thách): Tạo Mad Libs mini
# Hỏi người dùng nhập: tên, tính từ, con vật, số
# Rồi in ra câu chuyện vui
print("\n--- Trò chơi Mad Libs mini ---")
ten_nhan_vat = input("Nhập tên: ").strip()
tinh_tu = input("Nhập một tính từ: ").strip()
con_vat = input("Nhập một con vật: ").strip()
so_luong = input("Nhập một con số: ").strip()

print(f"\n{ten_nhan_vat} có một con {con_vat} rất {tinh_tu}.")
print(f"Mỗi ngày nó ăn {so_luong} bát cơm!")
