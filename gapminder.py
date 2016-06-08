import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

from utility import load_data
from utility import trans_data
from utility import merge_by_year
from utility import income_region
from utility import income_distr

def main():
    """
    This function is to present the results of this assignment.
    Users will ask to see:
    1)Income distribution across all countries for a given year:
      Users need to input a year from 1800 to 2012.
      Results will be saved as a .png file.
    2)Income distribution by region in recent years:
      Users need to input the first year, last year and year gap in a year rangeand select a plot type, boxplot or histograms.
      Results will be saved as a .pdf file.
    """

    #load countries and income data
    countries = load_data('countries.csv')
    income = load_data('indicator gapminder gdp_per_capita_ppp.csv')
    #transform income data set
    income = trans_data(income)

    try:
        while raw_input('To see income distribution across all countries? (y/n) ') == 'y':
            try:
                year = raw_input('Which year? ') #select a year
                income_distr(income, year)
            except:
                print 'Please input a year from 1800 to 2012'
        
        while raw_input('To see income distribution by region in recent years? (y/n) ') == 'y':
            try:
                from_year = int(raw_input('From which year? ')) #input the first year
                to_year = int(raw_input('To which year? ')) #input the last year
                year_gap = int(raw_input('Year gap? ')) #input a year gap
                pltype = raw_input('Plot type: boxplots or histograms? (b/h) ') #select a plot type
                if pltype == 'b':
                    pp = PdfPages('results/Income by region from {0} to {1}_boxplot.pdf'.format(from_year, to_year)) #create a pdf file to save plots
                    for i in xrange(from_year, to_year+1, year_gap):
                        fig = income_region(1,str(i))
                        pp.savefig(fig)
                elif pltype == 'h':
                    pp = PdfPages('results/Income by region from {0} to {1}_hist.pdf'.format(from_year, to_year))
                    for i in xrange(from_year, to_year+1, year_gap):
                        fig = income_region(0, str(i))
                        plt.suptitle('{}'.format(i))
                        pp.savefig(fig)
                pp.close() #close the pdf file
            except:
                print 'please input years from 1800 to 2012 and try again!'

    except(KeyboardInterrupt):
        print 'Bye!'
        sys.exit()

if __name__ == '__main__':
    main()