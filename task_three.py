import sys
from collections import defaultdict

def load_logs(file_path: str):
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split(' ', 3)
                logs.append({
                    'date': parts[0],
                    'time': parts[1],
                    'level': parts[2],
                    'message': parts[3] if len(parts) > 3 else ''
                })
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")
        sys.exit(1)
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        sys.exit(1)
    return logs

def count_logs_by_level(logs):
    counts = defaultdict(int)
    for log in logs:
        counts[log['level']] += 1
    return counts

def display_log_counts(counts):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count:<8}")

def main():
    if len(sys.argv) < 2:
        print("Використання: python main.py /path/to/logfile.log [level]")
        sys.exit(1)

    file_path = sys.argv[1]
    level = sys.argv[2].upper() if len(sys.argv) > 2 else None

    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if level:
        filtered_logs = [log for log in logs if log['level'] == level]
        print(f"\nДеталі логів для рівня '{level}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")

if __name__ == "__main__":
    main()
