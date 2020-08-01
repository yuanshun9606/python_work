n = int(input())
fish = list(map(int, input().split()))
for i in range(n):
    num = 0
    for j in range(i):
        if fish[j] < fish[i]:
            num += 1
    print(num, end=" ")
