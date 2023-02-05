#Name: Andrew Lee
#OSU CS 325
#Assignment 4, Problem 1
#Due Date: January 5, 2023

def max_independent_set(nums):
    '''function that takes a given array of numbers and returns the subset of non-consecutive numbers with the biggest
    sum. The function takes inspiration from the Exploration 4.3 coin making problem in that it stores what the number
    was added to the greatest sum and goes back from there. Uses a bottom up approach'''
    condition = False
    for x in nums:                                          #simple test to see if given arr is all negative numbers
        if x >= 0:
            condition = True
    if condition == False:
        return []
    another_condition = False
    for x in nums:                                          #simple test if given arr is neg and zeros
        if x > 0:
            another_condition = True
    if another_condition == False:
        return [0]
    table = []                                              #first memo to keep track of sums. Index of table lines up
                                                            #with index of nums.
    number_used = []                                        #second memo to keep track of what number was added to
                                                            #value in nums to get the biggest sum
    for x in range(len(nums)):
        table.append(nums[x])                               #append values of nums to table so that we can sum up
        number_used.append(x)                               #append index so we can track back numbers and create subset
    for x in range(len(nums)):                              #for loop that goes through every value in nums
        if (x+2) > len(nums)-1:
            pass
        else:
            for y in range((x+2), len(nums)):               #add x to every non-consecutive number in nums
                temporary_result = table[x] + nums[y]       #we add stored sum in table[x] so we eventually sum up numbers
                if temporary_result > table[y]:
                    table[y] = temporary_result             #store the sum if it's bigger
                    number_used[y] = x                      #store index used so we can back track
    result = 0
    for m in range(len(table)):                             #go through table and find the max sum
        if table[m] > result:
            result = m
    actual_result = []
    while result != number_used[result]:                    #go through numbers_used and create subset
        actual_result.insert(0, nums[result])
        result = number_used[result]
    actual_result.insert(0, nums[result])

    return actual_result

