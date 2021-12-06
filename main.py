starting_num = int(input("Enter the starting number:"))
desired_num = int(input("Enter the desired number:"))


def is_even(n):
    return n % 2 == 0


def calc(starting_num, desired_num):
    steps = 0
    food = 0
    total = starting_num
    running = True
    while running:
        steps += 1
        old = total
        if is_even(total):
            total += total/2
        elif not is_even(total):
            total += (total-1)/2

        food += 2*(total-old)

        if total >= desired_num:
            running = False
            return steps, food


steps, food = calc(starting_num, desired_num)
print("Number of steps:", steps)
print("Amount of food:", int(food))