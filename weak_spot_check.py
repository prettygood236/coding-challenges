def solution(n, weak, dist):
    copy_weak = weak[:]
    num = len(dist)
    temp_a = weak[-1] - weak[0]
    l = [] 
    for j in range(len(weak)):
      if weak[j] > (n/2):
        copy_weak.remove(weak[j])
        l.append(n - weak[j])
    temp_b = max(copy_weak) + max(l)
    min_dist = min(temp_a,temp_b)
    dist.sort(reverse=True)
    for i in dist:
      if i >= min_dist:
        
    answer = 0
    return answer


n = 12	
weak = [1, 5, 6, 10]	
dist = [1, 2, 3, 4]	
# 2

n = 12	
weak = [1, 3, 4, 9, 10]	
dist = [3, 5, 7]	
# 1

print(solution(n, weak, dist))