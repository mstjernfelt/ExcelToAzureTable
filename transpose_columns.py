import pandas as pd

# Read the excel file
df = pd.read_excel('data\openorders.xlsx')
print(df)

# Input dataframe:
#   ItemNo  2024-06-01 00:00:00  2024-07-01 00:00:00  2024-08-01 00:00:00  2024-09-01 00:00:00  2024-10-01 00:00:00  2024-11-01 00:00:00
# 0  Item1                 2000                 5000                 2500                 3000                 2250                 5250
# 1  Item2                 3000                  500                 3000                 3100                 2500                 1750

# columns doesn't have fixed names, so I will use the melt() function to achieve this
df = df.melt(id_vars='ItemNo', var_name='Production Date', value_name='Orders')

print(df)
# Output dataframe:
#    ItemNo      Production Date  Orders
# 0   Item1  2024-06-01 00:00:00    2000
# 1   Item2  2024-06-01 00:00:00    3000
# 2   Item1  2024-07-01 00:00:00    5000
# 3   Item2  2024-07-01 00:00:00     500
# 4   Item1  2024-08-01 00:00:00    2500
# 5   Item2  2024-08-01 00:00:00    3000
# 6   Item1  2024-09-01 00:00:00    3000
# 7   Item2  2024-09-01 00:00:00    3100
# 8   Item1  2024-10-01 00:00:00    2250
# 9   Item2  2024-10-01 00:00:00    2500
# 10  Item1  2024-11-01 00:00:00    5250
# 11  Item2  2024-11-01 00:00:00    1750