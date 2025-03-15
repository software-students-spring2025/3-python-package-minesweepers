#dummify(text: str) -> str – Reverses the vowels in a string.
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

#leetify(text: str) -> str – Converts text into 1337 speak.
def leetify(s):
    s = s.upper()

    leet= {
        'O': '0', 'I': '1', 'Z': '2', 'E': '3',
        'A': '4', 'S': '5', 'G': '6', 'T': '7',
        'B': '8', 'P': '9'
    }

    result = ""
    for char in s:
        if char in leet:
            result += leet[char] 
        else:
            result += char

    return result