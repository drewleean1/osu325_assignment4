#Name: Andrew Lee
#OSU CS 325
#Assignment 4, Problem 2
#Due Date: January 5, 2023

def powerset_helper(pointer, choices_made, input, result):
    '''helper function for power set. Implemented based on the pseudocode in Exploration 4.4 '''
    if pointer >= len(input):                                       #base case
        new_variable = []                                           #creating a local var to append. prob a better way to do this
        for x in choices_made:
            new_variable.append(x)
        result.append(new_variable)
        return
    choices_made.append(input[pointer])
    powerset_helper(pointer+1, choices_made, input, result)         #iterating pointer up
    choices_made.pop()
    powerset_helper(pointer+1, choices_made, input, result)

def powerset(inputSet):
    '''function that takes an array of numbers and returns its powerset. Difference from pseudocode in the exploration is
    starting the pointer from 0 and iterating up'''
    result = []
    powerset_helper(0, [], inputSet, result)
    return result

print(powerset([1,2,3]))