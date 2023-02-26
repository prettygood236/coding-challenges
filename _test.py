lines = []
while True:
    line = input().rstrip()
    if line:
        lines.append(line)
    else:
        break

print(*lines,sep='\n')
