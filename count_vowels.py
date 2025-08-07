#takes in a string
#return two ints length of string and number of vowels

def countVowels(str):
    num_vowels = 0
    string_len = len(str)
    vowels = ['a', 'i', 'o', 'e', 'u']

    for c in str:
        if c in vowels:
            num_vowels += 1
    return num_vowels, string_len


def main():
    result = countVowels('Hello World!')

    print(result)


if __name__ == "__main__":
    main()
