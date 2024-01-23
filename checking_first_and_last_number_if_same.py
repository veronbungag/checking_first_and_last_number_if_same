#define a function for  list of numbers
def first_last_same(numberList):
    #print given list
    print("Given list:", numberList)
    
    first_number = numberList[0]
    last_number = numberList[-1]
#if first number is equal to last number, return True
    if first_number == last_number:
        return True
#if neither condition above is met, return False
    else:
        return False
#given list set 1
numbers_set1 = [10, 20, 30, 40, 10]
#print result for Set 1
print("result is", first_last_same(numbers_set1))
#given list set 2
numbers_set2 = [75, 65, 35, 75, 30]
#print result for Set 2
print("result is", first_last_same(numbers_set2))