from collections import deque
import random
import time

queue = deque()
request_id = 0

def generate_request():
    global request_id
    request_id += 1
    new_request = f"Заявка №{request_id}"
    print(f"Генерація: {new_request}")
    queue.append(new_request)

def process_request():
    if queue:
        current_request = queue.popleft()
        print(f"Обробка: {current_request}")
    else:
        print("Черга пуста. Очікування нових заявок...")

def main():
    print("Програма розпочала роботу. Натисніть Ctrl+C для виходу.")
    try:
        while True:
            if random.choice([True, False]):
                generate_request()
            
            process_request()
            
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nПрограму завершено користувачем.")

if __name__ == "__main__":
    main()
