import pandas as pd
import wikipedia as wp

html = wp.page("List of S&P 500 companies").html().encode("UTF-8")
df = pd.read_html(html)[0]
df.to_csv('s&pIndustries.csv', header = 0, index = False)


