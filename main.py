def compound_interest(p, t, r):
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is', r)
#basecase
    ci = (p * t * r) / 100
    print('The Simple Interest is', ci)
    return ci
#recursive case


compound_interest(8, 6, 8)



def stars(n, descending=True):
    if (descending):
        print ('*'*n)
#basecase
    if n==1:
        if not descending:
            print ('*')
        return
#recursive case
    stars(n-1, descending)
    if not descending:
        print ('*'*n)

stars(5)
print
stars(5, descending=False)