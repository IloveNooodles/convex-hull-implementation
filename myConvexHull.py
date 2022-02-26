def minmax(points):  # get the min idx and max idx point from points
    min_point, max_point = points[0], points[0]
    min_idx, max_idx = 0, 0
    for i in range(len(points)):
        if(points[i][0] < min_point[0]):
            min_point = points[i]
            min_idx = i
        if(points[i][0] > max_point[0]):
            max_point = points[i]
            max_idx = i
    return min_idx, max_idx


# return min or max index when the point is farthest from respective isAbove
def farthestDistance(point1, point2, points, isAbove):
    max_distance, min_distance = 0, 0
    min_idx, max_idx = -1, -1
    for i in range(len(points)):
        distance = findDistance(point1, point2, points[i])
        if min_distance > distance:
            min_distance = distance
            min_idx = i
        if max_distance < distance:
            max_distance = distance
            max_idx = i

    if isAbove:
        return max_idx
    return min_idx


# derived from y-y1/y2-y1 = x-x1/x2-x1 change the y and x to point3 and if it > 0 it belongs to the upper segment of the line
def findDistance(point1, point2, point3):
    return ((point3[1] - point1[1])*(point2[0] - point1[0]) -
            (point3[0] - point1[0])*(point2[1] - point1[1]))


def quickHull(mostleft_idx, mostright_idx, points, isAbove, solution):  # quickHull Algo
    mostleft = points[mostleft_idx]
    mostright = points[mostright_idx]
    max_distance_idx = farthestDistance(mostleft, mostright, points, isAbove)
    if max_distance_idx == -1:
        solution.append([mostleft_idx, mostright_idx])
        return
    max_distance_point = points[max_distance_idx]

    quickHull(mostleft_idx, max_distance_idx, points, isAbove, solution)
    quickHull(max_distance_idx, mostright_idx, points, isAbove, solution)


def convexHull(points):
    solution = []
    mostleft_idx, mostright_idx = minmax(points)
    quickHull(mostleft_idx, mostright_idx, points, True, solution)
    quickHull(mostleft_idx, mostright_idx, points, False, solution)
    return solution
