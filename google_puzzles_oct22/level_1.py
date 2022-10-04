_TRANSLATION = {}
_ALPHABET = "abcdefghijklmnopqrstuvwxyz"

for i, letter in enumerate(_ALPHABET):
    _TRANSLATION[letter] = _ALPHABET[-1-i]

def solution(x: str):
    solution = ''
    for letter in x:
        if not letter.islower():
            solution += letter
        else:
            solution += _TRANSLATION[letter]
    return solution

print(solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?"))
print(solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"))