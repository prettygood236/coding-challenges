# ---
# title: Speed Camera Placement
# tags: [CodingChallenges, Python, Greedy, Sorting]
# created: '2023-10-05'
# ---

# # Speed Camera Placement

# ## Problem Description

# You are planning to install speed cameras on a highway. All vehicles using the highway should encounter at least one camera. Given the routes of each vehicle as an array where `routes[i][0]` is the point at which the i-th vehicle enters and `routes[i][1]` is the point at which it exits, determine the minimum number of cameras needed so that every vehicle encounters at least one camera.

# ## Constraints

# - The number of vehicles is between 1 and 10,000.
# - Each route in routes represents a vehicle's path with `routes[i][0]` as its entry point and `routes[i][1]` as its exit point.
# - Even if a camera is installed at a vehicle's entry or exit point, it counts as encountering a camera.
# - Entry and exit points are integers between -30,000 and 30,000.

# ## Solution

# This problem can be solved by using a greedy approach along with sorting. 

# Firstly sort all routes by their ending points. Then iterate through sorted routes while maintaining current camera position (`answer[-1]`). If current route starts before current camera position and ends after it then we don't need to add new camera because this car will encounter current camera.

# If not then add new camera positioned on end of current route because we want to cover as many future cars as possible (since routes are sorted by end position).

# ```python
def solution(routes):
    routes.sort(key=lambda x: x[1])
    answer = [-30001]
    
    for i,o in routes:
        if i <= answer[-1] <= o:
            continue
        answer.append(o) 

    return len(answer[1:])  

# Test Case
routes = [[-20,-15], [-20,-18], [-14,-5], [-18,-13], [-5,-3]]
print(solution(routes)) #2