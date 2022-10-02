def find_lists_min_sumValue(num_list):
    print(min(num_list, key=sum))

num_list = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
find_lists_min_sumValue(num_list)

