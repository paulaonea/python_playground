# Given a list of points on a 2D plan, identify all rectanlges that can be drawn using any 4 points.


points = [(3, 3), (5, 9), (5, 6), (5, 3), (7, 6), (9, 5), (9, 9), (9, 3), (9, 6)]

x = [x for x, _ in points]
y = [y for _, y in points]

n = len(points)
rectangles = 0
for i1 in range(0, n):
    for j1 in range(i1 + 1, n):
        if x[i1] == x[j1]:
            for i2 in range(j1 + 1, n):
                for j2 in range(i2 + 1, n):
                    if x[i2] == x[j2]:
                        if (y[i1] == y[i2] and y[j1] == y[j2]):
                            print(f'Rectangle found')
                            rectangles += 1
    i1 += 1

if rectangles == 0:
    print('No rectangles found')
else: print(f'Rectangles found: {rectangles}')