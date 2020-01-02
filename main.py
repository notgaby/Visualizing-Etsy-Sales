import pandas as pd
import matplotlib.pyplot as plt; plt.rcdefaults()
import ast
import numpy as np

data = pd.read_csv("Alldata.csv", na_values=['no info','.'])

productTitle = pd.DataFrame()

bts = 0
wallArt = 0
babyShower = 0
custom = 0

#months
january = 0
february = 0
march = 0
april = 0
may = 0
june = 0
july = 0
august = 0
september = 0
october = 0
november = 0
december = 0

#test
janWA = 0
janBTS = 0
janBS = 0

febWA = 0
febBTS = 0
febBS = 0

marWA = 0
marBTS = 0
marBS = 0

aprWA = 0
aprBTS = 0
aprBS = 0

mayWA = 0
mayBTS = 0
mayBS = 0

junWA = 0
junBTS = 0
junBS = 0

julWA = 0
julBTS = 0
julBS = 0

augWA = 0
augBTS = 0
augBS = 0

sepWA = 0
sepBTS = 0
sepBS = 0

octWA = 0
octBTS = 0
octBS = 0

novWA = 0
novBTS = 0
novBS = 0

decWA = 0
decBTS = 0
decBS = 0



#word = "lol"
#if(word.__contains__('l')):
#   print("yes")


for index, row in data.iterrows():

   prodType = data.iloc[index]['product title']
   monthBought = data.iloc[index]['date']
   prodType = str(prodType)
   monthBought = str(monthBought)

   if prodType.__contains__('wall'):
       wallArt += 1
       if monthBought.__contains__('Jsn'):
           january+=1
           janWA+=1
       elif monthBought.__contains__('Feb'):
           february +=1
           febWA+=1
       elif monthBought.__contains__('Mar'):
           march +=1
           marWA+=1
       elif monthBought.__contains__('Apr'):
           april +=1
           aprWA +=1
       elif monthBought.__contains__('May'):
           may +=1
           mayWA +=1
       elif monthBought.__contains__('Jun'):
           june +=1
           junWA+=1
       elif monthBought.__contains__('Jul'):
           july +=1
           julWA +=1
       elif monthBought.__contains__('Aug'):
           august +=1
           augWA +=1
       elif monthBought.__contains__('Sep'):
           september +=1
           sepWA +=1
       elif monthBought.__contains__('Oct'):
           october +=1
           octWA +=1
       elif monthBought.__contains__('Nov'):
           november +=1
           novWA +=1
       elif monthBought.__contains__('Dec'):
           december +=1
           decWA +=1


   elif prodType.__contains__('school'):
       bts +=1
       if monthBought.__contains__('Jsn'):
           january+=1
           janBTS+=1
       elif monthBought.__contains__('Feb'):
           february +=1
           febBTS+=1
       elif monthBought.__contains__('Mar'):
           march +=1
           marBTS+=1
       elif monthBought.__contains__('Apr'):
           april +=1
           aprBTS +=1
       elif monthBought.__contains__('May'):
           may +=1
           mayBTS +=1
       elif monthBought.__contains__('Jun'):
           june +=1
           junBTS+=1
       elif monthBought.__contains__('Jul'):
           july +=1
           julBTS +=1
       elif monthBought.__contains__('Aug'):
           august +=1
           augBTS +=1
       elif monthBought.__contains__('Sep'):
           september +=1
           sepBTS +=1
       elif monthBought.__contains__('Oct'):
           october +=1
           octBTS +=1
       elif monthBought.__contains__('Nov'):
           november +=1
           novBTS +=1
       elif monthBought.__contains__('Dec'):
           december +=1
           decBTS +=1

   elif prodType.__contains__('baby'):
       babyShower +=1
       if monthBought.__contains__('Jsn'):
           january+=1
           janBS+=1
       elif monthBought.__contains__('Feb'):
           february +=1
           febBS+=1
       elif monthBought.__contains__('Mar'):
           march +=1
           marBS+=1
       elif monthBought.__contains__('Apr'):
           april +=1
           aprBS +=1
       elif monthBought.__contains__('May'):
           may +=1
           mayBS +=1
       elif monthBought.__contains__('Jun'):
           june +=1
           junBS+=1
       elif monthBought.__contains__('Jul'):
           july +=1
           julBS +=1
       elif monthBought.__contains__('Aug'):
           august +=1
           augBS +=1
       elif monthBought.__contains__('Sep'):
           september +=1
           sepBS +=1
       elif monthBought.__contains__('Oct'):
           october +=1
           octBS +=1
       elif monthBought.__contains__('Nov'):
           november +=1
           novBS +=1
       elif monthBought.__contains__('Dec'):
           december +=1
           decBS +=1




   #productTitle[] = data.iloc[index]['product title']
   #productTitle.append(data.iloc[index]['product title'])
   #addEnd = data.iloc[index]['product title']
   #data = ast.literal_eval(addEnd)
   #data = ast.literal_eval(data.iloc[index]['product title'])
   #productTitle = productTitle.append(pd.DataFrame(data, columns=['titles']),ignore_index=True)
#print(productTitle)
#print(data.iloc[0]['product title'])
#productTitle = data

total = wallArt+bts+babyShower


### pie chart -> product types

#"""

labels = 'Back to school signs', 'Baby shower', 'Wall art'
sizes = [(bts/total),(babyShower/total),(wallArt/total)]
explode = (0,0,0.2) #0.1 to make it "explode"

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode = explode, labels = labels, autopct = '%1.1f%%',
       shadow = True, startangle = 90)
ax1.axis('equal')
plt.show()

#"""

### bar graphs -> month bought

#"""
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('number of orders per month')
ax.set_xlabel('month')
ax.set_ylabel('orders')

x = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
y = [january, february, march, april, may, june, july, august, september, october, november, december]
ax.bar(x,y, color=plt.cm.plasma_r(y))

for a in range(0,12):
   num = str(y[a])
   ax.text(x[a],y[a],num, va = 'center', ha = 'left', bbox = dict(facecolor="w", alpha=.5))

plt.show()
#"""

"""

months = ('Aug', 'Sep', 'Dec', 'January', 'February')
y_pos = np.arange(len(months))
numOrders = [august, september, december, january, february]

plt.bar(y_pos,numOrders, align='center', alpha=.5)
plt.xticks(y_pos,months)
plt.ylabel('Number of orders')
plt.title('Months vs orders')

plt.show()

"""


### scatter plot -> month bought (with statistics)

#"""
months = ('Aug', 'Sep', 'Dec', 'January', 'February')
numOrders = [august, september, december, january, february]

plt.scatter(months,numOrders, edgecolors='r')
plt.xlabel('Month')
plt.ylabel('Orders')
plt.title('Number of orders per month')
plt.show()

#"""


# bar graph (months and products)

#"""
n_groups = 12 #months
wallA = (janWA,febWA,marWA,aprWA,mayWA,junWA,julWA,augWA,sepWA,octWA,novWA,decWA)
BTS = (janBTS,febBTS,marBTS,aprBTS,mayBTS,junBTS,julBTS,augBTS,sepBTS,octBTS,novBTS,decBTS)
BabS = (janBS,febBS,marBS,aprBS,mayBS,junBS,julBS,augBS,sepBS,octBS,novBS,decBS)

fig, ax = plt.subplots()
index = np.arange(n_groups)
barWidth = .4
opacity = .8

rectWA = plt.bar(index, wallA, barWidth, alpha = opacity, color = 'b', label = 'Wall art')
rectBTS = plt.bar(index, BTS, barWidth, alpha = opacity, color = 'r', label = 'Back to school')
rectBS = plt.bar(index, BabS, barWidth, alpha = opacity, color = 'g', label = 'Baby shower')

plt.xlabel('Month')
plt.ylabel('Number of orders')
plt.title('Order type per month')
plt.xticks(index + barWidth - .4, ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
plt.legend()



plt.tight_layout()
plt.show()

#"""







