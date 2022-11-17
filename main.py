def print_evergreen_part(lines):
    for i in range(lines -1):
        print(" ", end='')
    print('/\\', end='')
    for i in range(lines -1):
        print(" ", end='')

    print('')

    for index in range(1, lines):
        for i in range(lines - index - 1):
            print(' ', end='')
        print('/', end='')
        for i in range(index*2):
            print(' ', end='')
        print('\\')

print_evergreen_part(3)
print_evergreen_part(3)
print_evergreen_part(3)



