employee = {
    "employee_id": "NV001",
    "full_name": "Nguyễn Văn An",
    "department": "Python Backend",
    "status": "probation"
}

print("Mã nhân viên:", employee["employee_id"])
print("Họ tên nhân viên:", employee["full_name"])

employee["status"] = "official"

employee["base_salary"] = 15000000

del employee["department"]

print("Thông tin nhân viên sau xử lý:", employee)
