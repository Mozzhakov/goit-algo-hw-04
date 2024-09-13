from pathlib import Path

with open('salary_file.txt', 'w', encoding="utf-8") as sal_file:
    sal_file.write('Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000')

path_to_salary = Path("salary_file.txt")

def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as sal_file:
            salaries = [el.strip().split(',')[1] for el in sal_file]
            total_salary = 0
            average_salary = 0
            for salary in salaries:
                total_salary += int(salary)
            average_salary = total_salary / len(salaries) if salaries else 0
            return f"Загальна сума заробітної плати: {total_salary}, Середня заробітна плата: {int(average_salary)}"
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return f"An error occured: {e}"
        
    
        
print(total_salary(path_to_salary))