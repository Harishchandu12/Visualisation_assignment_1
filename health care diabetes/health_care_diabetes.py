# import library
import matplotlib.pyplot as plt
import pandas as pd
import inspect
import os.path


# get current dir
def get_file_path():
    """
    This function returns the current path directory
    """
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    path = os.path.dirname(os.path.abspath(filename))
    return path


# read csv
input_path = str(get_file_path())+r"\health_care_diabetes.csv"

# add csv file to dataframe
df_health = pd.read_csv(input_path)


def age_group(df_row):
    """
    Returs the dataframe with age_group category from  the source data

    Parameters
    ----------

    df_row[] : Pandas.series shows an 'Age' column which is in the row dataframe


    Returns
    -------
    str: returs the dataframe with age_group category to which the age belongs

    """
    if df_row['Age'] < 30:
        age_group = '<30'
    elif df_row['Age'] >= 30 and df_row['Age'] < 40:
        age_group = '30-40'
    elif df_row['Age'] >= 40 and df_row['Age'] < 50:
        age_group = '40-50'
    elif df_row['Age'] >= 50 and df_row['Age'] < 60:
        age_group = '50-60'
    elif df_row['Age'] >= 60 and df_row['Age'] < 70:
        age_group = '60-70'
    else:
        age_group = '>70'
    return age_group


df_health['age_group'] = df_health.apply(age_group, axis=1)

df_outcome_agg = df_health.groupby(
    ['age_group'])['Outcome'].sum().reset_index(name='Total_Count')


x = df_outcome_agg['age_group']
y = df_outcome_agg['Total_Count']
explode = [0.05] * 6

# Add labels and plotting pie chart
colors = ['red', 'green', 'pink', 'grey', 'lightblue', 'purple']
plt.pie(y, labels=x, colors=colors, autopct='%1.1f%%',
        pctdistance=0.65, explode=explode)

# Adding a title
plt.title('Total Diabetes cases among different age groups', fontsize=15)

# displaying the pie chart
plt.show()
