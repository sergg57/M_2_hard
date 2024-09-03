n_list = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for i in range(len(n_list)):
    result_list = []
    result_str = ''
    first = i+1

    for k in range(1, n_list[i]):
        first = k
        for (j) in range(k, n_list[i]):
            if j == k:
                first = k
            else:
                sum = first + j
                if n_list[i] % sum == 0:
                    result_list.append(first)
                    result_str = result_str + str(first)
                    result_list.append(j)
                    result_str = result_str + str(j)

    print(n_list[i], '-', *result_list)
    print(n_list[i], ':', result_str)
