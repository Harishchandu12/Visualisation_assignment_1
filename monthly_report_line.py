import matplotlib.pyplot as plt
import pandas as pd



# read csv
monthly_sales_input_df = pd.read_csv("C:\\Users\\chunc\\OneDrive\\Documents\\datasets\\Month_Value_1.csv")


# convert datetime string to date
monthly_sales_input_df["Period"] = pd.to_datetime(monthly_sales_input_df["Period"],format='%d.%m.%Y')


def year_2019_data(df):
    """
    Returns the dataframe with data of 2019 year from the source data frame with this specific schema.
    
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
    
    filtered_df_2019 = df.loc[(df['Period'] >= '2019-01-01') & (df['Period'] < '2020-01-01')]
    filtered_df_2019["Period"] = pd.to_datetime(filtered_df_2019["Period"]).dt.date
    return(filtered_df_2019)    


filtered_df_2019 = year_2019_data(monthly_sales_input_df)


def plot_report(df):
    """
    Generate custom plot for given data
    
    Parameters
    ----------
    df :        
        Data columns (total 5 columns):
            #   Column                                        Dtype  
            ---  ------                                        -----  
            0   Period                                        object 
            1   Revenue                                       float64
            2   Sales_quantity                                float64
            3   Average_cost                                  float64
            4   The_average_annual_payroll_of_the_region      float64
            types: float64(4), object(1)
            
    Returns
    -------
    none
        
    """
    plt.title('Monthly Report', fontsize=20)
    plt.xlim([1, 12])
    plt.ylim([5000, 50000])
    plt.xlabel('Month', fontsize=10)
    plt.ylabel('Sales_quantity', fontsize=10)
    plt.xticks(pd.to_datetime(filtered_df_2019["Period"]).dt.month)
    # Add a label for the legend
    plt.plot(pd.to_datetime(filtered_df_2019["Period"]).dt.month, filtered_df_2019["Sales_quantity"], color='red', label='Sales_quantity' )

    plt.grid(True)

    # Show the legend
    plt.legend()

    plt.show()
    

plot_report(filtered_df_2019)