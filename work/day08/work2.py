a = input().split()
tree = [1] * (int(a[0]) + 1)
for i in range(int(a[1])):
    b = input().split()
    for j in range(int(b[0]), int(b[1]) + 1):
        tree[j] = 0
print(tree.count(1))
