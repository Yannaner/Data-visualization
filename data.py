#Basic usage
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("NVDA_data.csv")
data["timestamp"] = pd.to_datetime(data["timestamp"])
fig, ax = plt.subplots(1,1, figsize=(20,20))
fig.suptitle("NVDA stock", fontsize = 20,  color = "green")
ax.plot(data["timestamp"], data["trade_count"])

ax.legend()
ax.grid(visible=True,linestyle="--", color="blue",alpha=0.5)
plt.show()