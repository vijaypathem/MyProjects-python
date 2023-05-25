#the numbers list
nums_list = [0,1,2,3,4,5,6,7,8,9]

#key value to find
key = int(input())

#linear search method will take two parameters numbers list and key.
def linear_search(nums_list, key):
    for i in range(len(nums_list)):
        if nums_list[i]==key:
            return f'The number found at position {i}'
    return 'not found'

result = linear_search(nums_list,key)

print(result)
