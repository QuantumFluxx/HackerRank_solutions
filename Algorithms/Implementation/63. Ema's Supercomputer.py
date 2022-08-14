def get_pluses(x, y, grid, width, height):
    pluses = []
    if grid[y][x]:
        dist = 0

        for i in range(0, max(width, height)):
            if y-i < 0 or not grid[y-i][x]:
                break
            if y+i >= height or not grid[y+i][x]:
                break
            if x-i < 0 or not grid[y][x-i]:
                break
            if x+i >= width or not grid[y][x+i]:
                break
            pluses.append((x, y, dist, dist * 4 + 1))
            dist += 1

    return pluses


def line_intersect(l1, l2):
    return l1[0] <= l2[2] and l1[2] >= l2[0] and l1[1] <= l2[3] and l1[3] >= l2[1]


def intersect(p1, p2):
    if p1[0] == p2[0] and p1[1] == p2[1]:
        return True

    l1 = p1[0] - p1[2], p1[1], p1[0] + p1[2], p1[1]
    l2 = p1[0], p1[1] - p1[2], p1[0], p1[1] + p1[2]
    l3 = p2[0] - p2[2], p2[1], p2[0] + p2[2], p2[1]
    l4 = p2[0], p2[1] - p2[2], p2[0], p2[1] + p2[2]

    return line_intersect(l1, l3) or line_intersect(l1, l4) or line_intersect(l2, l3) or line_intersect(l2, l4)

if __name__ == '__main__':
    n, m = map(int, input().strip().split(' '))

    grid = []
    for i in range(n):
        grid.append([True if x == 'G' else False for x in input().strip()])

    pluses = []

    for y in range(n):
        for x in range(m):
            pluses += get_pluses(x, y, grid, m, n)

    if len(pluses) <= 1:
        print(0)
    else:
        best = 0
        for i in range(len(pluses)-1):
            for j in range(i+1, len(pluses)):
                if not intersect(pluses[i], pluses[j]):
                    best = max(best, pluses[i][3] * pluses[j][3])

        print(best)