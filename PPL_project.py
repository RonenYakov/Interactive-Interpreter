# ---------------------------------------------------------------------------
#                           Math
# ---------------------------------------------------------------------------
def add(z, y):
    """
    Adds two numbers.

    Parameters:
    z (int, float): The first number.
    y (int, float): The second number.

    Returns:
    int, float: The sum of z and y.
    """
    return z + y


def subtract(z, y):
    """
    Subtracts the second number from the first number.

    Parameters:
    z (int, float): The first number.
    y (int, float): The second number.

    Returns:
    int, float: The difference of z and y.
    """
    return z - y


def multiply(z, y):
    """
    Multiplies two numbers.

    Parameters:
    z (int, float): The first number.
    y (int, float): The second number.

    Returns:
    int, float: The product of z and y.
     """
    return z * y


def divide(z, y):
    """
    Divides the first number by the second number.

    Parameters:
    z (int, float): The dividend.
    y (int, float): The divisor.

    Raises:
    ZeroDivisionError: If y is zero.

    Returns:
    int, float: The quotient of z and y.
    """
    if y == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return z / y


def power(z, y):
    """
    Raises the first number to the power of the second number.

    Parameters:
    z (int, float): The base.
    y (int, float): The exponent.

    Returns:
    int, float: z raised to the power of y.
    """
    return z ** y


def square(z):
    """
    Returns the square root of the number.

    Parameters:
    z (int, float): The number.

    Returns:
    float: The square root of z.
    """
    return z ** 0.5


def Max(z, y):
    """
    Returns the maximum of two numbers.

    Parameters:
    x (int, float): The first number.
    y (int, float): The second number.

    Returns:
    int, float: The maximum of x and y.
    """
    if z > y:
        return z
    return y


def Min(z, y):
    """
    Returns the minimum of two numbers.

    Parameters:
    x (int, float): The first number.
    y (int, float): The second number.

    Returns:
    int, float: The minimum of x and y.
    """
    if z < y:
        return z
    return y


def mod(z, y):
    """
    Returns the remainder when the first number is divided by the second number.

    Parameters:
    x (int, float): The dividend.
    y (int, float): The divisor.

    Raises:
    ZeroDivisionError: If y is zero.

    Returns:
    int: The remainder of x divided by y.
    """
    if y == 0:
        raise ZeroDivisionError("Modulo by zero is not allowed")
    return z % y


def assign(x, y):
    """
    Assigns the value of y to x.

    Parameters:
    x (any): The variable to be assigned.
    y (any): The value to assign.

    Returns:
    any: The value y.
    """
    return y


def equal(z, y):
    """
    Checks if two values are equal.

    Parameters:
    z (any): The first value.
    y (any): The second value.

    Returns:
    bool: True if z equals y, otherwise False.
    """
    return z == y


def not_equal(z, y):
    """
    Checks if two values are not equal.

    Parameters:
    z (any): The first value.
    y (any): The second value.

    Returns:
    bool: True if z does not equal y, otherwise False.
    """
    return z != y


def greater_than(z, y):
    """
    Checks if the first value is greater than the second value.

    Parameters:
    z (int, float): The first value.
    y (int, float): The second value.

    Returns:
    bool: True if z is greater than y, otherwise False.
    """
    return z > y


def less_than(z, y):
    """
    Checks if the first value is less than the second value.

    Parameters:
    z (int, float): The first value.
    y (int, float): The second value.

    Returns:
    bool: True if z is less than y, otherwise False.
    """
    return z < y


def greater_than_equal(z, y):
    """
    Checks if the first value is greater than or equal to the second value.

    Parameters:
    z (int, float): The first value.
    y (int, float): The second value.

    Returns:
    bool: True if z is greater than or equal to y, otherwise False.
    """
    return z >= y


def less_than_equal(z, y):
    """
    Checks if the first value is less than or equal to the second value.

    Parameters:
    z (int, float): The first value.
    y (int, float): The second value.

    Returns:
    bool: True if z is less than or equal to y, otherwise False.
    """
    return z <= y


# Logical Operations
def logical_or(z, y):
    """
    Performs a logical OR operation between two boolean values.

    Parameters:
    z (bool): The first boolean value.
    y (bool): The second boolean value.

    Returns:
    bool: The result of the logical OR operation.
    """
    return z or y


def logical_and(z, y):
    """
    Performs a logical AND operation between two boolean values.

    Parameters:
    z (bool): The first boolean value.
    y (bool): The second boolean value.

    Returns:
    bool: The result of the logical AND operation.
    """
    return z and y


# Creating a dictionary of functions to have a more organized access to the operations
operations = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
    "power": power,
    "square": square,
    "max": Max,
    "min": Min,
    "mod": mod,
    "assign": assign,
    "equal": equal,
    "not_equal": not_equal,
    "greater_than": greater_than,
    "less_than": less_than,
    "greater_than_equal": greater_than_equal,
    "less_than_equal": less_than_equal,
    "logical_or": logical_or,
    "logical_and": logical_and,
}


# ---------------------------------------------------------------------------
#                           IF ELSE IF-ELSE
# ---------------------------------------------------------------------------
def custom_if(my_condition, true_value, false_value):
    """
    Custom implementation of an if statement.

    Parameters:
    my_condition (bool): The condition to evaluate.
    true_value (function): The function to execute if the condition is True.
    false_value (function): The function to execute if the condition is False.

    Returns:
    The result of true_value() if my_condition is True, otherwise the result of false_value().
    """
    return (my_condition and true_value()) or false_value()


def custom_else(my_condition, true_value, false_value):
    """
    Custom implementation of an else statement.

    Parameters:
    my_condition (bool): The condition to evaluate.
    true_value (function): The function to execute if the condition is False.
    false_value (function): The function to execute if the condition is True.

    Returns:
    The result of false_value() if my_condition is False, otherwise the result of true_value().
    """
    return (not my_condition and false_value()) or true_value()


def custom_ifElse(my_condition, true_value, false_value):
    """
    Custom implementation of an if-else statement.

    Parameters:
    my_condition (bool): The condition to evaluate.
    true_value (function): The function to execute if the condition is True.
    false_value (function): The function to execute if the condition is False.

    Returns:
    The result of true_value() if my_condition is True, otherwise the result of false_value().
    """
    return custom_if(my_condition, true_value, lambda: custom_else(my_condition, true_value, false_value))


def check_types(operation_name, *args):
    """
    Checks the types of the arguments passed to an operation.

    Parameters:
    operation_name (str): The name of the operation.
    *args: The arguments to check.

    Returns:
    bool: True if the argument types are correct, otherwise False.
    """
    if operation_name in {"add", "subtract", "multiply", "divide", "power", "max", "min", "mod"}:
        return all(isinstance(arg, int) for arg in args)
    elif operation_name in {"equal", "not_equal", "greater_than",
                            "less_than", "greater_than_equal", "less_than_equal"}:
        return all(isinstance(arg, int) for arg in args)
    elif operation_name in {"logical_or", "logical_and"}:
        return all(isinstance(arg, bool) for arg in args)
    elif operation_name == "square":
        return isinstance(args[0], int)
    return False


def call_operation(operation_name, *args):
    """
    Calls an operation by name with the provided arguments.

    Parameters:
    operation_name (str): The name of the operation.
    *args: The arguments to pass to the operation.

    Returns:
    The result of the operation, or an error message if an error occurs.
    """
    try:
        # Check if the function exists
        if operation_name not in operations:
            return f"Error: Operation '{operation_name}' not found."

        # Check if the arguments are of the correct type
        if not check_types(operation_name, *args):
            return f"Error: Incorrect argument types for operation '{operation_name}'."

        # Attempt to call the function with the provided arguments
        result = operations[operation_name](*args)
        return result
    except TypeError as te:
        return f"Error: {te}"
    except ZeroDivisionError as zde:
        return f"Error: {zde}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"


def is_positive():
    print("Checking if positive...")
    return "Number is positive"


def is_negative():
    print("Checking if negative...")
    return "Number is negative"


def is_zero():
    print("Checking if zero...")
    return "Number is zero"


# ---------------------------------------------------------------------------
#                       LOOPS
# ---------------------------------------------------------------------------
def custom_while(condition_func, action_func):
    """
    Custom implementation of a while loop.

    Parameters:
    condition_func (function): A function that returns a boolean value.
    action_func (function): A function that contains the action to perform while the condition is true.
    """
    if condition_func():
        action_func()
        custom_while(condition_func, action_func)


def custom_for(iterable, action_func, index=0):
    """
    Custom implementation of a for loop.

    Parameters:
    iterable (iterable): The iterable to loop over.
    action_func (function): A function that contains the action to perform on each item.
    index (int, optional): The starting index for the loop. Defaults to 0.
    """
    if index < len(iterable):
        action_func(iterable[index])
        custom_for(iterable, action_func, index + 1)


# ---------------------------------------------------------------------------
#                           class CustomString
# ---------------------------------------------------------------------------
class CustomString:
    """
    A custom string class that provides string manipulation methods.
    """

    def __init__(self, value):
        """
        Initializes a CustomString object.

        Parameters:
        value (str): The string value.
        """
        self.value = value

    def split(self, delimiter=" "):
        """
        Splits the string by the given delimiter.

        Parameters:
        delimiter (str, optional): The delimiter to split by. Defaults to a space.

        Returns:
        list: A list of substrings.
        """
        return self.value.split(delimiter)

    def replace(self, old, new):
        """
        Replaces occurrences of a substring with a new substring.

        Parameters:
        old (str): The substring to replace.
        new (str): The substring to replace with.

        Returns:
        str: The string with the replaced values.
        """
        result = ""
        i = 0
        while i < len(self.value):
            if self.value[i:i + len(old)] == old:
                result += new
                i += len(old)
            else:
                result += self.value[i]
                i += 1
        return result

    def isUpper(self):
        """
        Checks if all characters in the string are uppercase.

        Returns:
        bool: True if all characters are uppercase, otherwise False.
        """
        for char in self.value:
            if 'a' <= char <= 'z':  # Check if the character is a lowercase letter
                return False
        return True

    def isLower(self):
        """
        Checks if all characters in the string are lowercase.

        Returns:
        bool: True if all characters are lowercase, otherwise False.
        """
        for char in self.value:
            if 'A' <= char <= 'Z':  # Check if the character is an uppercase letter
                return False
        return True

    def concat(self, other):
        """
        Concatenates the current string with another CustomString object.

        Parameters:
        other (CustomString): The other CustomString object.

        Returns:
        str: The concatenated string.
        """
        result = ""
        for char in self.value:
            result += char
        for char in other.value:
            result += char
        return result


# ---------------------------------------------------------------------------
#                           class CustomTuple
# ---------------------------------------------------------------------------
class CustomTuple:
    """
    A custom tuple class that provides tuple manipulation methods.
    """

    def __init__(self, *values):
        """
        Initializes a CustomTuple object.

        Parameters:
        *values: The values to be stored in the tuple.
        """
        self.values = tuple(values)

    def sequence(self):
        """
        Returns the values in the tuple as a list.

        Returns:
        list: A list of the values in the tuple.
        """
        return [value for value in self.values]

    def sort(self):
        """
        Sorts the values in the tuple.

        Returns:
        tuple: A tuple with the sorted values.
        """
        sorted_values = list(self.values)  # Convert tuple to list for sorting
        n = len(sorted_values)
        for i in range(n):
            for j in range(0, n - i - 1):
                if sorted_values[j] > sorted_values[j + 1]:
                    # Swap if the element found is greater than the next element
                    sorted_values[j], sorted_values[j + 1] = sorted_values[j + 1], sorted_values[j]
        return tuple(sorted_values)

    def __add__(self, other):
        """
        Concatenates two CustomTuple objects.

        Parameters:
        other (CustomTuple): The other CustomTuple object.

        Returns:
        CustomTuple: A new CustomTuple containing the concatenated values.
        """
        combined_values = []
        for value in self.values:
            combined_values.append(value)
        for value in other.values:
            combined_values.append(value)
        return CustomTuple(*combined_values)

    def getItem(self, index):
        """
        Returns the value at the specified index.

        Parameters:
        index (int): The index of the value to retrieve.

        Raises:
        IndexError: If the index is out of bounds.

        Returns:
        any: The value at the specified index.
        """
        if index < -self.length() or index >= self.length():
            raise IndexError("Index out of bounds")
        return self.values[index]

    def index(self, value):
        """
        Returns the index of the first occurrence of a value.

        Parameters:
        value (any): The value to search for.

        Raises:
        ValueError: If the value is not found.

        Returns:
        int: The index of the value.
        """
        for i in range(self.length()):
            if self.values[i] == value:
                return i
        raise ValueError(f"{value} is not in CustomTuple")

    def length(self):
        """
        Returns the length of the tuple.

        Returns:
        int: The number of elements in the tuple.
        """
        my_count = 0
        for _ in self.values:
            my_count += 1
        return my_count


# ---------------------------------------------------------------------------
#                           class Array
# ---------------------------------------------------------------------------
class Array:
    """
    A custom array class that provides array manipulation methods.
    """

    def __init__(self, *args):
        """
        Initializes an Array object.

        Parameters:
        *args: The elements to be stored in the array.
        """
        self.items = list(args)
        self.size = len(self.items)

    def append(self, value):
        """
        Appends a value to the end of the array.

        Parameters:
        value (any): The value to append.

        Returns:
        Array: The array with the appended value.
        """
        self.items[self.size:self.size] = [value]
        self.size += 1
        return self

    def __len__(self):
        """
        Returns the length of the array.

        Returns:
        int: The number of elements in the array.
        """
        return self.size

    def index(self, value):
        """
        Returns the index of the first occurrence of a value.

        Parameters:
        value (any): The value to search for.

        Raises:
        ValueError: If the value is not found.

        Returns:
        int: The index of the value.
        """
        for i in range(self.size):
            if self.items[i] == value:
                return i
        else:
            raise ValueError(f"{value} is not in the array")

    # array(i)
    def find(self, index):
        """
        Returns the value at the specified index.

        Parameters:
        index (int): The index of the value to retrieve.

        Raises:
        IndexError: If the index is out of range.

        Returns:
        any: The value at the specified index.
        """
        if 0 <= index < self.size:
            return self.items[index]
        else:
            raise IndexError("Index out of range")

    def add(self, value, index):
        """
        Adds a value at a specific index in the array.

        Parameters:
        value (any): The value to add.
        index (int): The index at which to add the value.

        Raises:
        IndexError: If the index is out of range.

        Returns:
        Array: The array with the added value.
        """
        if 0 <= index <= self.size:
            self.items = self.items[:index] + [value] + self.items[index:]
            self.size += 1
        else:
            raise IndexError("Index out of range")
        return self

    # removing the value in index 'index'
    def remove(self, index):
        """
        Removes the value at a specific index in the array.

        Parameters:
        index (int): The index of the value to remove.

        Raises:
        IndexError: If the index is out of range.

        Returns:
        Array: The array with the value removed.
        """
        if 0 <= index < self.size:  # Index should be within range
            # Create a new list without the element at the specified index
            self.items = self.items[:index] + self.items[index + 1:]
            self.size -= 1
        else:
            raise IndexError("Index out of range")
        return self


# ---------------------------------------------------------------------------
#                               class Lexer
# ---------------------------------------------------------------------------
class Lexer:
    """
    A lexer class for tokenizing input text.
    """

    def __init__(self, input_text):
        """
        Initializes a Lexer object.

        Parameters:
        input_text (str): The input text to tokenize.
        """
        self.input_text = input_text
        self.position = 0
        self.tokens = []
        self.current_char = self.input_text[self.position]

    def advance(self):
        """
        Moves to the next character in the input text.
        """
        self.position += 1
        if self.position < len(self.input_text):
            self.current_char = self.input_text[self.position]
        else:
            self.current_char = None  # Indicates end of input

    def create_tokens(self):
        """
        Tokenizes the input text.

        Returns:
        list: A list of tokens.
        """
        while self.current_char is not None:
            if self.current_char.isspace():
                self.advance()  # Ignore whitespace
            elif self.current_char.isdigit():
                self.tokens.append(self.number())
            elif self.current_char.isalpha():
                self.tokens.append(self.identifier())
            elif self.current_char == '+':
                self.tokens.append(('PLUS', '+'))
                self.advance()
            elif self.current_char == '-':
                self.tokens.append(('MINUS', '-'))
                self.advance()
            elif self.current_char == '*':
                self.tokens.append(('MULTIPLY', '*'))
                self.advance()
            elif self.current_char == '/':
                self.tokens.append(('DIVIDE', '/'))
                self.advance()
            elif self.current_char == '=':
                self.tokens.append(('ASSIGN', '='))
                self.advance()
            else:
                raise ValueError(f"Unexpected character: {self.current_char}")
        return self.tokens

    def number(self):
        """
        Handles numeric tokens.

        Returns:
        tuple: A tuple containing the token type 'NUMBER' and the integer value.
        """
        num_str = ''
        while self.current_char is not None and self.current_char.isdigit():
            num_str += self.current_char
            self.advance()
        return 'NUMBER', int(num_str)

    def identifier(self):
        """
        Handles identifier tokens.

        Returns:
        tuple: A tuple containing the token type 'IDENTIFIER' and the identifier string.
        """
        id_str = ''
        while self.current_char is not None and self.current_char.isalnum():
            id_str += self.current_char
            self.advance()
        return 'IDENTIFIER', id_str


# ---------------------------------------------------------------------------
#                               class Parser
# ---------------------------------------------------------------------------
class Parser:
    """
    A parser class for constructing an abstract syntax tree (AST) from tokens.
    """

    def __init__(self, my_tokens):
        """
        Initializes a Parser object.

        Parameters:
        my_tokens (list): The list of tokens to parse.
        """
        self.tokens = my_tokens
        self.current_token = None
        self.pos = -1
        self.advance()

    def advance(self):
        """
        Advances to the next token.
        """
        self.pos += 1
        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]
        else:
            self.current_token = None

    def parse(self):
        """
        Parses the tokens into an abstract syntax tree (AST).

        Returns:
        tuple: The AST representing the expression.
        """
        if self.current_token:
            return self.expr()
        return None

    def factor(self):
        """
        Parses a factor in the expression.

        Returns:
        tuple: The AST node for the factor.
        """
        token = self.current_token
        if token[0] == 'NUMBER':
            self.advance()
            return 'NUMBER', token[1]
        elif token[0] == 'LPAREN':
            self.advance()
            my_result = self.expr()
            if self.current_token and self.current_token[0] == 'RPAREN':
                self.advance()
                return my_result
        return None

    def term(self):
        """
        Parses a term in the expression.

        Returns:
        tuple: The AST node for the term.
        """
        my_result = self.factor()
        while self.current_token and self.current_token[0] == 'OP' and self.current_token[1] in '*/':
            op = self.current_token
            self.advance()
            my_result = (op[1], my_result, self.factor())
        return my_result

    def expr(self):
        """
        Parses an expression.

        Returns:
        tuple: The AST node for the expression.
        """
        my_result = self.term()
        while self.current_token and self.current_token[0] == 'OP' and self.current_token[1] in '+-':
            op = self.current_token
            self.advance()
            my_result = (op[1], my_result, self.term())
        return my_result


# ---------------------------------------------------------------------------
#                           class Interpreter
# ---------------------------------------------------------------------------
class Interpreter:
    """
    An interpreter class for evaluating an abstract syntax tree (AST).
    """

    def __init__(self):
        """
        Initializes an Interpreter object.
         """
        pass

    def visit(self, node):
        """
        Visits an AST node and evaluates it.

        Parameters:
        node (tuple): The AST node to evaluate.

        Returns:
        float: The result of evaluating the AST node.
        """
        if isinstance(node, tuple):
            operator = node[0]
            if operator == '+':
                return self.visit(node[1]) + self.visit(node[2])
            elif operator == '-':
                return self.visit(node[1]) - self.visit(node[2])
            elif operator == '*':
                return self.visit(node[1]) * self.visit(node[2])
            elif operator == '/':
                right = self.visit(node[2])
                if right == 0:
                    raise ZeroDivisionError("Division by zero is not allowed")
                return self.visit(node[1]) / right
            elif operator == 'NUMBER':
                return float(node[1])
            else:
                raise ValueError(f"Unknown operator {operator}")
        elif isinstance(node, float) or isinstance(node, int):
            return node
        elif isinstance(node, str):
            return float(node)
        else:
            raise TypeError(f"Unsupported type in AST: {type(node)}")

    def interpret(self, ast):
        """
        Interprets and evaluates an abstract syntax tree (AST).

        Parameters:
        ast (tuple): The AST to evaluate.

        Returns:
        float: The result of evaluating the AST.
        """
        if ast is None:
            raise ValueError("AST is None")
        return self.visit(ast)


def main():
    # Dictionary to store variables of different types
    variables = {
        'strings': {},  # For CustomString objects
        'tuples': {},  # For CustomTuple objects
        'arrays': {},  # For Array objects
        'numbers': {}  # For numeric values (original)
    }

    def print_help():
        """Prints available commands and their usage."""
        print("\nAvailable Commands:")
        print("1. Basic Operations:")
        print("   - add/subtract/multiply/divide/power/mod <arg1> <arg2>")
        print("   - square <number>")
        print("   - max/min <arg1> <arg2>")
        print("2. Comparison Operations:")
        print("   - equal/not_equal/greater_than/less_than/greater_than_equal/less_than_equal <arg1> <arg2>")
        print("3. Logical Operations:")
        print("   - logical_and/logical_or <bool1> <bool2>")
        print("4. Variable Operations:")
        print("   - assign <variable_name> <value>")
        print("   - string_assign <variable_name> <string_value>")
        print("   - tuple_assign <variable_name> <value1> <value2> ...")
        print("   - array_assign <variable_name> <value1> <value2> ...")
        print("5. String Operations:")
        print("   - string_split <string_var> [delimiter]")
        print("   - string_replace <string_var> <old> <new>")
        print("   - string_isUpper <string_var>")
        print("   - string_isLower <string_var>")
        print("   - string_concat <string_var1> <string_var2>")
        print("6. Tuple Operations:")
        print("   - tuple_sort <tuple_var>")
        print("   - tuple_length <tuple_var>")
        print("   - tuple_index <tuple_var> <value>")
        print("   - tuple_get <tuple_var> <index>")
        print("7. Array Operations:")
        print("   - array_append <array_var> <value>")
        print("   - array_add <array_var> <value> <index>")
        print("   - array_remove <array_var> <index>")
        print("   - array_find <array_var> <index>")
        print("8. Utility Commands:")
        print("   - print <variable_name>")
        print("   - help")
        print("   - quit")

    while True:
        try:
            user_input = input("Enter a command (or 'help' for commands list): ").strip()

            if user_input.lower() == 'quit':
                print("Exiting the program. Goodbye!")
                break

            if user_input.lower() == 'help':
                print_help()
                continue

            # Split the input into parts
            parts = user_input.split()
            if len(parts) < 2:
                print("Invalid input. Please use the format: <operation> <arguments>")
                continue

            operation = parts[0].lower()
            args = parts[1:]

            # Handle string operations
            if operation.startswith('string_'):
                if operation == 'string_assign':
                    if len(args) < 2:
                        print("Invalid string assignment. Use: string_assign <variable> <value>")
                        continue
                    var_name = args[0]
                    string_value = ' '.join(args[1:])
                    variables['strings'][var_name] = CustomString(string_value)
                    print(f"Assigned string '{string_value}' to {var_name}")

                elif operation == 'string_split':
                    if len(args) < 1:
                        print("Invalid split operation. Use: string_split <variable> [delimiter]")
                        continue
                    var_name = args[0]
                    delimiter = args[1] if len(args) > 1 else " "
                    if var_name in variables['strings']:
                        result = variables['strings'][var_name].split(delimiter)
                        print(f"Split result: {result}")
                    else:
                        print(f"String variable {var_name} not found")

                elif operation == 'string_replace':
                    if len(args) < 3:
                        print("Invalid replace operation. Use: string_replace <variable> <old> <new>")
                        continue
                    var_name, old, new = args[0], args[1], args[2]
                    if var_name in variables['strings']:
                        result = variables['strings'][var_name].replace(old, new)
                        print(f"Replace result: {result}")
                    else:
                        print(f"String variable {var_name} not found")

                elif operation in ['string_isupper', 'string_islower']:
                    if len(args) < 1:
                        print(f"Invalid operation. Use: {operation} <variable>")
                        continue
                    var_name = args[0]
                    if var_name in variables['strings']:
                        if operation == 'string_isupper':
                            result = variables['strings'][var_name].isUpper()
                        else:
                            result = variables['strings'][var_name].isLower()
                        print(f"Result: {result}")
                    else:
                        print(f"String variable {var_name} not found")

            # Handle tuple operations
            elif operation.startswith('tuple_'):
                if operation == 'tuple_assign':
                    if len(args) < 2:
                        print("Invalid tuple assignment. Use: tuple_assign <variable> <value1> <value2> ...")
                        continue
                    var_name = args[0]
                    values = [int(x) for x in args[1:]]
                    variables['tuples'][var_name] = CustomTuple(*values)
                    print(f"Assigned tuple {values} to {var_name}")

                elif operation == 'tuple_sort':
                    if len(args) < 1:
                        print("Invalid sort operation. Use: tuple_sort <variable>")
                        continue
                    var_name = args[0]
                    if var_name in variables['tuples']:
                        result = variables['tuples'][var_name].sort()
                        print(f"Sorted tuple: {result}")
                    else:
                        print(f"Tuple variable {var_name} not found")

                elif operation == 'tuple_length':
                    if len(args) < 1:
                        print("Invalid length operation. Use: tuple_length <variable>")
                        continue
                    var_name = args[0]
                    if var_name in variables['tuples']:
                        result = variables['tuples'][var_name].length()
                        print(f"Length: {result}")
                    else:
                        print(f"Tuple variable {var_name} not found")

            # Handle array operations
            elif operation.startswith('array_'):
                if operation == 'array_assign':
                    if len(args) < 2:
                        print("Invalid array assignment. Use: array_assign <variable> <value1> <value2> ...")
                        continue
                    var_name = args[0]
                    values = [int(x) for x in args[1:]]
                    variables['arrays'][var_name] = Array(*values)
                    print(f"Assigned array {values} to {var_name}")

                elif operation == 'array_append':
                    if len(args) < 2:
                        print("Invalid append operation. Use: array_append <variable> <value>")
                        continue
                    var_name, value = args[0], int(args[1])
                    if var_name in variables['arrays']:
                        variables['arrays'][var_name].append(value)
                        print(f"Appended {value} to array {var_name}")
                    else:
                        print(f"Array variable {var_name} not found")

                elif operation == 'array_remove':
                    if len(args) < 2:
                        print("Invalid remove operation. Use: array_remove <variable> <index>")
                        continue
                    var_name, index = args[0], int(args[1])
                    if var_name in variables['arrays']:
                        variables['arrays'][var_name].remove(index)
                        print(f"Removed element at index {index} from array {var_name}")
                    else:
                        print(f"Array variable {var_name} not found")

            # Handle original numeric operations
            elif operation == "assign":
                if len(args) != 2:
                    print("Invalid assignment. Use: assign <variable> <value>")
                    continue
                var_name, value = args
                try:
                    value = int(value)
                    variables['numbers'][var_name] = value
                    print(f"Assigned {value} to {var_name}")
                except ValueError:
                    print("Invalid value. Please enter an integer.")

            elif operation in operations:
                try:
                    # Convert arguments to integers, replacing variable names with their values
                    int_args = []
                    for arg in args:
                        if arg in variables['numbers']:
                            int_args.append(variables['numbers'][arg])
                        else:
                            int_args.append(int(arg))

                    result = call_operation(operation, *int_args)
                    print(f"Result: {result}")
                except ValueError:
                    print("Invalid arguments. Please enter integers or valid variable names.")
                except Exception as e:
                    print(f"Error: {e}")

            elif operation == "print":
                if len(args) != 1:
                    print("Invalid print command. Use: print <variable>")
                    continue
                var_name = args[0]

                # Check in all variable dictionaries
                if var_name in variables['numbers']:
                    print(f"{var_name} = {variables['numbers'][var_name]}")
                elif var_name in variables['strings']:
                    print(f"{var_name} = {variables['strings'][var_name].value}")
                elif var_name in variables['tuples']:
                    print(f"{var_name} = {variables['tuples'][var_name].values}")
                elif var_name in variables['arrays']:
                    print(f"{var_name} = {variables['arrays'][var_name].items}")
                else:
                    print(f"Variable {var_name} not found.")

            else:
                print(f"Unknown operation: {operation}")

        except Exception as e:
            print(f"Error: {e}")
            print("Please try again or type 'help' for available commands.")


if __name__ == "__main__":
    main()
