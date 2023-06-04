import pandas as pd
from data_prep import data_scrapper
#
DIET_COSTS=data_scrapper.get_data_csv_specific_columns(f"data/food_costs_2017.csv",["Country Name","Cost of an energy sufficient diet","Cost of a nutrient adequate diet","Cost of a healthy diet"],'latin-1')
FOOD_COSTS =data_scrapper.get_data_csv_specific_columns(f"data/food_costs_2017.csv",["Country Name","Cost of fruits","Cost of vegetables","Cost of starchy staples","Cost of animal-source foods"],'latin-1')
PEOPLE_UNAFFORDABLE_DIET_SHARE = data_scrapper.get_data_csv_specific_columns(f"data/food_costs_2017.csv",["Country Name","Percent of the population who cannot afford sufficient calories","Percent of the population who cannot afford nutrient adequacy","Percent of the population who cannot afford a healthy diet"],'latin-1')
LAND_USE_1000KCAL = data_scrapper.get_data_csv_specific_columns(f"data/land-use-kcal-poore.csv",["Entity","Land use per 1000kcal (m2)"],'latin-1')
ARABLE_LAND = data_scrapper.get_data_csv_specific_columns(f"data/arable-land-%-2017.csv",["Country Name","Arable land (%)"],'latin-1')
print(ARABLE_LAND)

MEAT_PRODUCTION= data_scrapper.scrape_table_data("https://ourworldindata.org/grapher/global-meat-production?tab=table&time=2017",data_scrapper.adjust_unit,[1])
CEREAL_PRODUCTION=data_scrapper.scrape_table_data("https://ourworldindata.org/grapher/cereal-production?tab=table&time=2017",data_scrapper.adjust_unit,[1])
POPULATION = data_scrapper.scrape_table_data("https://ourworldindata.org/grapher/meat-consumption-vs-gdp-per-capita?tab=table&time=2017",data_scrapper.adjust_number,[3])
MEAT_CONSUMPTION_GDP_PER_CAPITA=data_scrapper.scrape_table_data("https://ourworldindata.org/grapher/meat-consumption-vs-gdp-per-capita?tab=table&time=2017",data_scrapper.adjust_unit,[1,2])
DIETARY_COMPOSITION = data_scrapper.scrape_table_data("https://ourworldindata.org/grapher/dietary-compositions-by-commodity-group?tab=table&time=2017",data_scrapper.adjust_unit,[5,6,7,8,9,10,4,3,2,1])
RISK_FACTORS = data_scrapper.scrape_table_data("https://ourworldindata.org/grapher/number-of-deaths-by-risk-factor?tab=table&time=2017",data_scrapper.adjust_unit,[2,3,4,6,14,17,19])

print(CEREAL_PRODUCTION)
print(POPULATION)
print(DIETARY_COMPOSITION)
print(RISK_FACTORS)

