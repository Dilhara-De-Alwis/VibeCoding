def get_valid_mark(subject_name):
    while True:
        try:
            mark = float(input(f"Enter marks for {subject_name}: "))
            if 0 <= mark <= 100:
                return mark
            else:
                print("Invalid input! Marks must be between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

def main():
    while True:
        name = input("\nEnter student's name (or type 'Exit' to quit): ")
        if name.lower() == "exit":
            print("Exiting program. Goodbye!")
            break
            
        marks = []
        for i in range(1, 4):
            mark = get_valid_mark(f"Subject {i}")
            marks.append(mark)
        
        average = sum(marks) / len(marks)
        
        if average >= 75:
            grade = "A"
        elif average >= 60:
            grade = "B"
        elif average >= 40:
            grade = "C"
        else:
            grade = "Fail"

        print("-" * 30)
        print(f"Name   : {name}")
        print(f"Average: {average:.1f}")
        print(f"Grade  : {grade}")
        print("-" * 30)

if __name__ == "__main__":
    main()
