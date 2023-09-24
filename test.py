# The time complexity of the solution using replace method is O(kn), where k is the number of words to replace and n is the size of the string.

def solution(s):
    numbers = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    for word,number in numbers.items():
        s = s.replace(word,number)
    
    return s

s = '8zerotwo8'
print(solution(s))
