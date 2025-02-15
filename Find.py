from datetime import datetime

def min_platforms(arrivals, departures):
    arrivals.sort()
    departures.sort()
    
    n = len(arrivals)
    platforms_needed = 1
    result = 1
    i, j = 1, 0

    while i < n and j < n:
        if arrivals[i] <= departures[j]:
            platforms_needed += 1
            i += 1
        else:
            platforms_needed -= 1
            j += 1

        result = max(result, platforms_needed)
    
    return result

# Example usage
arrivals = [datetime.strptime(t, '%H:%M') for t in ['9:00', '9:40', '9:50', '11:00', '15:00', '18:00']]
departures = [datetime.strptime(t, '%H:%M') for t in ['9:10', '12:00', '11:20', '11:30', '19:00', '20:00']]
print(min_platforms(arrivals, departures))
