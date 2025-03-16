import re
import sys
import random

sys.stdout.reconfigure(encoding='utf-8')

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

#stutterify(text: str) -> str – Adds a stuttering effect to the text.
def stutterify(s):
    pronouns = {"you","wait","what","so","um","uh","i"}
    conjunctions = {'but','and'}

    def stutter(word):
        prefix = word[:1]
        return f"{prefix}-{word}" if word else word
    
    words = re.findall(r"\b\w+\b|[^\w\s]", s)
    if words:
        words[0] = stutter(words[0])
    for i in range(1, len(words)):
        word = words[i].lower()
        if word in pronouns:
            words[i] = stutter(words[i])
        elif word in conjunctions:
            words[i] += "..."  
    result = []
    for i, word in enumerate(words):
        if i > 0 and re.match(r"[.,!?;:]", word):  
            result[-1] += word
        else:
            result.append(word)

    return " ".join(result)

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

#uwuify(text: str) -> str – L to w, sparkle ASCII at the start and end
def uwuify(s):
    s = s.lower().strip()

    uwu= {
        'l':'w','r':'w', '.':'˚｡⋆୨୧˚\n⋆˙⟡'
    }

    result = ""
    result += '✧˖°. '

    for char in s:
        if char in uwu:
            result += uwu[char] 
        else:
            result += char

    if (s[len(s)-1] == '.'):        
        return result[:-4]
    else:
        result += ' ₊˚⊹♡'
        return result

#sarcasmify(text: str) -> str – Alternates between uppercase and lowercase letters
def sarcasmify(s):
    result = []
    should_be_upper = bool(random.getrandbits(1))  # Random start
    
    for char in s:
        if char.isalpha():
            result.append(char.upper() if should_be_upper else char.lower())
            should_be_upper = not should_be_upper
        else:
            result.append(char)
    
    # Add sarcasm indicator
    if random.random() < 0.4:  # 40% chance
        result.append(" 🙄")
    
    return "".join(result)

#zalgoify(text: str) -> str – Adds "corrupted" text effects with combining characters
def zalgoify(s, intensity=1):
    # Unicode combining characters that will appear above
    above_chars = [
        '\u0300', '\u0301', '\u0302', '\u0303', '\u0304', '\u0305',
        '\u0306', '\u0307', '\u0308', '\u0309', '\u030A', '\u030B',
        '\u030C', '\u030D', '\u030E', '\u030F', '\u0310', '\u0311'
    ]
    
    # Unicode combining characters that will appear below
    below_chars = [
        '\u0316', '\u0317', '\u0318', '\u0319', '\u031A', '\u031B',
        '\u031C', '\u031D', '\u031E', '\u031F', '\u0320', '\u0321',
        '\u0322', '\u0323', '\u0324', '\u0325', '\u0326', '\u0327'
    ]
    
    # Unicode combining characters that will appear in the middle
    middle_chars = [
        '\u0334', '\u0335', '\u0336', '\u0337', '\u0338', '\u0339',
        '\u033A', '\u033B', '\u033C', '\u033D', '\u033E', '\u033F'
    ]
    
    result = []
    
    # Adjust number of combining characters based on intensity (1-3)
    intensity = max(1, min(3, intensity))
    count_above = intensity
    count_below = intensity
    count_middle = intensity
    
    for char in s:
        result.append(char)
        
        # Don't zalgoify spaces
        if char.isspace():
            continue
            
        # Add random combining characters above
        for _ in range(count_above):
            if random.random() < 0.7:  # 70% chance to add a character
                result.append(random.choice(above_chars))
                
        # Add random combining characters below
        for _ in range(count_below):
            if random.random() < 0.5:  # 50% chance to add a character
                result.append(random.choice(below_chars))
                
        # Add random combining characters in the middle
        for _ in range(count_middle):
            if random.random() < 0.3:  # 30% chance to add a character
                result.append(random.choice(middle_chars))
    
    return "".join(result)