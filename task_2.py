from collections import deque

def is_palindrome(input_string):
    cleaned_string = "".join(input_string.split()).lower()
    char_deque = deque(cleaned_string)
    
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
            
    return True  # Якщо ми пройшли весь цикл, рядок є паліндромом

# Приклад використання:
test_strings = [
    "Racecar",           # Непарна кількість, різний регістр
    "Abba",              # Парна кількість
    "A man a plan a canal Panama", # Фраза з пробілами
    "hello",             # Не паліндром
    "12321"              # Цифровий паліндром
]

for text in test_strings:
    result = "є паліндромом" if is_palindrome(text) else "не є паліндромом"
    print(f"'{text}' -> {result}")
