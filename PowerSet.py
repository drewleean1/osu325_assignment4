
def powerset_helper(pointer, choices_made, input, result):
    if pointer >= len(input):
        new_variable = []
        for x in choices_made:
            new_variable.append(x)
        result.append(new_variable)
        return
    choices_made.append(input[pointer])
    powerset_helper(pointer+1, choices_made, input, result)
    choices_made.pop()
    powerset_helper(pointer+1, choices_made, input, result)

def powerset(inputSet):
    result = []
    powerset_helper(0, [], inputSet, result)
    return result

print(powerset([1,2,3]))