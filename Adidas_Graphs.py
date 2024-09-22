#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# In[2]:


ad = pd.read_csv(r"C:\Users\Himanshu\OneDrive\Documents\Imar Python\AdidasC.csv")


# In[3]:


ad.info()


# In[4]:


ad


# In[5]:


ad.Retailer.unique()


# In[6]:


ad.Total_Sales.mean()


# In[7]:


ad.Total_Sales.sum()


# In[8]:


Re = pd.DataFrame(ad.groupby('Region').Total_Sales.sum())
Re


# In[9]:


plt.figure(figsize = (8,5))
plt.pie(Re.Total_Sales , labels = Re.index , autopct = '%1.0f%%')
plt.title("Total Sales in each Region");
# this pie chart shows the total sales for all the regions


# In[10]:


Ra = pd.DataFrame(ad.groupby('Sales_Method').Total_Sales.sum())
Ra


# In[11]:


plt.figure(figsize = (8,5))
sns.barplot(x = Ra.Total_Sales , y = Ra.index)
plt.title("Total Sales through Sales Method");
# this bar graph shows the sales conducted by 


# In[12]:


ad.Product.value_counts()


# In[13]:


sns.countplot(x='Product',data=ad,order=ad['Product'].value_counts().index, hue='Sales_Method')
plt.xticks(rotation=90);


# In[14]:


ad.Units_Sold.sum()


# In[15]:


ad.Units_Sold.count()


# In[16]:


ad.Units_Sold.mean()


# In[17]:


ad.Units_Sold.median()


# In[18]:


sns.countplot(x = 'Retailer' , data = ad)
plt.title("Number of Customers")
plt.grid()


# In[19]:


sns.lineplot(x ='Region', y ='Operating_Margin', data = ad , marker='^')
plt.grid();


# In[20]:


ad.Operating_Profit.mean()


# In[21]:


ad.Operating_Profit.sum()


# In[22]:


ad.Operating_Profit.median()


# In[23]:


ad.Operating_Profit.count()


# In[24]:


ad.Operating_Profit.value_counts()


# In[25]:


sns.boxplot(x = 'Sales_Method' , y = 'Operating_Margin' , data = ad)
plt.title("Margins of each Sales Method")


# In[26]:


df6 = pd.DataFrame(ad.groupby('Region').Operating_Profit.mean())
df6


# In[27]:


plt.pie(df6.Operating_Profit , labels = df6.index , autopct = '%1.0f%%' , wedgeprops = dict(width = .5) )
plt.title("Regionwise Profit percentage")


# In[28]:


sns.violinplot(x = 'Sales_Method' , y = 'Units_Sold' , data = ad)
plt.title("Units Sold by each Method of Sales")


# In[29]:


plt.hist(ad.Operating_Margin , color = 'red' , bins = 20 , edgecolor = 'black')
plt.xlabel('Interval')
plt.ylabel('Margins')
plt.title('Interval in Operating Margin')


# In[30]:


sns.displot(ad.Units_Sold);


# In[31]:


plt.figure(figsize=(10,6))
plt.bar(ad.City , ad.Units_Sold , color = 'lime')
plt.xticks(rotation = 90)
plt.title("Units Sold in Cities");


# In[32]:


sns.pointplot(x = 'Product', y = 'Total_Sales', data = ad , color = 'gold' , hue = 'Sales_Method')
plt.grid()
plt.title("Total Sales on different Methods")
plt.xticks(rotation = 75);


# In[33]:


ad.Region.value_counts()


# In[34]:


ad.head()


# In[35]:


sns.jointplot(x = 'Operating_Margin' , y = 'Total_Sales' , data = ad , color = 'darkmagenta')


# In[36]:


plt.figure(figsize=(10,8))
sns.jointplot(x = 'Price_per _nit' , y = 'Units_Sold' , data = ad , kind = 'hex' , color = 'teal')


# In[37]:


sns.boxplot(x = 'Region' , y = 'Price_per _nit' , data = ad , hue = 'Sales_Method')
plt.title("Regionwise method of sales in price per unit");


# In[38]:


df2 = pd.DataFrame(ad.groupby('Retailer').Units_Sold.mean())
df2


# In[39]:


plt.figure(figsize=(10,6))
plt.bar(df2.index , df2.Units_Sold , color = ['chartreuse','lime','limegreen','forestgreen','green','darkgreen'])
plt.title("Mean Units sold by the Retailer")
plt.xlabel("Retailer")
plt.ylabel("Mean of units sold")


# In[40]:


plt.figure(figsize=(10,6))
sns.barplot(x = ad.State , y = ad.Operating_Margin)
plt.xticks(rotation = 90)
plt.title("Different Margins in different States")
plt.grid();


# In[41]:


df3 = pd.DataFrame(ad.groupby('City').Total_Sales.sum())

df3 = df3.sort_values('Total_Sales' , ascending = False)
df3


# In[42]:


df3.Total_Sales[0:10]


# In[43]:


df3.Total_Sales[-5:]


# In[44]:


plt.figure(figsize = (10,6))
plt.pie(df3.Total_Sales[0:10] , labels = df3.index[0:10] , autopct = '%1.0f%%' , explode = (.05,.05,0,0,0,0,0,0,0,0))
plt.title("Top 10 Total amount of Sales per City");


# In[45]:


plt.figure(figsize = (10,6))
sns.barplot(x = df3.index[-5:] , y = df3.Total_Sales[-5:])
plt.xticks(rotation = 75)
plt.title("Bottom 5 Total amount of Sales per City");


# In[46]:


plt.figure(figsize = (10,6))
sns.barplot(x = df3.index , y = df3.Total_Sales)
plt.xticks(rotation = 75)
plt.title("Total amount of Sales per City");


# In[47]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly


# In[48]:


import cufflinks as cf
import plotly.express 


# In[49]:


#!pip install cufflinks


# In[50]:


from plotly.offline import download_plotlyjs , init_notebook_mode , plot , iplot

init_notebook_mode(connected = True)   #  to connect to notebook
cf.go_offline()    ## to work offline
import plotly.express as px


# In[51]:


fig = px.sunburst(ad , path = ['Region' , 'State' , 'City'] , values = 'Total_Sales' , width = 700 , height = 700)
fig.show()


# In[52]:


fig1 = px.treemap(ad , path = ['Sales_Method' , 'Region' , 'City'] , values = 'Total_Sales' , width = 700 , height = 700)
fig1.show()


# In[53]:


ad.head()


# In[54]:


df1 = pd.DataFrame(ad.Retailer.value_counts())
df1.columns = ['count_of_retailer']


# In[55]:


df2 = pd.DataFrame(ad.Region.value_counts())
df2.columns = ['count_of_region']


# In[56]:


df3 = pd.DataFrame(ad.Product.value_counts())
df3.columns = ['count_of_product']


# In[57]:


df4 = pd.DataFrame(ad.Sales_Method.value_counts())
df4.columns = ['count_of_salesmethod']


# In[58]:


fig, ax = plt.subplots(nrows = 2 , ncols = 2 , figsize = (10,8) , constrained_layout = True)
ax[0,0].bar(df1.index , df1.count_of_retailer , color = 'darkmagenta')
ax[0,1].bar(df2.index , df2.count_of_region , color = 'cyan')
ax[1,0].bar(df3.index , df3.count_of_product , color = 'darkblue')
ax[1,1].bar(df4.index , df4.count_of_salesmethod , color = 'lime')

ax[0,0].tick_params(axis = 'x' , rotation = 45)
ax[0,1].tick_params(axis = 'x' , rotation = 45)
ax[1,0].tick_params(axis = 'x' , rotation = 75)
ax[1,1].tick_params(axis = 'x' , rotation = 0)

ax[0,0].title.set_text("Sales based on Retailer")
ax[0,1].title.set_text("Sales based on Region")
ax[1,0].title.set_text("Sales based on Product")
ax[1,1].title.set_text("Sales based on Sales Method");


# In[59]:


df5 = pd.DataFrame(ad.groupby('Sales_Method').Total_Sales.sum())
df5


# In[60]:


plotly.express.bar(df5 , x = df5.index , y = df5.Total_Sales , color = df5['Total_Sales'])


# In[61]:


ad.describe()


# In[62]:


fig = go.Figure(data = go.Scatter(x = ad['Total_Sales'] , y = ad['Price_per _nit']))
fig.update_layout(xaxis_title = 'Sales' , yaxis_title = 'Profit')
fig.show()


# In[ ]:




