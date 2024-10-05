def find_the_password(figure):
    password = ''
    for i in range(1, figure):
        for j in range(2, figure):
            if j <= i:
                continue
            if figure % ( i + j) == 0:
                password += str(i) + str(j)
    return password
numbers = int(input('Запишите число от 3 до 20: '))
print('Код:', find_the_password(numbers))

