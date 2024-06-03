# -*- coding:utf-8 -*-

# Calculating simple compound interest (without taxes) ------------------------------------------------------

currentValue = float(input("How much do you have today? -> "))
valuePerMonth = float(input("How much will you apply per month? -> "))
percentageOfIncomePerMonth = float(input("What is the % of interest rate per month of your investment? -> "))
allMoneyInvested = currentValue
desiredQtd = float(input("How much do you desire to have in the future? -> "))
count = 0

percentageOfIncomePerMonth = percentageOfIncomePerMonth/100

while currentValue < desiredQtd:
	count += 1;
	print("Month " + str(count))
	if currentValue > 0:
		incomeOfMonth = currentValue * percentageOfIncomePerMonth;
		print("	Income: " + str(round(incomeOfMonth, 2)))
		currentValue += incomeOfMonth
	currentValue += valuePerMonth
	allMoneyInvested += valuePerMonth
	print("	Current value : " + str(round(currentValue,2)))

print(f'It will take you {count} months to reach your desired value, and you will invest ${allMoneyInvested} out of your pocket during this time')
print(f'However, you will receive ${round((currentValue-allMoneyInvested), 2)} in passive income')