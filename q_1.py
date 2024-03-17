def total_salary_inf(path):
    sum_salary = 0
    all_workers = 0

    with open(path, 'r') as file:
        text = file.readlines()
        for line in text:
            name, salary = line.strip().split(',')
            sum_salary += int(salary)
            all_workers += 1

    if all_workers == 0:
        return "немає інформіції по робітникам"
    else:
        average_salary = sum_salary / all_workers

    return sum_salary, average_salary


total_salary, average_salary = total_salary_inf("path/to/info.txt")
print(f"Загальна сума заробітної плати: {total_salary}, Середня заробітна плата: {average_salary}")

