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
        return "There is no information about workers."
    else:
        average_salary = sum_salary / all_workers

    return sum_salary, average_salary


total_salary, average_salary = total_salary_inf("path/to/info.txt")
print(f"Total salary: {total_salary}, Average salary: {average_salary}")

