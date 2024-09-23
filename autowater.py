import numpy as np
import matplotlib.pyplot as plt
import datetime
from collections import defaultdict

data = np.genfromtxt('autowater.csv', delimiter=',', dtype=None, encoding='latin1', names=True)

print(data[:5])

dates = data['DATE_TIME_HEURE']
values = data['VALUE_VALEUR']

valid_indices = ~np.isnan(values)
dates = dates[valid_indices]
values = values[valid_indices]

dates = [datetime.datetime.strptime(date, '%d/%m/%Y %H:%M') for date in dates]
monthly_data = defaultdict(list)
for date, value in zip(dates, values):
    month = date.strftime('%Y-%m')
    monthly_data[month].append(value)

months = sorted(monthly_data.keys())
monthly_avg_values = [np.mean(monthly_data[month]) for month in months]

months = [datetime.datetime.strptime(month, '%Y-%m') for month in months]

plt.figure(figsize=(10, 6))
plt.plot(months, monthly_avg_values, marker='o', linestyle='-', color='b')
plt.title('Monthly Data Visualization')
plt.xlabel('Month')
plt.ylabel('Average Value')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()