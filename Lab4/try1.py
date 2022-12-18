import pandas as pd
import numpy as np
ave_data = np.array(np.arange(24)).reshape(6,4)
dates = pd.date_range("20210101", periods=6)
ave_df = pd.DataFrame(ave_data, index=dates, columns=list("1234"))
print(ave_df)
print(ave_df.loc["2021-01-01":"2021-01-03",["1","3"]])
print(ave_df.loc["2021-01-02",["1","3"]][0]*5)
print(ave_df.loc[dates[1],"1"])
print(ave_data[2])
print(ave_df.iloc[1:3, 2:5])
print(ave_df[ave_df>=5])
start_date = "20210101"
ave_numpy_data = np.array(np.arange(40)).reshape(10,4)
dates = pd.date_range(start_date, periods=10)
ave_df = pd.DataFrame(ave_numpy_data, index=dates, columns=list("abcd"))
print(ave_df)
ave_df_cars = ave_df.copy()
ave_df_cars["Cars"] = ["Ford","Opel", "Mazda", "Mitsubishi", "Renault", "lada", "Hammer", "BMW", "Mercedes", "VW"]
print(ave_df_cars)
print(pd.date_range(start_date, periods=10))
print(pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index = pd.date_range(start_date, periods=10)))
ave_series = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index = pd.date_range(start_date, periods=10))
ave_df_cars["Extra"] = ave_series*10+2
print(ave_df_cars)
ave_df_cars.at[dates[4],"Cars"] = "Citroen"
print(ave_df_cars)
ave_df_cars.iat[4, 2] = 666
print(ave_df_cars)
ave_new_array = np.array(np.arange(len(ave_df_cars)))*10+5
print(ave_new_array)
ave_df_cars["E"] = ave_new_array
print(ave_df_cars)
laptops = ["Lenovo", "Dell", "HP", "Chromebook", "Macbook"]
laptops_df = pd.DataFrame({
    "price" : [350,400,500, 560,100],
    "disc_space" : [0.5, 1, 2, 3, 1.5]},
    index=laptops
)
print(laptops_df)

more_laptops = ["Lenovo", "Dell", "HP", "Huawei", "Macbook"]
laptops_df_2 = laptops_df.reindex(more_laptops)
print(laptops_df_2)
laptops_df_3 = laptops_df_2.fillna(value=100)
print(laptops_df_3)
print(pd.isnull(laptops_df_2))
pd.set_option("display.precision", 2)
print(laptops_df_2.apply(np.cumsum, axis=0))
pieces = [laptops_df_2[:1], laptops_df_2[1:3], laptops_df_2[3:]]
print(pieces)
new_list = pieces[0], pieces[2]
pd.concat(new_list)
print(new_list)
new_last_row = laptops_df_2.iloc[2]
laptops_df_2.append(new_last_row)
print(laptops_df_2)
print()
left = pd.DataFrame({
    "my_key" : ["K0", "K1", "k2", "K3"],
    "A" : ["A0", "A1", "A2", "A3"],
    "B" : ["B0", "B1", "B2", "B3"]
})
right = pd.DataFrame({
    "my_key" : ["K0", "K1", "K2", "K3"],
    "C" : ["C0", "C1", "C2", "C3"],
    "D" : ["D0", "D1", "D2", "D3"]
})
result = pd.merge(left, right, on="my_key")
print(result)
### Import Data
bank_df = pd.read_csv("/Users/Bogruk/Downloads/Pandas-main/bank.csv")
print(bank_df.head(100))
bank_df.to_csv("/Users/Bogruk/Downloads/Pandas-main/bank_updated.csv")
retail_file = "/Users/Bogruk/Downloads/Pandas-main/Online Retail.xlsx"
online_retail_df = pd.read_excel(retail_file, "Online Retail", index_col=None, na_values=["NA"])
print(online_retail_df)
print(online_retail_df.groupby("Quantity").sum())
online_retail_df.groupby("Country").count()
ave_index = pd.date_range("1/1/2021", periods=10, freq="min")
print(ave_index)
ave_series = pd.Series(np.arange(10), index=ave_index)
print(ave_series)
ave_series_resample = ave_series.resample("5min").sum()
print(ave_series_resample)
def custom_math(array_like):
    temp=3*np.sum(array_like)+10
    return temp
print(ave_series.resample("3min").apply(custom_math))
ave_simple_series = pd.Series(np.random.randn(5), index=["A","B","C","D","E"])
print(ave_simple_series)
ave_dictionary = {"A":30, "B":-5.8, "C":666}
ave_another_series = pd.Series(ave_dictionary)
print(ave_another_series)
def mult_by_ten (input_element):
    return input_element*10.0
print(ave_simple_series.map(mult_by_ten))
series_of_random_staff = pd.Series(["A","B","C","Abracadabra", np.nan, "dog","cow,","helicopter"])
series_of_random_staff.str.lower()
from datetime import datetime
now=datetime.now()
print(now)
pd.Timedelta("5 days 10 hours")
pd.Timedelta(days=2, seconds=10)
new_year= datetime(2021, 1, 1)
print(new_year)
national_absurdity_day = datetime(2021, 11, 20)
print(national_absurdity_day)
Tuvalu_independence_day= datetime(2021, 10, 1)
print(Tuvalu_independence_day)
time_to_relax = national_absurdity_day-Tuvalu_independence_day
print(time_to_relax)
time_to_relax_range = pd.date_range(national_absurdity_day, periods=time_to_relax.days, freq="D")
time_to_relax_series = pd.Series(np.random.randn(time_to_relax.days), index=time_to_relax_range)
print(time_to_relax_series.tail())
ave_dictionary = {"A":20, "B":-20, "C":666}
ave_dictionary_df = pd.DataFrame(ave_dictionary, index=["start", "finish"])
print(ave_dictionary_df)