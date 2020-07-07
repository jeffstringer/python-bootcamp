# tuple unpacking example

employee_hours = [('Billy', 40), ('Mary', 100), ('Jane', 80)]

def star_employee(employee_hours):
    current_hours = 0
    employee = ''

    for name, hours in employee_hours:
        if hours > current_hours:
            current_hours = hours
            employee = name
    return (employee,current_hours)

star,hours = star_employee(employee_hours)

print(f'the employee who worked the most hours is {star} who worked {hours} hours')
