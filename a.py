# from wfml import Task

# task = Task.init(project_name="some-project",reuse_last_task_id=False)

# print("WFML")

# task.close()


import pandas as pd 
import matplotlib.pyplot as plt 
df = pd.DataFrame() 
for a in range(2):
    df[str(a)] = range(0,10)
fig = df.plot(x="0", y="1", kind="bar").figure
fig.savefig("x.png")