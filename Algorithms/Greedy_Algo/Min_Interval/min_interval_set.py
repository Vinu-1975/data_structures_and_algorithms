def min_points(intervals):
    # Sort intervals by end point
    intervals.sort(key=lambda x: x[1])

    points = []
    while intervals:
        # Take the end point of the first interval
        point = intervals[0][1]
        points.append(point)

        # Remove all intersected intervals
        intervals = [i for i in intervals if i[0] > point]

    return points

# Test Cases
intervals = [[1,9], [4,6], [5,11], [11,19], [12,20]]
print(min_points(intervals))  # Expected Output: [9, 19]

# Additional Test Cases
intervals = [[1, 7], [9, 20], [3, 10]]
print(min_points(intervals))  # Expected Output: [3, 11]

intervals = [[1, 2], [2, 3], [3, 4]]
print(min_points(intervals))  # Expected Output: [2, 3, 4]
