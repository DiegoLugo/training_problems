def pangrams(s):
    set_aux = set()
    for i in range(0, len(s)):
        if s[i].isalpha():
            set_aux.add(s[i].lower())
    return "pangram" if len(set_aux) == 26 else "not pangram"


if __name__ == '__main__':
    print(pangrams("We promptly judged antique ivory buckles for the next prize"))
    print(pangrams("We promptly judged antique ivory buckles for the prize"))
