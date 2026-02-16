"""
Author: Isha
Assignment: #1
"""

# Step 3: Variables
gym_member = "Alex Alliton"       # str
preferred_weight_kg = 20.5        # float
highest_reps = 25                 # int
membership_active = True          # bool

# Step 4: Dictionary
# Dictionary storing workout minutes for each friend: data type is dict[str, tuple[int, int, int]]
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (20, 60, 25),
    "Taylor": (15, 50, 30)
}

# Calculate total minutes and add new key-value pairs
for friend, activities in workout_stats.items():
    total_minutes = sum(activities)
    workout_stats[f"{friend}_Total"] = total_minutes

# Step 5: 2D list
# Nested list of workout minutes for all friends: data type is list[list[int]]
workout_list = [list(activities) for activities in workout_stats.values() if isinstance(activities, tuple)]

# Slice: Yoga and running for all friends
yoga_running = [row[:2] for row in workout_list]
print("Yoga and running minutes:", yoga_running)

# Slice: Weightlifting for last two friends
weightlifting_last2 = [row[2] for row in workout_list[-2:]]
print("Weightlifting minutes for last two friends:", weightlifting_last2)

# Step 6: Check for friends with total workout >= 120
for friend, activities in workout_stats.items():
    if "_Total" not in friend and sum(activities) >= 120:
        print(f"Great job staying active, {friend}!")

# Step 7: User input for friend's name
friend_name = input("Enter friend's name: ")
if friend_name in workout_stats:
    activities = workout_stats[friend_name]
    total = sum(activities)
    print(f"{friend_name}'s workout minutes: Yoga={activities[0]}, Running={activities[1]}, Weightlifting={activities[2]}, Total={total}")
else:
    print(f"Friend {friend_name} not found in the records.")

# Step 8: Friend with highest and lowest total workout minutes
totals = {k: v for k, v in workout_stats.items() if "_Total" in k}
highest = max(totals, key=totals.get)
lowest = min(totals, key=totals.get)
print(f"Friend with highest total workout minutes: {highest} ({totals[highest]} minutes)")
print(f"Friend with lowest total workout minutes: {lowest} ({totals[lowest]} minutes)")
