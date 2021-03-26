import matplotlib.pyplot as plt

plt.style.use('bmh')

province = ['punjab','sindh','kpk','Balochistan','Islamabad']
population = [52,18,20,10,26]
explode = [0,0.025,0,0,0]

color=['#118DFF','#99E4AD','#FB87A2','brown','green']

plt.pie(population,labels=province ,shadow=True
    ,explode=explode, colors=color,autopct="%1.1f%%", wedgeprops={'edgecolor':'black'})

plt.title("PAKISTAN ADMINISTRATIVE UNIT")
plt.legend(loc=(0.05,0.07))
plt.tight_layout()
plt.show()