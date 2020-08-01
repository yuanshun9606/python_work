a = int(input())
if a <= 150:
    result = a * 0.4463
elif a <= 400:
    result = 150 * 0.4463 + (a - 150) * 0.4663
else:
    result = 150 * 0.4463 + 250 * 0.4664 + (a - 400) * 0.5663

print('%.1f' % result)
