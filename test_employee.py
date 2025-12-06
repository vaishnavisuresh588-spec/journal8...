from employee import employee_details

def test_employee_details():
    expected_output = (
        "Employee Name: vaishnavi\n"
        "Employee ID: 01fe24bca014\n"
        "Department:bca\n"
        "Salary:60000\n"
    )

    assert employee_details("vaishnavi","01fe24bca014","bca",60000) == expected_output
