import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('../dataset_raw/Social_Network_Ads.csv')
df = df.drop(columns=['User ID'])
le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])
df.to_csv('Social_Network_Ads_preprocessing.csv', index=False)
print("✅ File preprocessing berhasil dibuat!")