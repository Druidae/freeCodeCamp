def arithmetic_arranger(problems, show_answer=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        operands = problem.split()
        if len(operands[0]) > 4 or len(operands[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        if not operands[0].isdigit() or not operands[2].isdigit():
            return "Error: Numbers must only contain digits."
        if operands[1] not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

    first_line = ""
    second_line = ""
    separator = ""
    answer_line = ""

    for problem in problems:
        operands = problem.split()
        operand1 = int(operands[0])
        operator = operands[1]
        operand2 = int(operands[2])
        result = 0

        if operator == "+":
            result = operand1 + operand2
        elif operator == "-":
            result = operand1 - operand2

        max_length = max(len(operands[0]), len(operands[2])) + 2
        first_line += str(operand1).rjust(max_length) + "    "
        second_line += operator + str(operand2).rjust(max_length - 1) + "    "
        separator += "-" * max_length + "    "

        if show_answer:
            answer_line += str(result).rjust(max_length) + "    "

    arranged_problems = first_line.rstrip() + "\n" + second_line.rstrip() + "\n" + separator.rstrip()

    if show_answer:
        arranged_problems += "\n" + answer_line.rstrip()

    return arranged_problems
