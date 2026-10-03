import sys

def parse_log_line(line: str)-> dict:
    # Розбиває рядок логу на 4 складові та повертає словник
    try:
        parts = line.split(maxsplit=3)
        log_dict = {'date': parts[0], 'time': parts[1], 'level': parts[2], 'message': parts[3]}
        return log_dict
    except (IndexError,ValueError):
        print(f"Увага: Пропущено некоректний рядок логу -> {line}")


def load_logs(file_path: str) -> list:
    # Розбиває файл з логами на рядки, та формує список на основі функції
    #parse_log_line список словників
    logs_list = []
    try:
        with open(file_path,'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    parsed_line = parse_log_line(line)
                    if parsed_line:
                        logs_list.append(parsed_line)
    except FileNotFoundError:
        print(f"Помилка: Файл '{file_path}' не знайдено.")
    return logs_list

def filter_logs_by_level(logs: list, level: str) -> list:
    # Список всіх записів логу для певного рівня логування
    return [log for log in logs if log['level'].upper() == level.upper()]

def count_logs_by_level(logs: list) -> dict:
    # Підрахунок кількості записів для кожного рівня логування
    count_dict = {}
    for log in logs:
        level = log['level'].upper()
        if level in count_dict:
            count_dict[level] += 1
        else:
            count_dict[level] = 1
    return count_dict

def display_log_counts(counts: dict):
    # Форматування та виведення результатів
    print(f"{'Рівень логування':<17} | {'Кількість'}")
    print("-" * 17 + "-|-" + "-" * 9)
    for level, count in counts.items():
        print(f'{level:<17} | {count}')

def main():
    # Каркас, що об'єднує попередні функції
    if len(sys.argv) < 2:
        print('Помилка: вкажіть шлях до файлу з логами.')
        return

    file_path = sys.argv[1]
    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if len(sys.argv) >= 3:
        level = sys.argv[2]
        print(f"\nДеталі логів для рівня '{level.upper()}':")
        filtered_logs = filter_logs_by_level(logs, level)
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")

if __name__ == "__main__":
    main()

