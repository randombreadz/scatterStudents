import pandas as pd
import plotly.express as px
import csv

df = pd.read_csv("Student.csv")

student_df = df.loc[df['student_id'] == "TRL_987"]
print(student_df.groupby("level")["attempt"].mean())

fig = px.scatter(df, x = "student_id", y = "level", size = "attempt", color = "attempt")

fig.show()
  