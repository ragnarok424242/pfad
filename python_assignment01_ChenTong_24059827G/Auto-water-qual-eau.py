import numpy as np
import matplotlib.pyplot as plt
import datetime
from collections import defaultdict

data = np.genfromtxt('Auto-water-qual-eau.csv', delimiter=',', dtype=None, encoding='latin1', names=True)

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

plt.figure(figsize=(20, 10))
plt.plot(months, monthly_avg_values, marker='o', linestyle='-', color='b')
plt.title('Monthly Auto-water-qual-eau Data Visualization')
plt.xlabel('Month')
plt.ylabel('Average Value')
plt.xticks(months, [month.strftime('%Y-%m') for month in months], rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()