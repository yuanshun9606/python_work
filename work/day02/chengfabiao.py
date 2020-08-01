# for i in range(1,10):
#     for j in range(1,10):
#         print("%d * %d = %d "%(i,j,i*j),end="\t")
#     print()
for i in range(1,10):
    for j in range(1,10):
        if(j<=i):
            print("%d * %d = %d " % (j, i, i * j), end="\t")
    print()