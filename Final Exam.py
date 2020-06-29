#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 12:14:59 2020

@author: sebastian_soman
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# read in covid-19 data
covid_df = pd.read_csv('us-states.csv')
covid_df

# convert the 'date' column to datetime format 
covid_df['date']= pd.to_datetime(covid_df['date'])
# query data from Pennsylvania
covid_df = covid_df.loc[covid_df['state'] == 'Pennsylvania']
covid_df = covid_df.reset_index(drop=True)
# create Series of 'deaths' column
adj_deaths = pd.Series(covid_df['deaths'].values)
covid_df['adj_deaths'] = adj_deaths.values
covid_df
# subtract April 21 deaths by 282
covid_df.loc[(covid_df.date == '2020-04-21'), 'adj_deaths'] = adj_deaths - 282
# subtract April 22 deaths by 297
covid_df.loc[(covid_df.date == '2020-04-22'), 'adj_deaths'] = adj_deaths - 297
covid_df

# create bar chart (run this chunk of code together)
plt.figure(figsize=(15, 7))
ax = plt.gca()
x = covid_df['date']
y = covid_df['adj_deaths']
plt.xlabel('Date')
plt.ylabel('Deaths')
plt.title('Pa. coronavirus deaths')
formatter = mdates.DateFormatter("%Y-%m-%d")
ax.xaxis.set_major_formatter(formatter)
ax.xaxis.set_major_locator(mdates.WeekdayLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
plt.bar(x, y)
plt.xticks(fontsize=10)

