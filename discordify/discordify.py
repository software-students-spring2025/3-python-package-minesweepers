def dummify(s):
    vowels = "aeiouAEIOU"
    vowel_list = [char for char in s if char in vowels]
    result = []
    for char in s:
        if char in vowels:
            result.append(vowel_list.pop())
        else:
            result.append(char)
    return "".join(result)
