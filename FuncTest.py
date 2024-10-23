import PPL_Project


def test_all_functions():
    # Test each function one by one
    print("Original main to check all func in the project:")
    print("main to check all func in the project:")
    # Arithmetic operations
    print(PPL_Project.call_operation("add", 5, 3))  # Output: 8
    print(PPL_Project.call_operation("subtract", 10, 5))  # Output: 5
    print(PPL_Project.call_operation("multiply", 4, 2))  # Output: 8
    print(PPL_Project.call_operation("multiply", 4, "2"))  # Error: Incorrect argument types for operation 'multiply'.
    print(PPL_Project.call_operation("divide", 10, 2))  # Output: 5.0
    print(PPL_Project.call_operation("divide", 10, 0))  # Error: Division by zero is not allowed
    print(PPL_Project.call_operation("power", 2, 3))  # Output: 8
    print(PPL_Project.call_operation("square", 9))  # Output: 3.0
    print(PPL_Project.call_operation("mod", 10, 3))  # Output: 1
    print(PPL_Project.call_operation("mod", 10, 0))  # Error: Modulo by zero is not allowed

    # Comparison operations
    print(PPL_Project.call_operation("max", 7, 9))  # Output: 9
    print(PPL_Project.call_operation("min", 7, 9))  # Output: 7
    print(PPL_Project.call_operation("equal", 5, 5))  # Output: True
    print(PPL_Project.call_operation("not_equal", 5, 4))  # Output: True
    print(PPL_Project.call_operation("greater_than", 10, 5))  # Output: True
    print(PPL_Project.call_operation("less_than", 3, 7))  # Output: True
    print(PPL_Project.call_operation("greater_than_equal", 7, 7))  # Output: True
    print(PPL_Project.call_operation("less_than_equal", 2, 5))  # Output: True

    # Logical operations
    print(PPL_Project.call_operation("logical_or", True, False))  # Output: True
    print(PPL_Project.call_operation("logical_or", 1, 0))  # Error: Incorrect argument types for operation 'logical_or'.
    print(PPL_Project.call_operation("logical_and", True, True))  # Output: True
    print(PPL_Project.call_operation("logical_and", True, False))  # Output: False

    # Custom if-else logic
    print(PPL_Project.custom_if(True, lambda: "Condition is True",
                                lambda: "Condition is False"))  # Output: Condition is True
    print(PPL_Project.custom_else(False, lambda: "Condition is True",
                                  lambda: "Condition is False"))  # Output: Condition is False
    print(PPL_Project.custom_ifElse(True, lambda: "Condition is True",
                                    lambda: "Condition is False"))  # Output: Condition is True
    print(PPL_Project.custom_ifElse(False, lambda: "Condition is True",
                                    lambda: "Condition is False"))  # Output: Condition is False

    # Custom while loop test
    print("\nTesting custom_while:")
    x = 1
    count = 0

    def condition():
        return count < 10

    def action():
        nonlocal count, x
        count += 1
        x += 1

    PPL_Project.custom_while(condition, action)
    print("x:", x)  # Expected output: x: 11
    print("count:", count)  # Expected output: count: 10

    # Custom for loop test
    print("\nTesting custom_for:")
    items = []

    def action(item):
        items.append(item)

    PPL_Project.custom_for(range(1, 6), action)
    print("items:", items)  # Expected output: items: [1, 2, 3, 4, 5]

    # CustomString class tests
    s1 = PPL_Project.CustomString("Hello World")
    s2 = PPL_Project.CustomString("Python")
    print(s1.replace("World", "Universe"))  # 'Hello Universe'
    print(PPL_Project.CustomString("HELLO").isUpper())  # True
    print(PPL_Project.CustomString("Hello").isUpper())  # False
    print(PPL_Project.CustomString("hello").isLower())  # True
    print(PPL_Project.CustomString("Hello").isLower())  # False
    print(s1.concat(s2))  # 'Hello WorldPython'
    # Test for split method
    print("\nTesting CustomString split:")
    s3 = PPL_Project.CustomString("apple,banana,cherry")
    print(s3.split(","))  # Expected output: ['apple', 'banana', 'cherry']

    # CustomTuple class tests
    t1 = PPL_Project.CustomTuple(3, 1, 4, 1, 5, 9)
    try:
        print(t1.getItem(10))  # Should raise IndexError
    except IndexError as e:
        print(e)
    print(t1.getItem(2))  # Output: 4
    print(t1.getItem(-1))  # Output: 9
    try:
        print(t1.index(10))  # Should raise ValueError
    except ValueError as e:
        print(e)
    print(t1.index(4))  # Output: 2
    print(t1.length())  # Output: 6
    # Test for sequence method
    print("\nTesting CustomTuple sequence:")
    print(t1.sequence())  # Expected output: [3, 1, 4, 1, 5, 9]

    # Test for sort method
    print("\nTesting CustomTuple sort:")
    print(t1.sort())  # Expected output: (1, 1, 3, 4, 5, 9)

    # Array class tests
    arr = PPL_Project.Array(1, 2, 3)
    arr.append(4)
    print(arr.items)  # [1, 2, 3, 4]
    print(len(arr))  # 4
    print(arr.index(3))  # 2
    print(arr.find(2))  # 3
    arr.add(10, 1)
    print(arr.items)  # [1, 10, 2, 3, 4]
    arr.remove(3)
    print(arr.items)  # [1, 10, 2, 4]

    # Lexer class test
    lexer = PPL_Project.Lexer("x = 10 + 20")
    tokens = lexer.create_tokens()
    print(tokens)  # [('IDENTIFIER', 'x'), ('ASSIGN', '='), ('NUMBER', 10), ('PLUS', '+'), ('NUMBER', 20)]

    # Parser and Interpreter tests
    tokens = [('NUMBER', '3'), ('OP', '+'), ('NUMBER', '5')]
    parser = PPL_Project.Parser(tokens)
    ast = parser.parse()
    print("AST:", ast)  # Should output a valid AST
    interpreter = PPL_Project.Interpreter()
    result = interpreter.interpret(ast)
    print(result)  # Expected output: 8.0


if __name__ == "__main__":
    test_all_functions()
