def solution(s):
    # breakpoint()
    i = 0
    new_s = ''
    # We just need to iterate over the index i according to the condition. So let's use a while loop!
    while i < len(s): 
        try:
            if int(s[i]):
                new_s += s[i]
                i += 1
                continue
        except:
            if s[i:i+3] == 'one':
                new_s += '1'
                i += 3
                continue
            elif s[i:i+3] == 'two':
                new_s += '2'
                i += 3
                continue
            elif s[i:i+3] == 'six':
                new_s += '6'
                i += 3
                continue
            elif s[i:i+4] == 'zero':
                new_s += '0'
                i += 4
                continue
            elif s[i:i+4] == 'four':
                new_s += '4'
                i += 4
                continue
            if s[i:i+4] == 'five':
                new_s += '5'
                i += 4
                continue
            if s[i:i+4] == 'nine':
                new_s += '9'
                i += 4
                continue
            if s[i:i+5] == 'three':
                new_s += '3'
                i += 5
                continue
            if s[i:i+5] == 'seven':
                new_s += '7'
                i += 5
                continue
            if s[i:i+5] == 'eight':
                new_s += '8'
                i += 5
                continue


    return new_s

s = '8zerotwo8'
print(solution(s))
