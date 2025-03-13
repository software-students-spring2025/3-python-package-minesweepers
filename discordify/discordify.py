import re

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

def stutterify(s):
    pronouns = {"you","wait","what","so","um","uh","i"}
    conjunctions = {'but','and'}

    def stutter(word):
        prefix = word[:1]
        return f"{prefix}-{word}" if word else word
    
    words = re.findall(r"\b\w+\b|[^\w\s]", text)
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
