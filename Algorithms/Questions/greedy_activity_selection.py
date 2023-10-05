def activity_selection(activities):
    n = len(activities)
    activities.sort(key=lambda x:x[1])
    selected_activities = []
    i = 0
    selected_activities.append(activities[i])

    for j in range(1,n):
        if activities[j][0] >= activities[i][1]:
            selected_activities.append(activities[j])
            i = j

    return selected_activities


activities = [(1, 4), (3, 5), (0, 6), (5, 7), (8, 9), (5, 9)]
print(activity_selection(activities))