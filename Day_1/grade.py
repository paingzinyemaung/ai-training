# grade classification program
marks = float(input("Enter your marks from 0 to 100: "))

if marks < 0 or marks > 100:
    print("Invalid marks. Please enter marks between 0 and 100.")
elif marks >= 80:
    print("Excellent")
elif marks >= 60:
    print("Good")
elif marks >= 40:
    print("Passed")
else:
    print("Failed")
