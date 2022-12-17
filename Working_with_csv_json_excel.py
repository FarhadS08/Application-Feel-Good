import pandas as pd

df1 = pd.DataFrame([[2,4,6], [1,3,5]], columns=['Price', 'Age', 'Value'], index=['First', 'Second',])

df2 = pd.DataFrame([{'Name': 'John'},{'Name': 'Jack'}])

print(df2)