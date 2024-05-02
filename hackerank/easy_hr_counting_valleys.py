def countingValleys(steps, path):
    # Write your code here
    level = 0
    valleys = 0
    for i in range(0, steps):
        if path[i] == 'D':
            level -= 1
        else:
            level += 1
            if level == 0 and i != 0:
                valleys += 1
    return valleys


if __name__ == '__main__':
    print(countingValleys(8, 'UDDDUDUU'))
