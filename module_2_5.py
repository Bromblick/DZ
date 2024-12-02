def get_matrix (n, m, value):
    matrix = []
    for i in range(n):
        list_ = []
        for j in range(m):
            if value >=1:
                list_.append(value)
            else:
                list_.append([])
        matrix.append(list_)
    return matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)


