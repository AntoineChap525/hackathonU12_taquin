def signature(taquin0):

    taquin = []
    for elt in taquin0:
        taquin += elt


    n = len(taquin)
    seen = [False] * n
    sign = 1
    nb_cycle = 0
    for i in range(n):
        if not seen[i]:
            start = taquin[i]
            index = i

            while not seen[index]:
                seen[index] = True
                index = taquin[index]
            nb_cycle += 1
    return ((-1)**(n-nb_cycle), seen)

print(signature([[0, 1], [3, 2, 4, 5]]))

        