import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
print(fiddy_states[0]["Name Abbreviation"])
# df.plot()
# plt.show()