import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

df_survey = pd.read_csv('Data_Science_Topics_Survey.csv')
df_survey.drop('Timestamp', axis=1, inplace=True)
results = {column.split("[")[1][:-1]:df_survey[column].value_counts() for column in df_survey.columns}
df_results = pd.DataFrame(results).transpose()
df_results.reset_index(inplace=True)
df_results.sort_values(by='index', inplace=True)
df_results.set_index('index', inplace=True)
df_results = df_results[['Very interested', 'Somewhat interested', 'Not interested']]
df_results.sort_values(by='Very interested', ascending=False, inplace=True)
df_results['Total'] = df_results.sum(axis=1)
for column in ['Very interested', 'Somewhat interested', 'Not interested']:
    df_results[column] = round((100*df_results[column])/df_results['Total'], 2)
del df_results['Total']

my_colors = ['#5cb85c', '#5bc0de', '#d9534f']
ax = df_results.plot(kind="bar", figsize=(20,8), width=0.8, color=my_colors)
ax.set_xticklabels(df_results.index, fontsize=14)
ax.set_title("Percentage of Respondents' Interest in Data Science Areas", fontsize=16)

ax.legend(fontsize=14)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.yaxis.set_ticks([])
rects = ax.patches
labels = np.array(df_results.transpose().values)
labels = np.concatenate((labels,), axis=None)
for rect, label in zip(rects, labels):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2, height+2, label,
            ha='center', va='bottom', fontsize=14)
