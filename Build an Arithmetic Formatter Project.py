def arithmetic_arranger(problems, show_answers=False):
    # 1. Check the length of the problems list
    if len(problems) > 5:
        return "Error: Too many problems."

    # 2. Check the operator
    operators = []
    for problem in problems:
        array = problem.split()
        operators.append(array[1])

    for operator in operators:
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

    # 3. Check for non-digit numbers
    numbers = []
    for problem in problems:
        array = problem.split()
        numbers.append(array[0])
        numbers.append(array[2])

    for number in numbers:
        if not number.isdigit():
            return 'Error: Numbers must only contain digits.'

    # 4. Check operand length
    for number in numbers:
        if len(number) > 4:
            return 'Error: Numbers cannot be more than four digits.'

    # 5. Evaluation and answer computation
    answers = []
    top_row = ''
    bottom_row = ''
    answer_row = ''
    dashes = ''

    for i in range(len(problems)):
        num1, operator, num2 = problems[i].split()
        num1, num2 = int(num1), int(num2)

        # Perform the operation and calculate result
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2

        # Calculate the space width for formatting
        space_width = max(len(str(num1)), len(str(num2))) + 2

        # Append to the rows
        top_row += str(num1).rjust(space_width)
        bottom_row += operator + str(num2).rjust(space_width - 1)
        dashes += '-' * space_width
        answers.append(result)

        # Add spacing between problems if needed
        if i != len(problems) - 1:
            top_row += '    '
            bottom_row += '    '
            dashes += '    '

    # 6. Format the answers row if needed
    for i in range(len(answers)):
        space_width = max(len(str(numbers[2 * i])), len(str(numbers[2 * i + 1]))) + 2
        answer_row += str(answers[i]).rjust(space_width)

        if i != len(answers) - 1:
            answer_row += '    '

    # 7. Final arrangement and return
    if show_answers:
        arranged_problems = '\n'.join([top_row, bottom_row, dashes, answer_row])
    else:
        arranged_problems = '\n'.join([top_row, bottom_row, dashes])

    return arranged_problems

# Example call to the function
print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
