def probability(k):
    l=365-k+1
    n=365**k
    m=1
    if k > 365:
        return "100%"
    else:
        for x in range(l,366):
            m*=x
        result = 1 - (m/n)
        main=result*100
        return ("{}%".format(main))


print(probability(153))



