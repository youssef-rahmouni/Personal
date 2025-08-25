import re
import json

GoalDoneDayID = [None] * 7
GoalsNumber = 30
DayProgress = [None] * 7
WeekProgress = 0
WeekID = int()
DaysID = [None] * 7
j = 2

print("________________PROGRESS MEASURE CALCULS________________")
data = input("Enter the data from ProgressDaily :")
GoalsNumber = int(input(f"Enter the Goals Number for Week ({WeekID}) : "))
print(data)

def output(WeekID, DaysID, GoalDoneDayID, WeekProgress, GoalsNumber, DayProgress):
    days_dict = {}
    for i in range(7):
        days_dict[DaysID[i]] = {
            "GoalsDone": int(GoalDoneDayID[i]),
            "DayProgress": round(DayProgress[i], 1)
            }
    data_json = {
    "WeekID" : WeekID,
    "WeekProgress" : round(WeekProgress, 1),
    "GoalsNumber": GoalsNumber,
    "Days": days_dict
    }
    return json.dumps(data_json, indent=4, separators=(',', ': '))


databrute = data.replace(" ","").replace("\n","")
pattern = r"(\d{6})\{(\d{4})\:(\d+)\,(\d{4})\:(\d+)\,(\d{4})\:(\d+),(\d{4})\:(\d+)\,(\d{4})\:(\d+)\,(\d{4})\:(\d+)\,(\d{4})\:(\d+)\}"

try :
    match = re.search(pattern, databrute)
    WeekID = match.group(1)
    for i in range(7):
        DaysID[i] = match.group(j)
        GoalDoneDayID[i] = match.group(j+1)
        DayProgress[i] = (int(GoalDoneDayID[i]) / GoalsNumber) * 100
        WeekProgress += DayProgress[i]
        j +=2
    
    print(output(WeekID, DaysID, GoalDoneDayID, WeekProgress, GoalsNumber, DayProgress))

except Exception as e:
    print("Error:", e)
