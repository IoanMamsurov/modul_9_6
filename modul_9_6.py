from itertools import combinations

def all_variants(text):
    a = []
    for i in range(1, len(text)+1):
        a = []
        b = combinations(text, i)
        a.extend(b)
        for j in a:
            j = list(j)
            yield (''.join(j))





a = all_variants("abc")
for i in a:
    print(i)