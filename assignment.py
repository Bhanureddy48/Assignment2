import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb 

def dataframe_generate(r):
    data=pd.read_csv(r)
    d1=data.drop(['Country Code','Indicator Name','Indicator Code'],axis=1)
    d2=d1
    d2= d2.set_index('Country Name', drop=True)
    d2=d2[['1965','1975','1985','1995','2000','2005','2010','2015']]
    d2=d2.transpose()
    return d1,d2

data1,data2=dataframe_generate('country_population.csv')
data2=data2.reset_index()
data2=data2[['index','Albania','Arab World','South Africa','Zambia','Vietnam','Zimbabwe']]
data1.describe()
data2.describe()
data1=data1[['Country Name','1965','1975','1985','1995','2000','2005','2010','2015']]
country=data1['Country Name'].tolist()
year=data2['index'].tolist()
data2=data2.set_index('index')
mean_1965=np.mean(data2.loc['1965'].tolist())
mean_1975=np.mean(data2.loc['1975'].tolist())
mean_1985=np.mean(data2.loc['1985'].tolist())
mean_1995=np.mean(data2.loc['1995'].tolist())
mean_2000=np.mean(data2.loc['2000'].tolist())
mean_2005=np.mean(data2.loc['2005'].tolist())
mean_2010=np.mean(data2.loc['2010'].tolist())
mean_2015=np.mean(data2.loc['2015'].tolist())
mean_year=[mean_1965,mean_1975,mean_1985,mean_1995,mean_2000,mean_2005,mean_2010,mean_2015]
plt.figure(figsize=(5, 4))
plt.scatter(year, mean_year)
plt.plot(year, mean_year)
plt.title("yearly growth of population")
plt.show()
South_Africa=data2['South Africa'].tolist()
Zimbabwe=data2['Zimbabwe'].tolist()
Albania=data2['Albania'].tolist()
Arab_World=data2['Arab World'].tolist()
Zambia=data2['Zambia'].tolist()
Vietnam=data2['Vietnam'].tolist()
plt.figure(figsize=(10, 3))
plt.subplot(1,2,1)
plt.plot(year, South_Africa, linestyle='--',color='red')
plt.title('South Africa population over year')
plt.subplot(1,2,2)
plt.plot(year,Zimbabwe, linestyle='--')
plt.title('Zimbabwe population over year')
plt.show()
dataplot = sb.heatmap(data2.corr(), cmap="YlGnBu", annot=True) 
plt.show() 
plt.figure(figsize=(7, 4))
plt.plot(year, South_Africa, label="South_Africa")
plt.plot(year,Zimbabwe, label="Zimbabwe")
plt.plot(year,Albania, label="Albania")
plt.plot(year,Arab_World, label="Arab World")
plt.plot(year,Zambia, label="Zambia")
plt.plot(year,Vietnam, label="Vietnam")
plt.title("Population growth in different countries")
plt.xlabel("YEAR")
plt.ylabel("Population growth")
plt.legend()
plt.show()
data3=data1[0:5]
data3_con=data3['Country Name'].tolist()
data3_1965=data3['1965'].tolist()
data3_1975=data3['1975'].tolist()
data3_1985=data3['1985'].tolist()
data3_1995=data3['1995'].tolist()
data3_2000=data3['2000'].tolist()
data3_2005=data3['2005'].tolist()
data3_2010=data3['2010'].tolist()
data3_2015=data3['2015'].tolist()
bar_width = 0.025
loc = range(len(data3_con))
plt.figure(figsize=(10, 5))
plt.bar(loc,data3_1965, bar_width, label="1965")
plt.bar([i+ bar_width for i in loc],data3_1975, bar_width, label="1975")
plt.bar([i +2* bar_width for i in loc],data3_1985, bar_width, label="1985")
plt.bar([i +3* bar_width for i in loc],data3_1995, bar_width, label="1995")
plt.bar([i +4* bar_width for i in loc],data3_2000, bar_width, label="2000")
plt.bar([i +5* bar_width for i in loc],data3_2005, bar_width, label="2005")
plt.bar([i +6* bar_width for i in loc],data3_2010, bar_width, label="2010")
plt.bar([i +7* bar_width for i in loc],data3_2015, bar_width, label="2015")
plt.xlabel("Year")
plt.ylabel("fertility rate")
plt.title("Comparison of Average fertility rate accross different country")
plt.xticks([i + bar_width / 2 for i in loc], data3_con, rotation=45)
plt.legend()
plt.tight_layout()
plt.show()