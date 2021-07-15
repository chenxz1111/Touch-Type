def med(str1, str2):
    assert(isinstance(str1, str))
    assert(isinstance(str2, str))
    m = len(str1)
    n = len(str2)
    matrix = [0 for i in range(2 * (n + 1))]
    for j in range(n + 1):
        matrix[j] = j
    for i in range(1, m + 1):
        for j in range(n + 1):
            if j == 0:
                matrix[j + n + 1] = i
            elif str1[i - 1] == str2[j - 1]:
                matrix[j + n + 1] = matrix[j - 1]
            else:
                matrix[j + n + 1] = min(matrix[j + n], matrix[j - 1]) + 1
        for j in range(n + 1):
            matrix[j] = matrix[j + n + 1]
    return matrix[n]

if __name__ == '__main__':
    pass