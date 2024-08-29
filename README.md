 # Balanced Brackets Checker

This project contains an implementation of a stack data structure and two functions that check whether a given expression containing brackets is balanced or not.

## Stack Implementation

The Stack class provides the following methods:

- __init__(): Initializes an empty stack.
- is_empty(): Checks if the stack is empty.
- push(item): Adds an item to the top of the stack.
- pop(): Removes and returns the top item from the stack.
- peek(): Returns the top item from the stack without removing it.
- size(): Returns the number of items in the stack.

## Balanced Brackets Checker Functions

The is_balanced(expression) function checks whether the given expression is balanced in terms of the opening and closing brackets. It uses the Stack implementation to keep track of the opening brackets and checks if the closing brackets match the corresponding opening brackets.

The is_balanced_optimized(expression) function is an optimized version of the is_balanced() function, which avoids unnecessary comparisons and improves performance.

## Usage

1. Import the Stack class and the is_balanced() or is_balanced_optimized() function from the script.
2. Use the functions to check the balance of expressions containing brackets:

from brackets_checker import Stack, is_balanced, is_balanced_optimized

balanced_expression = "(((([{}]))))"
unbalanced_expression = "{{[(])]}}"

if is_balanced_optimized(balanced_expression):
    print("Balanced")
else:
    print("Not Balanced")

if is_balanced_optimized(unbalanced_expression):
    print("Balanced")
else:
    print("Not Balanced")

## Testing

The script includes a set of test cases for both balanced and unbalanced expressions. You can run these tests to ensure the correctness of the is_balanced_optimized() function.

## Requirements

- Python 3.x

## License

This project is licensed under the [MIT License](LICENSE).

README.md (Russian)

# Проверка сбалансированности скобок

Этот проект содержит реализацию структуры данных стек (Stack) и две функции, которые проверяют, является ли заданное выражение, содержащее скобки, сбалансированным или нет.

## Реализация стека

Класс Stack предоставляет следующие методы:

- __init__(): Инициализирует пустой стек.
- is_empty(): Проверяет, является ли стек пустым.
- push(item): Добавляет элемент в верхнюю часть стека.
- pop(): Удаляет и возвращает верхний элемент из стека.
- peek(): Возвращает верхний элемент из стека, не удаляя его.
- size(): Возвращает количество элементов в стеке.

## Функции проверки сбалансированности скобок

Функция is_balanced(expression) проверяет, является ли заданное выражение сбалансированным в отношении открывающих и закрывающих скобок. Она использует реализацию стека Stack для отслеживания открывающих скобок и проверяет, соответствуют ли закрывающие скобки соответствующим открывающим скобкам.

Функция is_balanced_optimized(expression) является оптимизированной версией функции is_balanced(), которая избегает ненужных сравнений и повышает производительность.

## Использование

1. Импортируйте класс Stack и функции is_balanced() или is_balanced_optimized() из скрипта.
2. Используйте функции для проверки сбалансированности выражений, содержащих скобки:

from brackets_checker import Stack, is_balanced, is_balanced_optimized

balanced_expression = "(((([{}]))))"
unbalanced_expression = "{{[(])]}}"

if is_balanced_optimized(balanced_expression):
    print("Сбалансировано")
else:
    print("Не сбалансировано")

if is_balanced_optimized(unbalanced_expression):
    print("Сбалансировано")
else: print("Не сбалансировано")

## Тестирование

Скрипт включает набор тестовых примеров для сбалансированных и несбалансированных выражений. Вы можете запустить эти тесты, чтобы убедиться в правильности работы функции is_balanced_optimized().

## Требования

- Python 3.x

## Лицензия

Этот проект распространяется под [Лицензией MIT](LICENSE).

7522 из 16384
