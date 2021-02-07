# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 21:05:15 2021

@author: avry_
"""


import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')

#salary parsing
#Company name text only
#statefield
#age of company
#parsing of job description (python, etc.)


###SALARY PARSING###

#Make new folders for hourly and employer pro. dan menambahkan
#nilai 1 untuk tabel salary estimate yang mengandung Hourly dan empl
df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary' in x.lower() else 0)


#Remove -1 
df = df[df['Salary Estimate'] != '-1']

#Remove Glassdoor est.
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])

#Remove Minus and $ Symbol
minus_Kd = salary.apply(lambda x: x.replace('K','').replace('$',''))

#Remove per hour in salary estimate
min_hr = minus_Kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))

#Split the range numbers to 2 columns min, max and make avg column as well
df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df['min_salary']+df['max_salary'])/2

###COMPANY NANE TEXT ONLY###

#company names have numbers on it so we must create another one to split it from the number

df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis = 1)

##STATE FIELD###
#Split the location with code
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1])
df.job_state.value_counts()

#Same state with headquearter or not ?
df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis =1)

##AGE OF COMPANY ##

df['age'] = df.Founded.apply(lambda x: x if x <1 else 2020 - x)

## PARSING OF JOB DESCRIPTION (PYTHON, ETC.) ##

#python?
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
#R Studio ?
df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'R Studio' in x.lower() else 0)
#Spark ?
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
#aws ?
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
#excel ?
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)

df.columns

#Remove unnamed row
df_out = df.drop(['Unnamed: 0'], axis =1)

#Import to csv
df_out.to_csv('salary_data_cleaned.csv',index = False)
