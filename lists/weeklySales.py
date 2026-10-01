# Your mission: Record seven days' sales in a list.
# Calculate the total, the average, and show the day 
# with the highest sales.

def weeklySales():
    sales = []

    for s in range(7):
        userInput = float(input(f"Día {s + 1}: "))

        sales.append(userInput)

    print(f"Total ventas: {sum(sales):.2f}")
    print(f"Promedio ventas: {sum(sales) / len(sales):.2f}")
    print(f"Día con mayores ventas: {sales.index(max(sales)) + 1}")


weeklySales()