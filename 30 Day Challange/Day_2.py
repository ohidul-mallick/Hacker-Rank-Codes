meal_cost=100
tip_percent = 15
tax_percent = 8
tip = (meal_cost*tip_percent)/100
tax = (meal_cost*tax_percent)/100
result = round(meal_cost+tip+tax)
print(result)