N = int(input())
M = int(input())
movement_digits = {0, 3, 6, 9, 12}

is_movement_digit = [False] * 13
for digit in movement_digits:
    is_movement_digit[digit] = True

result = 0
for _ in range(N):
    number = int(input())
    count = 0
    if number == 0:
        if is_movement_digit[0]:
            count = 1
    else:
        while number > 0:
            digit = number % 13
            if is_movement_digit[digit]:
                count += 1
            number //= 13
    if count <= M:
        result += 1

print(result)