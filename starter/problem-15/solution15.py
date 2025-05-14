def evaluate_student(marks):
    # Check if any subject has marks less than 40
    if any(mark < 40 for mark in marks):
        print("FAILED")
    else:
        average = sum(marks) / len(marks)
        print("Average Marks:", average)

# Test for Student 1
print("Student 1 Result:") 
evaluate_student([40, 45, 70, 90, 56])  # All above 40 → show average

# Test for Student 2
print("Student 2 Result:")
evaluate_student([57, 35, 80, 98, 46])  # One subject < 40 → FAILED