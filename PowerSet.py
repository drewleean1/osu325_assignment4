def powerset(inputSet):
    def powerset_helper(pointer, choices_made, input, result):
        if (pointer < 0)):
            append
        choices_made
        to
        results  # make a deep copy since we are working with objects
        return

        append
        input[pointer]
        to
        choices_made
        powerset_helper(pointer - 1, choices_made, input, result)
        # backtracking
        remove
        last
        element
        added
        to
        choices_made
        powerset_helper(pointer - 1, choices_made, input, result)

    def powerset(input):
        result = []
        powerset_helper(len(input) - 1, [], input, result)
        return result
