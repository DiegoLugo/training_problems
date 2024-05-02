def marsExploration(s):
    changed_chars = 0
    for i in range(0, len(s)):
        if i % 3 == 2 or i % 3 == 0:
            if s[i] != 'S':
                changed_chars += 1
        else:
            if s[i] != 'O':
                changed_chars += 1
    return changed_chars


if __name__ == '__main__':
    print(marsExploration("SOSSPSSQSSOR"))
    print(marsExploration("SOSSOSSOS"))
