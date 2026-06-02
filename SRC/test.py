# this used for converting data ... 

from load_data import convert_tsf_to_dataframe
import pandas as pd

df, frequency, horizon, missing, equal_length = (
    convert_tsf_to_dataframe(
        r"C:\Users\com125\Desktop\Parth_Intern\DATA\us_births_dataset.tsf"
    )
)

values = df["series_value"][0] 

start_date = df["start_timestamp"][0]

births_df = pd.DataFrame({"date": pd.date_range(start=start_date, periods=len(values), freq="D"), "births": values})

print(births_df.head())
print(births_df.shape)
print(births_df.info())
print(births_df.describe())
print(births_df.isnull().sum())

