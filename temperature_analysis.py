# Name: Kalaiarasi Thangamani
# Roll Number: iitp_aimltn_2602878
# Assignment: Python Loops & Automation - Subjective Question
#--------------------------------------------------------------------------------------------------------------

# Write code to find the highest and lowest temperature from the list.

print("===== Task 1: Find Maximum and Minimum =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]

max_temp = temperatures[0]

for temp in temperatures:
    if temp > max_temp:
        max_temp = temp
print(f"Highest Temperature: {max_temp}°C")

min_temp = temperatures[0]

for temp in temperatures:
    if temp < min_temp:
        min_temp = temp
print(f"Lowest Temperature: {min_temp}°C")

#--------------------------------------------------------------------------------------------------------------
# Count how many days had temperature above 30°C. Skip days with temperature ≤30°C using continue.

print("\n===== Task 2: Count Hot Days =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]

hot_days = 0
for temp in temperatures:

    if temp <= 30:
        continue
    hot_days += 1
print(f"Hot Days (>30°C): {hot_days}")

#--------------------------------------------------------------------------------------------------------------
# Count hot days but stop immediately if temperature reaches 40°C or higher using break.

print("\n===== Task 3: Alert System =====")
temperatures = [28, 32, 35, 40, 31, 33, 30]

hot_days = 0
day = 0
for temp in temperatures:

    if temp <= 30:
        day += 1
        continue
    elif temp > 30 and temp < 40:
        hot_days += 1
        day += 1
    elif temp >= 40:
        break
day += 1

print(f"Hot Days before alert: {hot_days}")
print(f"Alert! Extreme temperature 40°C detected on Day {day}")
