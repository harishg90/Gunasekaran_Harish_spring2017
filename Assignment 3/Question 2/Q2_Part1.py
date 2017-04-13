from pandas import Series, DataFrame
import pandas as pd

df1=pd.read_csv('C:/Users/ABC/DataAnalysis4Python_Spring17/Assignments/Assignment 3/Data/employee_compensation.csv', sep=',', skiprows=(1,1))
#DataFrame({'Total Compensation' : df1.groupby( [ "Organization Group", "Department"] ).size()}).reset_index()

dfq2=DataFrame(df1.groupby(["Organization Group", "Department"])['Total Compensation'].mean())
dfq2.sort_values(by='Total Compensation', ascending=False)

dfq2.to_csv('Q2_Part1Output.csv', sep=',', encoding='utf-8')
dfq2.head()