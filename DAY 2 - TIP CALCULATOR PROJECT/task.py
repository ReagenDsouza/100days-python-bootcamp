print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_calc=(bill/people)*(1+(tip/100))
final_amt=round(tip_calc,2)
print(f"Tip to be given by each person is: ${final_amt}")


