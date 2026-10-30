from datetime import datetime, timedelta
start_date = datetime(2026,10,28)
end_date= datetime(2098,12,31)
maxrun =0
max_run_start = ""
max_run_end = ""
current_run_length=0
last_distinct_date= ""
while start_date <= end_date:
    date_string = start_date.strftime("%d%m%y")
    distinct=len(set(date_string))==6
    if distinct:
        if current_run_length> maxrun:
            maxrun= current_run_length
            max_run_start =last_distinct_date
            max_run_end = date_string
        last_distinct_date= date_string
        current_run_length= 0
    else:
        if last_distinct_date!="":
            current_run_length +=1
    start_date += timedelta(days=1)
print(f"longest run: {maxrun} days")
print("answer format(ddmmyyDDMMYY):")
print(f"{max_run_start}{max_run_end}")
