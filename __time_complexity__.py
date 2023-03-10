
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

n = int(input())
c = 0
for i in range(1,n-1):
    c += (n-(i+1)) * (n+1-((n-(i+1))+1))



# for i in range(1,n-1):
#     print(c,'1')
#     for j in range(i+1,n):
#         print(c,'2')
#         for k in range(j+1,n+1):
#             c += 1

print(c)
print(3)