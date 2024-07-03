import pandas as pd
import numpy as np

#read data from ods
all_data = pd.read_excel('data_1_thread_loc.ods')
x_data = all_data['node'].dropna().to_numpy()
x_name = "number of node"
y_data = all_data['kg'].dropna().to_numpy()
y_name = "force, kg"

import matplotlib.pyplot as plt

#figure
fig, axes = plt.subplots()

#plot
axes.scatter(x_data, y_data, 'red')

#grid
plt.grid()

#additional
axes.set_xlabel(x_name)
axes.set_ylabel(y_name)
axes.set_title("dependence of tensile strength on the type of node");
axes.legend(['experimental data'])


#show
plt.show()

#save
#plt.savefig('')
