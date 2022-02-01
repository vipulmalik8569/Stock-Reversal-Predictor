import pandas as pd
import matplotlib.pyplot as plt

syms = ['MSFT', 'JPM', 'AMZN', 'UNH', 'KO', 'FB', 'NVDA', 'TSLA', 'AMZN']
sym = 'MSFT'
df = pd.read_csv(f'{sym}.csv')

plt.plot(df['close'].loc[0:10,], label='close')

plt.plot(df['Real Upper Band'].loc[0:10,], label='BBand Upper')
plt.plot(df['Real Middle Band'].loc[0:10,], label='BBand Mid')
plt.plot(df['Real Lower Band'].loc[0:10,], label='BBand Lower')
plt.legend()
plt.show()

df['Trend'] = df['close'] - df['Real Middle Band']
df['Trend'] = list(map(lambda x: 'U' if x>=0 else 'D', df['Trend']))
print(df.columns)

df.to_csv(f'{sym}.csv')