def grade(score):
    if score >= 90:
        return "A"
    else:
        if score >= 80:
            return "B"
        else:
            if score >= 70:
                return "C"
            else:
                if score >= 60:
                    return "D"
                else:
                    return "F"

# Simplified logic using elif
# Cleaner logic using elif
# This version is easier to read and maintain.
def grade_elif(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Cleaner logic using dictionary mapping
def grade_dict(score):
    # List of tuples: (minimum_score, grade)
    grade_map = [
        (90, "A"),
        (80, "B"),
        (70, "C"),
        (60, "D"),
        (0, "F"),
    ]
    for min_score, grade_letter in grade_map:
        if score >= min_score:
            return grade_letter

# Test the functions with sample scores
test_scores = [95, 85, 75, 65, 55]

print("Testing grade functions:")
print("Score | grade() | grade_elif() | grade_dict()")
print("-" * 45)

for score in test_scores:
    result1 = grade(score)
    result2 = grade_elif(score)
    result3 = grade_dict(score)
    print(f"{score:5d} | {result1:7s} | {result2:11s} | {result3:11s}")