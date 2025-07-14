# Imports
import pandas as pd
import matplotlib.pyplot as plt

# Analyzing weather patterns.
# Load in the seattle_weather.csv as seattle_weather.
# Load in the austin_weather.csv as austin_weather.
seattle_weather = pd.read_csv("seattle_weather.csv")
austin_weather = pd.read_csv("austin_weather.csv")

# Initializing subplots
fig, ax = plt.subplots(2,2)

# Addressing the top left Axes as index 0, 0, plot month and Seattle precipitation ('MLY-PRCP-NORMAL')
ax[0,0].plot(seattle_weather['MONTH'],
        seattle_weather['MLY-PRCP-NORMAL'])

# In the top right (index 0,1), plotting month and Seattle temperatures ('MLY_TAVG_NORMAL')
ax[0,1].plot(seattle_weather['MONTH'],
        seattle_weather['MLY-TAVG-NORMAL'])

# In the bottom left (1, 0), plotting month and Austin precipitations ('MLY-PRCP-NORMAL')
ax[1,0].plot(austin_weather['MONTH'],
        austin_weather['MLY-PRCP-NORMAL'])

# In the bottom right (1, 1), plotting month and Austin temperatures ('MLY_TAVG_NORMAL')
ax[1,1].plot(austin_weather['MONTH'],
        austin_weather['MLY-TAVG-NORMAL'])

# Call the show function.
plt.show()

# For precipitation, adding percentiles to give more information about the data distribution.
# Creating a figure and an array of axes: 2 rows, 1 column with shared y-axis
fig, ax = plt.subplots(2,1)

# Plotting Seattle precipitation data in the top axes. Plotting the 'MLY-PRCP-NORMAL'
# with color equal to blue ('b'). Plot 'MLY_PRCP-25PCTL' and 'MLY-PRCP-75-PCTL'
# with color equal to blue ('b') and linetype dashed ('--').
ax[0].plot(seattle_weather['MONTH'],
        seattle_weather['MLY-PRCP-NORMAL'],
           color='b')

ax[0].plot(seattle_weather['MONTH'],
        seattle_weather['MLY-PRCP-25PCTL'],
        color='b')

ax[0].plot(seattle_weather['MONTH'],
        seattle_weather['MLY-PRCP-75PCTL'],
           color='b')


# Plotting Austin precipitation data in the bottom axes. Plotting the 'MLY-PRCP-NORMAL'
# # with color equal to red ('r'). Plot 'MLY_PRCP-25PCTL' and 'MLY-PRCP-75-PCTL'
# # with color equal to red ('r') and linetype dashed ('--').
ax[1].plot(austin_weather['MONTH'],
        austin_weather['MLY-PRCP-NORMAL'],
           color='r')

ax[1].plot(austin_weather['MONTH'],
        austin_weather['MLY-PRCP-25PCTL'],
        color='r')

ax[1].plot(austin_weather['MONTH'],
        austin_weather['MLY-PRCP-75PCTL'],
           color='r')


# Call the show function.
plt.show()




# Advanced Customization with Matplotlib
# Load in the mens_rowing.csv as mens_rowing.
# Load in mens_gymnastics.csv as mens_gymnastics
mens_rowing = pd.read_csv("mens_rowing.csv")
mens_gymnastics = pd.read_csv("mens_gymnastics.csv")

# Create a fig and ax using subplots()
fig, ax = plt.subplots()

# Plotting a bar graph by computing mean and standard deviation of height
ax.bar('Rowing',
       mens_rowing['Height'].mean(),
       yerr=mens_rowing['Height'].std())

# Add a bar for the gymnastics "Height" column mean/std
ax.bar('Gymnastics',
       mens_gymnastics['Height'].mean(),
       yerr=mens_gymnastics['Height'].std())

# Label the y-axis
ax.set_ylabel('Height')

# Call the show function.
plt.show()



# Plotting for standard deviation present for data
fig, ax = plt.subplots()

# Add Seattle temperature data in each month with error bars
ax.errorbar(seattle_weather['MONTH'],
            seattle_weather['MLY-TAVG-NORMAL'],
            yerr=seattle_weather['MLY-TAVG-STDDEV'])

# Add Austin temperature data in each month with error bars
ax.errorbar(austin_weather['MONTH'],
            austin_weather['MLY-TAVG-NORMAL'],
            yerr=austin_weather['MLY-TAVG-STDDEV'])

# Set the y-axis label
ax.set_ylabel('Tempreture')

# Call the show function.
plt.show()





# Seaborn Customization
# Using pandas to load DC_bike_share.csv as bike_share
bike_share = pd.read_csv("DC_bike_share.csv")

# Creating the crosstab DataFrame to build a table of visits by group and year.
# Creating a crosstab dataframe of bike_share by 'temp' and  'mnth'. Round temp to one
bike_share['temp'] = bike_share['temp'].round(1)

bike_matrix = pd.crosstab(bike_share['temp'],
                          bike_share['mnth'],
                          values=bike_share['total_rentals'],
                          aggfunc='mean').round(0)


# Import seaborn and alias it sns
import seaborn as sns

# Plotting a heatmap of the crosstab dataframe with no color bar (cbar)
sns.heatmap(bike_matrix, cmap='BuGn',
            cbar = False, linewidths=0.3)
plt.xticks(rotation=90)
plt.yticks(rotation=0)

# Show the plot
plt.show()



# FacetGrids
# Load in the college_datav3.csv as college_data.
college_data = pd.read_csv("college_datav3.csv")

# Creating a FacetGrid that shows a point plot of the Average
g = sns.FacetGrid(college_data,row='Degree_Type',row_order=['Graduate', 'Bachelors', 'Associates', 'Certificate'])


# Using the .map() method of a seaborn FacetGrid type, Map a pointplot of SAT_AVG_ALL onto the grid
g.map(sns.pointplot, 'SAT_AVG_ALL')

# Show the plot
plt.show()



# Catplot()
# Creating a factor plot that contains boxplots of Tuition values
sns.catplot(x='REGION', y='Tuition', data=college_data, row="Degree_Type", kind='box')

# Show the figure
plt.show()




# Lmplot
g = sns.FacetGrid(college_data,col='Degree_Type',col_order=['Graduate', 'Bachelors', 'Associates', 'Certificate'])

# Map a scatter plot of the Undergrad Population (‘UG’) compared to PCTPELL
g.map(plt.scatter, 'UG','PCTPELL')

# Show the plot
plt.show()

sns.lmplot(data=college_data, x='UG', y='PCTPELL',
           col='Degree_Type', fit_reg=True)

# Show the plot
plt.show()


# Creating a facetted lmplot() comparing SAT_AVG_ALL to Tuition
sns.lmplot(data=college_data,
           x='Tuition', y='SAT_AVG_ALL',
           col='Ownership',row='Degree_Type',
           fit_reg=True, hue='WOMENONLY')

# Show the plot
plt.show()




# PairGrids()
# To create pairplot using the auto insurance data
insurance_data = pd.read_csv('insurance_premiums.csv')

g = sns.PairGrid(insurance_data, vars=['fatal_collisions', 'premiums'])

g = g.map(sns.scatterplot)

# Show the plot
plt.show()

# Create another PairGrid by plotting a histogram on the diagonal and scatter plot on the off-diagonal.
g = sns.PairGrid(insurance_data, vars=['fatal_collisions', 'premiums'])
g = g.map_diag(sns.histplot)
g = g.map_offdiag(sns.scatterplot)

# Show the plot
plt.show()


# Create a pairwise plot of the variables using a scatter plot
sns.pairplot(insurance_data, vars=['fatal_collisions', 'premiums'],
             kind='scatter')

# Show the plot
plt.show()

# Plot the same data but use a different color palette and color code by Region
sns.pairplot(insurance_data, vars=['fatal_collisions', 'premiums'],
             kind='scatter', hue='Region', palette='RdBu')

# Show the plot
plt.show()

# Creating a pair plot that examines fatal_collisions_speeding and fatal_collisions_alc on the x-axis, and premiums and
# insurance_losses on the y-axis.

sns.pairplot(insurance_data,
             x_vars=['fatal_collisions_speeding', 'fatal_collisions_alc'],
             y_vars=['premiums','insurance_losses'],
             kind='scatter',
             hue='Region', palette='RdBu')

# Show the plot
plt.show()


#JointGrid
sns.set_style('whitegrid')

g = sns.JointGrid(data=bike_share,
                  x='hum', y='total_rentals')

# Plot a regplot() and histplot() on the margins.
g.plot(sns.regplot, sns.histplot)

# Show the plot
plt.show()





# Jointplot
sns.jointplot(data=bike_share,
              x='hum', y = 'total_rentals',
              kind = 'reg')

# Show the plot
plt.show()


# Creating a jointplot with a scatter plot comparing temp and casual riders
sns.jointplot(data=bike_share,
              x='temp', y = 'casual',
              kind = 'scatter',
              marginal_kws = dict(bins=10)).plot_joint(sns.kdeplot, alpha=0.5)


# Show the plot
plt.show()