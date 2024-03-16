def total_salary_inf(path):
    with open('info.txt', 'r') as file:
        text = file.readlines()
        workers, salary = [line.strip().split(',') for line in text]
        sum_salary += int(salary)
        all_workers += 1
    if all_workers == 0:
        return print("немає інформіції по робітникам")
    else:
        average_salary = sum_salary / all_workers
    return total_salary, average_salary

total_salary, average_salary = total_salary_inf("path/to/info.txt")
print(f"Загальна сума заробітної плати: {total_salary}, Середня заробітна плата: {average_salary}")






# total, average = total_salary("path/to/info.txt")
# print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")