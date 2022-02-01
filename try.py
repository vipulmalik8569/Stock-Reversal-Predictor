import pandas as pd
li =[1,2,3,4]
li2= list(map(lambda x: x+1, li))
df = pd.DataFrame({'a':li})
df['b'] = li
print(df)
