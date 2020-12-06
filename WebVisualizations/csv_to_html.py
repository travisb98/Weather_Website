import pandas as pd 


#CSV path
cities_path="WebVisualizations/Resources/cities.csv"
# reading the csv path to a df
cities_df = pd.read_csv(cities_path, encoding="UTF-8")


  
# to save as html file 
# named as "Table" 
cities_df.to_html("WebVisualizations/Resources/city.html",index=False) 
  