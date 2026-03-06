def main():
    budget = float(input("Enter total monthly budget (LKR): "))
    
    print("\nEnter expenses (type 'done' to finish):")
    
    while True:
        expense_input = input("Enter expense amount (LKR): ")
        
        if expense_input.lower() == "done":
            break
        
        try:
            expense = float(expense_input)
            budget -= expense
            print(f"Remaining balance: {budget:.2f} LKR")
            
            if budget < 500:
                print("Warning: Low Funds")
                
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")
    
    print(f"\nFinal remaining balance: {budget:.2f} LKR")
    if budget < 500:
        print("Warning: Low Funds")

if __name__ == "__main__":
    main()