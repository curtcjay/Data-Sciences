import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_data(filename):
    """
    This function is to load a csv data
    """
    fpath = 'data/' + filename
    return pd.read_csv(fpath)

def trans_data(df):
    """
    This function is to transform a data set
    df: dataframe to be transformed
    """
    df = df.set_index(df.columns[0])
    df = df.T
    return df

def merge_by_year(year):
    """
    This function is to merge the countries and income data sets for any given year.
    year: to merge data sets for this given year
    """
    countries = load_data('countries.csv')
    income = load_data('indicator gapminder gdp_per_capita_ppp.csv')
    income = trans_data(income)
    income_year = income.ix[year]
    income_year_df = pd.DataFrame(income_year)
    income_year_df = income_year_df.reset_index()
    merged_df = pd.merge(countries, income_year_df, how="inner", left_on=countries.columns[0],right_on=income_year_df.columns[0])
    merged_df = merged_df.drop(income_year_df.columns[0], axis = 1)
    merged_df = merged_df.dropna() #drop null data
    return merged_df

def income_distr(income_df, year):
    """
    This function is to display the distribution of income per person across all countries for any given year, using histograms.
    Attributes:
    income_df: income dataframe
    year: year selected, from 1800 to 2012, e.g. 2008
    
    Note: after calling this function, the plot will be saved as a .png file
    """

    income_year = income_df.ix[year]
    income_year = income_year.dropna() #drop null data
    income_year.hist(bins = 40, color = 'grey', edgecolor = 'DarkGrey')
    plt.ylabel('Number of Countries')
    plt.xlabel('Income per person')
    plt.title('The Distribution of Income per person in {}'.format(year))
    plt.savefig('results/Income distribution in {}.png'.format(year))

def income_region(boxplot, year):
    """
    This function is to explore the distribution of the income per person by region for a given year using boxplots or histograms.
    
    Attributes:
    year: year selected, from 1800 to 2012, e.g. 2008
    boxplot: 1 for boxplot; 0 for histogram.
    """
    
    merged = merge_by_year(year) #merge the data sets for a given year
    if boxplot == 1:
        ax = merged.boxplot(by='Region') #by region
        fig = ax.get_figure()
    elif boxplot == 0:
        ax = merged.hist(by='Region', bins = 15, xlabelsize=8, xrot=45)
        fig = ax[0][0].get_figure()
    return fig