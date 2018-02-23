# Simple method that will define a methods and how to call it

list_nums = [1,2,3,4,5]

def average(list_of_nums):
    # variable average that would be returned
    average = 0

    # calculate our average
    for i in range(0, len(list_nums)):
        average = average + list_nums[i]

    average = average / len(list_nums)
    return average

def lowMidHigh(list_of_nums, low=1, high=4):
    print("---------- Low numbers-----------")
    for i in range(0, len(list_of_nums)):
        if (list_of_nums[i] < low):
            print(list_of_nums[i])

    print("---------- mid numbers-----------")
    for i in range(0, len(list_of_nums)):
        if (list_of_nums[i] > low and list_of_nums[i] < high):
            print(list_of_nums[i])

    print("---------- high numbers-----------")
    for i in range(0, len(list_of_nums)):
        if (list_of_nums[i] >= high):
            print(list_of_nums[i])

print('Average')
print(average(list_nums))
print(lowMidHigh(list_nums, 2, 3))
lowMidHigh(list_nums, 2, 3)
