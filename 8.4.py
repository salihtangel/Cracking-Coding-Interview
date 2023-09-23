def all_subsets(my_set):
    n = len(my_set)
    all_subsets_list = []

    for i in range(2**n):
        subset = set()
        for j in range(n):
            if (i >> j) & 1:
                subset.add(list(my_set)[j])
        all_subsets_list.append(subset)
    
    return all_subsets_list

my_set = {'a', 'b', 'c' ,'d', 'e'}

subsets = all_subsets(my_set)

# for subset in subsets:
#     print(subset)

print(list(my_set))[0]