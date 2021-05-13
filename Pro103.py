import pandas as pd
import plotly.express as px

df = pd.read_csv("covidData.csv")
fig = px.scatter(df,x="date", y = "cases", color="country", title="Covid cases", size="cases", size_max=10)
fig.show()
