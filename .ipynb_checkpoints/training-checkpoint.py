from datasets import load_dataset
import pandas as pd
import numpy as np


dataset = load_dataset('lukebarousse/data_jobs')
dataframe = dataset['train'].to_pandas()

# print(dataframe.info())
# print(dataframe[(dataframe.job_title == 'Data Analyst') & (dataframe.salary_year_avg > 100000)])
# print(dataframe.job_title_short.unique())
# dataAnalyst = dataframe[['job_title','salary_year_avg']][(dataframe.job_title_short == 'Data Analyst') & (dataframe.salary_year_avg > 100000) & (dataframe.salary_year_avg != 'NaN')]

# dataAnalystAvgSalary = np.mean(dataAnalyst.salary_year_avg)
# dataAnalystMinSalary = np.min(dataAnalyst.salary_year_avg)
# dataAnalystMaxSalary = np.max(dataAnalyst.salary_year_avg)
# print(dataAnalystAvgSalary.round(1))
# print(dataAnalystMaxSalary)
# print(dataAnalystMinSalary)
# print(dataAnalyst.count())

# print(pd.to_datetime(dataframe.job_posted_date))
# print(dataframe[['job_title_short','salary_year_avg']].sort_values(by='salary_year_avg',ascending=True)
# [(dataframe.job_title_short == 'Data Analyst')&(dataframe.salary_year_avg > 100_000)&(dataframe.salary_year_avg != 'NaN')])

# print(dataframe.drop(labels='job_title_short',axis=1))
print(dataframe.dropna(subset='salary_year_avg'),axis=1)
