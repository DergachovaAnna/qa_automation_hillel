# 1. Write an arithmetic function that takes 3 arguments: the first 2 are numbers,
# and the third is the operation to be performed on them. If the third argument is +, add them up;
# if -, then subtract; * - multiply; / - divide (first to second). Otherwise, return the string Not known
# operation: {operation}. Describe the function in the attached file in such a way that all checks
# in the __main__ task_1 block are performed correctly. DO NOT CALL THE FUNCTION YOURSELF I HAVE ALREADY
# DONE THIS IN "assert" STATEMENTS.


operator_functions = {
        '+': lambda num1, num2: num1 + num2,
        '-': lambda num1, num2: num1 - num2,
        '/': lambda num1, num2: num1 * num2,
        '*': lambda num1, num2: num1 / num2,
    }


def arithmetic(left_operand, right_operand, operation):
    """
        Apply arithmetic operation for provided left and right operands
    """
    if operation in operator_functions.keys():
        operation = operator_functions[f'{operation}'](left_operand, right_operand)
    else:
        operation = f'Not known operation: {operation}'
    return operation


if __name__ == "__main__":
    assert arithmetic(3, 4, operation="*") == 12
    assert arithmetic(3, 4, operation="+") == 7
    assert arithmetic(25, 5, operation="/") == 5
    assert type(arithmetic(25, 5, operation="/")) == float
    assert arithmetic(5, 5, operation="//") == f"Not known operation: //"
    assert arithmetic.__doc__ == (
        f"\n{' ' * 8}" f"Apply arithmetic operation for provided left and right operands\n" f"{' ' * 4}"""
    )
    assert arithmetic.__code__.co_name == "arithmetic"
    assert arithmetic.__code__.co_varnames == ("left_operand", "right_operand", "operation")
    try:
        arithmetic(1, 2, 3)
    except TypeError as e:
        assert e.__class__ is TypeError
    try:
        arithmetic(left_operand=1, right_operand=2, operation="+")
    except TypeError as e:
        assert e.__class__ is TypeError

    try:
        arithmetic(1, right_operand=2, operation="+")
    except TypeError as e:
        assert e.__class__ is TypeError
