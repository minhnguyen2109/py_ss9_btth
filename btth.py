branch_names = ["Highlands Nhà Thờ", "Highlands Bà Triệu", "Highlands Nguyễn Du", 
                "Highlands Landmark 81", "Highlands Trần Hưng Đạo"]
daily_revenues = [15500000, 28000000, 9200000, 45000000, 11000000]   
target_achieved = [True, True, False, True, False] 

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ DOANH THU HIGHLANDS =====")
    print("1. Hiển thị báo cáo doanh thu tổng hợp")
    print("2. Thống kê chi nhánh Cao nhất / Thấp nhất")
    print("3. Lọc danh sách cơ sở kém (Không đạt chỉ tiêu)")
    print("4. Thoát chương trình")
    print("================================================")
    
    choice = input("Nhập lựa chọn của bạn (1-4): ")
    
    if not choice.isdigit():
        print("[Lỗi] Lựa chọn không hợp lệ, vui lòng nhập lại số từ 1 đến 4!")
        continue
    
    choice = int(choice)

    if choice == 1:
        print("\n--- BÁO CÁO DOANH THU TỔNG HỢP ---")
        print("Tên Cơ Sở\t| Doanh Thu\t| Trạng Thái")
        print("---")
        total_revenue = 0
        for i in range(len(branch_names)):
            revenue = daily_revenues[i]
            total_revenue += revenue
            status = "Đạt" if target_achieved[i] else "Không Đạt"
            print(f"{branch_names[i]}\t| {revenue}\t| {status}")
        print(f"\n=> TỔNG DOANH THU TOÀN VÙNG: {total_revenue} VND")
    
    elif choice == 2:
        max_revenue = max(daily_revenues)
        min_revenue = min(daily_revenues)
        max_index = daily_revenues.index(max_revenue)
        min_index = daily_revenues.index(min_revenue)
        max_branch = branch_names[max_index]
        min_branch = branch_names[min_index]
        print("\n--- THÔNG KÊ CƠ SỞ NỔI BẬT ---")
        print(f"- Cơ sở có doanh thu CAO NHẤT: {max_branch} ({max_revenue} VND)")
        print(f"- Cơ sở có doanh thu THẤP NHẤT: {min_branch} ({min_revenue} VND)")
    
    elif choice == 3:
        failed_branches = []
        for i in range(len(branch_names)):
            if not target_achieved[i]: 
                failed_branches.append(branch_names[i])
        print("\n--- DANH SÁCH CƠ SỞ CẦN HỖ TRỢ (KHÔNG ĐẠT) ---")
        print(failed_branches)
    
    elif choice == 4:
        print("Hệ thống ghi nhận dữ liệu hoàn tất. Tạm biệt!")
        break
    
    else:
        print("[Lỗi] Lựa chọn không hợp lệ, vui lòng nhập lại số từ 1 đến 4!")