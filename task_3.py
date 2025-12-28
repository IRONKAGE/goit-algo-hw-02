def check_brackets_symmetry(expression):
    brackets_map = {')': '(', ']': '[', '}': '{'}
    open_brackets = brackets_map.values()
    
    stack = []
    
    for char in expression:
        if char in open_brackets:
            stack.append(char)
        elif char in brackets_map:
            if not stack or stack.pop() != brackets_map[char]:
                return f"{expression}: Несиметрично"
    
    if not stack:
        return f"{expression}: Симетрично"
    else:
        return f"{expression}: Несиметрично"

# Приклад використання:
test_cases = [
    "( ){[ 1 ]( 1 + 3 )( ){ }}",
    "( 23 ( 2 - 3);",
    "( 11 }",
    "{[()]}",
    "((()))"
]

for test in test_cases:
    print(check_brackets_symmetry(test))
