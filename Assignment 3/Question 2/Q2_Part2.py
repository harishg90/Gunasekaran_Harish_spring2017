from pandas import Series, DataFrame
import pandas as pd

dataset=pd.read_csv('C:/Users/ABC/DataAnalysis4Python_Spring17/Assignments/Assignment 3/Data/employee_compensation.csv', sep=',', skiprows=(1,1))
df = DataFrame(dataset[dataset.apply(lambda x: x['Year Type'] == 'Calendar', axis = 1)])
df1 = df.groupby('Employee Identifier')['Salaries', 'Overtime', 'Other Salaries', 'Total Salary', 'Retirement', 'Health/Dental', 'Other Benefits', 'Total Benefits','Total Compensation'].mean()
df1 = df1[df1.apply(lambda x: x['Overtime'] > 0.05 * x['Salaries'], axis = 1)]
df1 = DataFrame(df1.index.get_level_values('Employee Identifier'))

job_family = df1.merge(df, on = 'Employee Identifier')['Job Family'].unique()
df2 = df[df['Job Family'].isin(job_family)]
df2 = df2.groupby('Job Family')['Total Benefits', 'Total Compensation'].mean()

# df2 = df1.merge(df, on = 'Employee Identifier').groupby('Job Family')['Total Benefits', 'Total Compensation'].mean()

df2['Percent_Total_Benefit'] = df2['Total Benefits'] * 100 / df2['Total Compensation']
df2.sort_values(by='Percent_Total_Benefit', ascending=False).head(n=5)
df2.to_csv('Q2_Part2Output.csv', sep=',', encoding='utf-8')