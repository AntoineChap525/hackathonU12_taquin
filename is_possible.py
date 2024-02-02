def is_possible(taquin0,coord):

    taquin = []
    for elt in taquin0:
        taquin += elt
    a,b = coord
    n = len(taquin0)
    p = (2*n-2-a-b) % 2
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
    return (1 == (-1)**(n-nb_cycle)*(-1)**p)

        