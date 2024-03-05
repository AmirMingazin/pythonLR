import openpyxl
import pandas as pd

import statsmodels.api as sm
workbook = openpyxl.load_workbook('mydata.xlsx')


sheet = workbook.active


hours = []
exams = []
score = []


for row in sheet.iter_rows(values_only=True):
    hours.append(row[0])
    exams.append(row[1])
    score.append(row[2])
hours.pop(0)
exams.pop(0)
score.pop(0)

print("Массив из первого столбца:", hours)
print("Массив из второго столбца:", exams)
print("Массив из третьего столбца:", score)
df = pd.DataFrame({'hours1': hours,
                   'exams1': exams,
                   'score1': score})

#view data
df



#define response variable
y = df['score1']

#define predictor variables
x = df[['hours1', 'exams1']]

#add constant to predictor variables
x = sm.add_constant(x)

#fit linear regression model
model = sm.OLS(y, x).fit()

#view model summary
print(model.summary())