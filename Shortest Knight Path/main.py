# https://www.codewars.com/kata/549ee8b47111a81214000941
# 4 kyu
# Python 3.8

from collections import deque


def knight(p1, p2):
    if p1 == p2:
        return True

    alph_indexes = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}

    p1 = (alph_indexes[p1[0]], int(p1[1]) - 1)
    p2 = (alph_indexes[p2[0]], int(p2[1]) - 1)

    pmoves = (-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)

    visited, que = set(), deque()
    que.append(tuple([p1, 0]))
    visited.add(p1)

    while que:
        vertex = que.popleft()
        for i in range(8):
            neighbour = ((vertex[0][0] + pmoves[i][0], vertex[0][1] + pmoves[i][1]), vertex[1] + 1)
            if neighbour[0] == p2:
                return neighbour[1]
            if not (neighbour[0] in visited) and 0 <= neighbour[0][0] <= 7 and 0 <= neighbour[0][1] <= 7:
                visited.add(neighbour[0])
                que.append(neighbour)


print(knight("a3", "b5"))
