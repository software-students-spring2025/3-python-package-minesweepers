

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