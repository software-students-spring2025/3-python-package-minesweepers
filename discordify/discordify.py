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


#uwuify(text: str) -> str – L to w, sparkle ASCII at the start and end
def uwuify(s):
    s = s.lower()

    uwu= {
        'l':'w','r':'w', '.':'⋆ ˚｡⋆୨୧˚\n⋆˙⟡'
    }

    result = ""
    result += '✧˖°. '

    for char in s:
        if char in uwu:
            result += uwu[char] 
        else:
            result += char
    result += ' ₊˚⊹♡'

    return result
