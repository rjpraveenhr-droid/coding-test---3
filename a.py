# 1 Store five student names and score
grade_book = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 72,
    "Diana": 95,
    "Ethan": 64
              }

# initialize variables
max_score = 100
min_score = -1
top_scorer = "" 
bottom_scorer = ""

# 2 For loop to find top and bottom scorer
for student, score in grade_book.items():
    if score > max_score: 
        max_score = score
        top_scorer = student

    if score < min_score:
        min_score = score
        bottom_scorer = student

# Calculate
extreme_average = (max_score + min_score) / 2

print("Class Statistics")
print(f"Top Scorer: {top_scorer} ({max_score})")
print(f"Bottom Scorer: {bottom_scorer} ({min_score})")
print(f"Average of Top and Bottom Scorer: {extreme_average:2f}\n")

print("Student Grade Lookup")
search_name = input("Enter the name of the student")

retrieved_score = grade_book.get(search_name)
if retrieved_score is not None:
    print(f"{search_name}'s score is: {retrieved_score}")
else:
    print(f"sorry, 'search_name' was not found.")