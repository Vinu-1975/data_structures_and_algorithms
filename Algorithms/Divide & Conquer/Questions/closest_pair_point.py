import math


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def brute_force(points):
    min_dist = float("inf")
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            min_dist = min(min_dist, distance(points[i], points[j]))
    return min_dist


def closest_split_pair(px, py, delta, best_pair):
    ln_x = px[len(px) // 2][0]  # Select midpoint on x-sorted array
    sy = [p for p in py if ln_x - delta <= p[0] <= ln_x + delta]
    best = delta
    len_sy = len(sy)
    for i in range(len_sy - 1):
        for j in range(i + 1, min(i + 7, len_sy)):
            p, q = sy[i], sy[j]
            dist = distance(p, q)
            if dist < best:
                best_pair = p, q
                best = dist
    return best, best_pair


def closest_pair_rec(px, py):
    if len(px) <= 3:
        return brute_force(px), None
    mid = len(px) // 2
    Qx = px[:mid]
    Rx = px[mid:]
    midpoint = px[mid][0]
    Qy = list(filter(lambda x: x[0] <= midpoint, py))
    Ry = list(filter(lambda x: x[0] > midpoint, py))
    (left_dist, pair_left) = closest_pair_rec(Qx, Qy)
    (right_dist, pair_right) = closest_pair_rec(Rx, Ry)
    if left_dist < right_dist:
        delta = left_dist
        best_pair = pair_left
    else:
        delta = right_dist
        best_pair = pair_right
    (split_dist, split_pair) = closest_split_pair(px, py, delta, best_pair)
    if delta <= split_dist:
        return delta, best_pair
    else:
        return split_dist, split_pair


def closest_pair_of_points(points):
    px = sorted(points, key=lambda x: x[0])
    py = sorted(points, key=lambda x: x[1])
    return closest_pair_rec(px, py)[0]


# Example usage:
points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print("The smallest distance is:", closest_pair_of_points(points))
