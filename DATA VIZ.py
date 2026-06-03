# Data Visualisation (Matplotlib and Seaborn)

"""
Matplotlib was designed by John Hunter as he felt the need of Matlab like plots in Python.
Matlab is a high level programming language and a numerical computer environment used by
engineers and scientists for data analysis, visualisation and algorithmic development.
Matplotlib was complex and difficult for beginners but was a powerful tool.
Thus Seaborn was created by Michael Waskom which is simple and easy to use.
Seaborn is a easier upgradation of Matplotlib.
Cufflinks was developed by Santiago Pallandino and was an upgradation of Seaborn.
"""

"""
Data Viz can be done using code or using tools.
Using code includes Matplotlib, Seaborn, Plotly, etc.
Very flexible and can be integrated into apps, ML pipelines, etc.
Using tools includes Power BI, Tableau, etc.
Limited to what the tool allows and very tough to integrate with ML pipelines.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Matplotlib Basics
"""Create 2 Arrays"""
x = np.linspace(-5, 5, 51)
y = x ** 2
print(x)
print(y)


plt.plot(x, y)
plt.title("Begin")
plt.xlabel("Numbers")
plt.ylabel("Their Squares")
plt.show()


# Subplots in Matplotlib
plt.subplot(2,2,1)
plt.plot(x**2, y**4)
plt.subplot(2,2,2)
plt.plot(x, y)
plt.subplot(2,2,3)
plt.plot(x, x)
plt.subplot(2,2,4)
plt.plot(y, x)
plt.show()

plt.subplot(6,6,1)
plt.plot(x*y, y)
plt.subplot(6,6,10)
plt.plot(x*y, y*69)
plt.subplot(6,6,20)
plt.plot(x*y, y*y*y)
plt.subplot(6,6,30)
plt.plot(x*x, y*y)
plt.subplot(6,6,36)
plt.plot(x*x, y*y)
plt.show()


# Object Oriented Way
fig = plt.figure(figsize=(12,8), dpi=100)

axis1 = fig.add_axes([0.1,0.1,0.8,0.8])
axis2 = fig.add_axes([0.3,0.2,0.6,0.6])

axis1.plot(x,y)
axis2.plot(y,x)

plt.show()


# Types of Plot

plt.scatter(x,y)
plt.show()

plt.hist(x)
plt.show()

plt.boxplot(x)
plt.show()

# Saving Plots
fig2 = plt.figure()
ax1 = fig2.add_axes([0.1,0.1,1,1])
ax1.plot(x,y)
plt.show()
#plt.savefig("basicplot.png")

# Working with Images
import matplotlib.image as mpimg

#img = mpimg.imread('<image_name>')
#plt.imshow(img)

#cropped_img = img[50:200,100:300]
#plt.imshow(cropped_img)


# Designing
plt.plot(x,y,color="pink",linewidth=0.25)
plt.show()

plt.plot(x,y,color="pink",linewidth=2)
plt.show()


# Seaborn
# Distribution Plots
"""
used for quantitative data
diff types :
displot / histplot
jointplot
pairplot
rugplot
"""

ssa = sns.load_dataset('tips')
print(ssa)

"""
here total_bill, tip are quantitative

sex, smoker, day, time, size are categorical
"""
ssb = ssa['size'].unique()
print(ssb)
plt.subplot(2,2,1)
sns.histplot(ssa['total_bill'], bins=20, kde=True)
plt.subplot(2,2,2)
sns.histplot(ssa['tip'], bins=20, kde=True)
plt.show()

# Joint Plot
sns.jointplot(x='total_bill', y='tip', data=ssa,kind='reg')
plt.show()

# Pair Plot
sns.pairplot(ssa,hue='size',palette='rainbow')
plt.show()

# Rug Plot
sns.rugplot(ssa['total_bill'])
plt.show()


# Categorical Plots
"""
boxplot
violinplot
stripplot
swarmplot
barplot
countplot
"""
# Count Plot
sns.countplot(x=ssa['sex'])
plt.show()
sns.countplot(x=ssa['sex'],hue=ssa['smoker'])
plt.show()

# Bar Plot
sns.barplot(x=ssa['sex'],y=ssa['tip'],estimator=np.sum)
plt.show()

# Box Plot
sns.boxplot(x='tip',y='day',data=ssa)
plt.show()

# Violin Plot
sns.violinplot(x='day',y='total_bill',data=ssa)
plt.show()

# Strip Plot
sns.stripplot(x='day',y='total_bill',data=ssa)
plt.show()

# Swarm Plot
sns.swarmplot(x='day',y='total_bill',data=ssa)
plt.show()

sns.violinplot(x='tip',y='day',data=ssa)
sns.swarmplot(x='tip',y='day',data=ssa)
plt.show()

# Matrix Plots
"""
heat map
cluster map
pivot table heat map
"""

flights = sns.load_dataset('flights')

# Heat Map
sss = ssa[['total_bill', 'tip', 'size']]
ssscorr = sss.corr()
print(ssscorr)
sns.heatmap(sss.corr(),annot=True)
plt.show()


# Cluster Map
""" Requires scipy """
sns.clustermap(sss.corr(),annot=True)
plt.show()

# Pivot Table Heat Map

print(flights)
pvtflight = flights.pivot_table(values='passengers',index='month',columns='year')
print(pvtflight)

sns.heatmap(pvtflight,cmap='viridis')

plt.show()

# Regression Plots
"""
used in ML
lmplot() is used to create regression plot
"""
sns.lmplot(x='total_bill',y='tip',data=ssa)
plt.show()

sns.lmplot(x='total_bill',y='tip',data=ssa,hue='sex',markers=['o', 'v'])
plt.show()

