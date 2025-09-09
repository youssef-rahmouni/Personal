import matplotlib.pyplot as plt
import pandas as pd
import re


print()
def Minute_to_Float(MinuteNumber):
    return int(( MinuteNumber / 60 ) * 100)


df = pd.read_excel('PythonChart/com.samsung.shealth.sleep.xlsx')

# For cleaning columns name from BOM
df.columns = df.columns.str.strip().str.replace('/ufeff','')

# Variables & Lists
SleepColums = str('com.samsung.health.sleep.start_time')
WakeColums = str('com.samsung.health.sleep.end_time')
UpdatedSleepTime = []
SleepTime = []
WakeTime = []
DaysID = []
i = 0


# Cleaning and organize data on groups
# Groups : 1=YYYY, 2=MM, 3=DD, 4=HH, 5=MM
pattern = r"(\d{4})-(\d{2})-(\d{2})\s+(\d{2}):(\d{2})"

for sleepcolum, wakecolumn in zip(df[SleepColums], df[WakeColums]):
    i += 1
    sleepmatch = re.search(pattern, str(sleepcolum))
    wakematch = re.search(pattern, str(wakecolumn))
    daysmatch = re.search(pattern, str(sleepcolum))
    SleepTime.append(float(f"{sleepmatch.group(4)}.{Minute_to_Float(int(sleepmatch.group(5)))}")) #SleepTime[index] = HH.MM
    if int(wakematch.group(4)) == 0 or int(wakematch.group(4)) == 12 :
        WakeTime.append(float(f"{12}.{Minute_to_Float(int(wakematch.group(5)))}")) #WakeTime[index] = HH.MM
    else :
        WakeTime.append(float(f"{wakematch.group(4)}.{Minute_to_Float(int(wakematch.group(5)))}")) #WakeTime[index] = HH.MM
    #DaysID.append(str(f"{daysmatch.group(3)}/{daysmatch.group(2)}")) #DaysID[index] = 'DD/MM'
    DaysID.append(str(f"{daysmatch.group(3)}/{daysmatch.group(2)}_{i}"))

# Update SleepTime list to be correct in chart
for i, value in enumerate(SleepTime):
    wake = WakeTime[i]
    # If sleep > wake, it means sleep went past midnight
    if value > wake:
        # shift SleepTime to negative for early morning
        value = value - 24
    UpdatedSleepTime.append(value)


# Line in Chart
plt.plot(DaysID, UpdatedSleepTime, color= '#652f86', marker='', alpha= 1, label='Sleep Time')
plt.plot(DaysID, WakeTime, color= '#0075c1',marker='',  linestyle= '--', label='Wake Time')
plt.legend()
plt.grid()
plt.fill_between(DaysID, UpdatedSleepTime, WakeTime, color='orange', alpha=0.3)

# Axes X and Y
plt.title('Sleep Time', fontweight= 'bold', size= 20)
plt.ylabel('Hours', size= 15)
plt.xlabel('Days', size= 15)

y_min = min(UpdatedSleepTime)
y_max = max(WakeTime)
y_range = range(int(y_min)-2, int(y_max)+2)
y_labels = []
for y in y_range:
    if y < 0:
        y_labels.append((y + 24) % 24)  # -1→23, -2→22…
    else:
        y_labels.append(y)

plt.ylim(int(y_min)-2, int(y_max)+2)
plt.yticks(y_range, labels=y_labels)

#plt.ylim(int(min(UpdatedSleepTime)-2), int(max(WakeTime)+2))
#plt.yticks(range(int(min(UpdatedSleepTime)-2), int(max(WakeTime)+2)))
labels_clean = [d.split("_")[0] for d in DaysID]
plt.xticks(range(len(DaysID)), labels_clean, rotation=75)

plt.show()
