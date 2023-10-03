def activity_selection(activities):
    """
    activities: List of tuples where each tuple has two values:
    (start_time, finish_time). It's assumed that the input activities 
    are distinct.
    
    Returns a list of selected activities.
    """
    
    # Sort activities by finish time
    sorted_activities = sorted(activities, key=lambda x: x[1])
    
    n = len(sorted_activities)
    
    print("Activities selected are:")
    
    # The first activity always gets selected
    i = 0
    print(sorted_activities[i])
    
    # Consider the rest of the activities
    for j in range(n):
        # If this activity has a start time greater than or equal 
        # to the finish time of the previously selected, then select it
        if sorted_activities[j][0] >= sorted_activities[i][1]:
            print(sorted_activities[j])
            i = j

# Test
activities = [(1, 4), (3, 5), (0, 6), (5, 7), (8, 9), (5, 9)]
activity_selection(activities)
