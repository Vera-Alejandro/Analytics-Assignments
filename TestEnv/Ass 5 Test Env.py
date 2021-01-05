import pandas as pd

books = pd.read_csv(())

#Edit the P
P_cards =[ #SL  ,S1   ,S2   ,S3   ,S12  ,S13  ,S23  ,SW
          [1.000,0.333,0.333,0.333,0.000,0.000,0.000,0.000],
          [0.000,0.000,0.000,0.000,0.333,0.333,0.000,0.000],
          [0.000,0.000,0.000,0.000,0.333,0.000,0.333,0.000],
          [0.000,0.000,0.000,0.000,0.000,0.333,0.333,0.000],
          [0.000,0.333,0.333,0.000,0.000,0.000,0.000,0.000],
          [0.000,0.333,0.000,0.333,0.000,0.000,0.000,0.000],
          [0.000,0.000,0.333,0.333,0.000,0.000,0.000,0.000],
          [0.000,0.000,0.000,0.000,0.333,0.333,0.333,1.000]
         ]

#Edit the P
P = [[1.0,0.0,0.0,0.0,0.0],
     [0.5,0.0,0.5,0.0,0.0],
     [0.0,0.5,0.0,0.5,0.0],
     [0.0,0.0,0.5,0.0,0.5],
     [0.0,0.0,0.0,0.0,1.0]]

#Edit the P
P = [[1.0,0.0,0.0,0.0,0.0],
     [0.4,0.0,0.6,0.0,0.0],
     [0.0,0.5,0.0,0.5,0.0],
     [0.0,0.0,0.5,0.0,0.5],
     [0.0,0.0,0.0,0.0,1.0]]




#put each product into its own list here.
#put each product into its own list here.
meat1 = df['hamburgers']
meat2 = df['brats']
meat3 = df['pork']
meat4 = df['steaks']
meat5 = df['chicken']
meat6 = df['lamb']

#plot each list holding the product data. Label appropriately, set marker to o, and the linewidth to 3.
plt.plot(monthList, meat1, 'o-', lw='3', label='Hamburgers Sales Data')
plt.plot(monthList, meat2, 'o-', lw='3', label='Brats Sales Data')
plt.plot(monthList, meat3, 'o-', lw='3', label='Pork Sales Data')
plt.plot(monthList, meat4, 'o-', lw='3', label='Steak Sales Data')
plt.plot(monthList, meat5, 'o-', lw='3', label='Chicken Sales Data')
plt.plot(monthList, meat6, 'o-', lw='3', label='Lamb Sales Data')

plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.legend(loc='upper left')
plt.xticks(monthList)
plt.yticks([1000, 2000, 4000, 6000, 8000, 10000, 12000, 15000, 18000])
plt.title('Sales data')
plt.show()