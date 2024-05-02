def sumOfNumbers(num: int):
    if num == 1:
        return num
    return num + sumOfNumbers(num - 1)


if __name__ == '__main__':
    print(sumOfNumbers(5))
