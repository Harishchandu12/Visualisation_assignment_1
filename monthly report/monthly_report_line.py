import matplotlib.pyplot as plt
import pandas as pd
import inspect
import os.path


# get current dir
filename = inspect.getframeinfo(inspect.currentframe()).filename
path     = os.path.dirname(os.path.abspath(filename))

# read csv
# link for kaggle dataset : https://www.kaggle.com/datasets/podsyp/time-series-starter-dataset
input_path = path+"\Month_Value_1.csv"
monthly_sales_input_df = pd.read_csv(input_path)


# convert datetime string to date
monthly_sales_input_df["Period"] = pd.to_datetime(
    monthly_sales_input_df["Period"], format='%d.%m.%Y')


def year_data(df, year: str):
    """
    Returns the dataframe with data of the year from the source data frame with this specific schema.

    Parameters
    ----------
    df :  
        Data columns (total 5 columns):
         #   Column                                      Dtype         
        ---  ------                                      -----         
         0   Period                                      datetime64[ns]
         1   Revenue                                     float64       
         2   Sales_quantity                              float64       
         3   Average_cost                                float64       
         4   The_average_annual_payroll_of_the_region    float64       
        dtypes: datetime64[ns](1), float64(4)
    year : str 
        year of data    

    Returns
    -------
    df :        
        Data columns (total 5 columns):
     #   Column                                        Dtype  
    ---  ------                                        -----  
     0   Period                                        object 
     1   Revenue                                       float64
     2   Sales_quantity                                float64
     3   Average_cost                                  float64
     4   The_average_annual_payroll_of_the_region      float64
    dtypes: float64(4), object(1)
    """
    from_date = str(year)+'-01-01'
    to_date = str(int(year)+1)+'-01-01'

    # filter data for year
    filtered_df_year = df.loc[(df['Period'] >= from_date)
                              & (df['Period'] < to_date)]

    filtered_df_year["Period"] = pd.to_datetime(
        filtered_df_year["Period"]).dt.date
    return(filtered_df_year)


filtered_df_2015 = year_data(monthly_sales_input_df, '2015')
filtered_df_2016 = year_data(monthly_sales_input_df, '2016')
filtered_df_2017 = year_data(monthly_sales_input_df, '2017')
filtered_df_2018 = year_data(monthly_sales_input_df, '2018')
filtered_df_2019 = year_data(monthly_sales_input_df, '2019')

# define plot properties
plt.title('Monthly Report', fontsize=20)
plt.xlim([1, 12])
plt.ylim([5000, 50000])
plt.xlabel('Month', fontsize=10)
plt.ylabel('Sales_quantity', fontsize=10)
plt.xticks(pd.to_datetime(filtered_df_2018["Period"]).dt.month)

# plot the lines for respective years
plt.plot(pd.to_datetime(filtered_df_2015["Period"]).dt.month,
         filtered_df_2015["Sales_quantity"], color='red', label='2015')
plt.plot(pd.to_datetime(filtered_df_2016["Period"]).dt.month,
         filtered_df_2016["Sales_quantity"], color='orange', label='2016')
plt.plot(pd.to_datetime(filtered_df_2017["Period"]).dt.month,
         filtered_df_2017["Sales_quantity"], color='blue', label='2017')
plt.plot(pd.to_datetime(filtered_df_2018["Period"]).dt.month,
         filtered_df_2018["Sales_quantity"], color='green', label='2018')
plt.plot(pd.to_datetime(filtered_df_2019["Period"]).dt.month,
         filtered_df_2019["Sales_quantity"], color='black', label='2019')

plt.grid(True)

# Show the legend
plt.legend(loc='upper right')

plt.show()
