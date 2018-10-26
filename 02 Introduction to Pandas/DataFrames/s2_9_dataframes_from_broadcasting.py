import pandas as pd

counties = ['Antrim','Armagh','Carlow','Cavan','Clare','Cork','Derry','Donegal','Down','Dublin','Fermanagh','Galway',
            'Kerry','Kildare','Kilkenny','Laois','Leitrim','Limerick','Longford','Louth','Mayo','Meath','Monaghan',
            'Offaly','Roscommon','Sligo','Tipperary','Tyrone','Waterford','Westmeath','Wexford','Wicklow']

# Create a string with the value 'IRELAND'
country = "IRELAND"

# Create new dictionary
ireland = {'Country':country, 'County':counties}

# Create a DataFrame from the dictionary
df = pd.DataFrame(ireland)

print(df)
