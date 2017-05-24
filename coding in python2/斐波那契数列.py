n = int(raw_input())
F0, F1 = 0, 1
if n == 0:
    print F0
elif n == 1:
    print F1
elif 1 < n <= 50:
    while n > 1:
        F0, F1 = F1, F0 + F1
        n = n - 1
    print F1
else:
    print 'error'
