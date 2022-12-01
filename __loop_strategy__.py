
#. brute force strategy
# import random
# box = [i for i in range(1,101)]
# random.shuffle(box)
# success = []
# while len(success) < 100:
#   success = []
#   for i in range(1,101):
#     for _ in range(50):
#       if i == random.choice(box):
#         success.append(i)
#         break
# print(success)
# print(0.5**100)

#. loop strategy
import random
box = [i for i in range(100)]
l = []
count = 0
success = 0
probablity = 0
while count < 1000000 : 
  random.shuffle(box)
  l = []
  flag = False
  for i in range(100):
    loop = i
    for _ in range(50):
      if box[loop] == i:
        flag = True
        l.append(i)
        break
      loop = box[loop]
    if flag == False:
      break
  count += 1
  if len(l) == 100:
    success += 1
probablity = (success / count)*100
print(probablity,'%')
    
