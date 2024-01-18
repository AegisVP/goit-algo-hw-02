from collections import deque

d = deque()


def is_palyndrom():
    could_be_palyndrom = True
    while could_be_palyndrom:
        if len(d) <= 1:
            return True
        else:
            if d[0] == d[-1]:
                d.popleft()
                d.pop()
            else:
                could_be_palyndrom = False
                break
    return False


def check_string_if_palyndrom(string):
    for i in string:
        d.append(i)
    return is_palyndrom()


if __name__ == '__main__':
    input_string = input('Enter a string: ')
    if (len(input_string) == 0):
        print("no input string provided")
        exit(0)
    print("The string is a palyndrom" if check_string_if_palyndrom(input_string) else "The string in not a palyndrom")
