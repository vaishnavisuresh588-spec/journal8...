import employee

def employee_details(name, emp_id, department, salary):
    result = (
        f"Employee Name : {name}\n"
        f"Employee ID   : {emp_id}\n"
        f"Department    : {department}\n"
        f"Salary        : {salary}\n"
    )
    return result


if __name__ == "__main__":
    name = "vaishnavi"
    emp_id = "01fe24bca014"
    department = "bca"
    salary = "55000"
    print(employee_details(name, emp_id, department, salary))
