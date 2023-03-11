
# MenOfPassion(A[], n) {
#     i = ⌊n / 2⌋;
#     return A[i]; # 코드1
# }
# n**0

# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n
#         sum <- sum + A[i]; # 코드1
#     return sum;
# }
# n**1

# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n
#         for j <- 1 to n
#             sum <- sum + A[i] × A[j]; # 코드1
#     return sum;
# }
# n**2


# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n - 1
#         for j <- i + 1 to n
#             sum <- sum + A[i] × A[j]; # 코드1
#     return sum;
# }

# n = int(input())
# c = 0
# for i in range(1,n):
#     c += n+1-(i+1)
      
# print(c)
# print(2)



# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n
#         for j <- 1 to n
#             for k <- 1 to n
#                 sum <- sum + A[i] × A[j] × A[k]; # 코드1
#     return sum;
# }



# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n - 2
#         for j <- i + 1 to n - 1
#             for k <- j + 1 to n
#                 sum <- sum + A[i] × A[j] × A[k]; # 코드1
#     return sum;
# }


# n = int(input())
# count = 0

# # for i in range(1,n-1):
# #     for j in range(i+1,n):
# #         for k in range(j+1,n+1):
# #             count += 1

# for i in range(1,n):
#     count += (n-(i)) * (n-(i+1))

# count //= 2

# print(count)
# print(3)




a1,a0 = map(int,input().split())
c = int(input())
n0 = int(input())
flag = 1

for i in range(n0,100):
    if(a1*i+a0 <= c*i):
        continue
    else:
        flag = 0
        break

print(flag)