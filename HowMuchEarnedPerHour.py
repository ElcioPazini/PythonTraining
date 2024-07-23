# -*- coding:utf-8 -*-
_dollarPerHour = 25
_hoursWorkedByMonth = 140
caDollarValue = 3.86

def calculateSalaryPerMonth(dollarPerHour, hoursWorkedByMonth):
	return dollarPerHour * hoursWorkedByMonth

def calculateSalaryPerYear(salaryPerMonth):
	return salaryPerMonth * 12

salaryPerMonth = calculateSalaryPerMonth(_dollarPerHour, _hoursWorkedByMonth); 
salaryPerYear = calculateSalaryPerYear(salaryPerMonth);

print(f'Salary per month: {str(salaryPerMonth)} \nSalary per year: {str(salaryPerYear)} \nBRL Month: {str(salaryPerMonth*caDollarValue)} \nBRL Year: {str(salaryPerYear*caDollarValue)}')