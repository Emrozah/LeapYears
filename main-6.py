
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_year_leap(year):

    if year % 4 != 0: 
        return False 
    elif year % 100 != 0: 
        return True 
    elif year % 400 != 0: 
        return False 
    else: 
        return True


def days_in_month(year, month):
    
    if year < 1582 or month < 1 or month > 12: 
        return None

    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days2 = days[month-1]
    
    if month == 2 and is_year_leap(year):
        return 29
    else:
        return days2
        
def day_of_year(year, month, day):

    sum_of_days = 0
    for i in range (0, month):
        daysInCurrentMonth = days_in_month(year,i)
        #print(daysInCurrentMonth)
        if daysInCurrentMonth != None:
            sum_of_days += daysInCurrentMonth
            #sum_of_days1 = (sum_of_days + day)
    sum_of_days += day    
    return(sum_of_days)


test_years = [2000]
test_months = [12]
test_day = [31]
test_results = [366]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	da = test_day [i]
	print(yr, mo, da, "->", end="")
	result = day_of_year(yr, mo, da,)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
		
		
	print(result)