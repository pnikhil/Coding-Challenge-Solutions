#Given a year, return the century it is in

def centuryFromYear(year):
    if year % 100 ==0:
        return year//100
    else:
        return (year)//100 + 1
		
#Check Palindrome

def checkPalindrome(inputString):
    return inputString == inputString[::-1]
	
#Adjacent Element product

def adjacentElementsProduct(inputArray):
    largest = inputArray[0] * inputArray[1]
    new_sum = 0
    for i in range(1,len(inputArray)):
        if i < len(inputArray) - 1:
            new_sum = inputArray[i] * inputArray[i+1]
            if new_sum > largest:
                largest = new_sum
                print(largest)
    return largest

#ShapeArea

def shapeArea(n):
    return pow(n,2) + ((n-1) * (n-1))
	
#Make Array consecutive 2

def makeArrayConsecutive2(statues):
    statues.sort()
    return len(list(range(statues[0],statues[-1]+1))) - len(statues)
	

#Almost increasing sequence

def check_if_ordered(temp_arr):
    # prev = temp_arr[0]
    # for element in temp_arr[1:]:
    #     if element > prev:
    #         prev = element
    #         continue
    #     else:
    #         return False
    # return True
    return all(x < y for x, y in zip(temp_arr, temp_arr[1:]))

arr = [1, 2, 5, 3, 5]
for i in range(0,len(arr)-1):
    temp_arr = arr[:i] + arr[i+1:]
    print(temp_arr)
    status = check_if_ordered(temp_arr)
    if status == True:
        break
print(status)