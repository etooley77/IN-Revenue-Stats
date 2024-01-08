import matplotlib.pyplot as pyplot
import numpy

month_dictionary = {
    0 : 'July',
    1 : 'August',
    2 : 'September',
    3 : 'October',
    4 : 'November',
    5 : 'December',
    6 : 'January',
    7 : 'February',
    8 : 'March',
    9 : 'April',
    10 : 'May',
    11 : 'June'
}

yearly_revenue_lists = [
    # Fiscal Year 2023
    [
        [2023],
        # [(Month, shown as a number starting with July as 0), (Actual Revenue), (Revenue Forecast), (Difference), (Percent Error)]
        # July
        [0, 1482.8, 1330.1, 152.7, 11.5],
        # August
        [1, 1549.5, 1348.5, 201.0, 14.9],
        # September
        [2, 1879.0, 1783.4, 95.6, 5.4, ],
        # October
        [3, 1654.1, 1376.7, 277.4, 20.2],
        # November
        [4, 1352.0, 1230.5, 121.5, 9.9],
        # December
        [5, 1711.9, 1539.9, 172.0, 11.2],
        # January
        [6, 1943.6, 1801.9, 141.7, 7.9],
        # February
        [7, 1220.0, 995.2, 224.8, 22.6],
        # March
        [8, 1499.7, 1278.6, 221.1, 17.3],
        # April
        [9, 2859.2, 2580.2, 279.0, 10.8],
        # May
        [10, 1541.2, 1324.3, 216.9, 16.4],
        # June
        [11, 2365.3, 2237.1, 128.2, 5.7],
        # Year-to-Date
        [21058.2, 18826.3, 2231.9, 11.9]
    ],
    # Fiscal Year 1967
    [
        [2022],
        # [(Month, shown as a number starting with July as 0), (Actual Revenue), (Revenue Forecast), (Difference), (Percent Error)]
        # July
        [0, 1482.8, 1330.1, 152.7, 11.5],
        # August
        [1, 1549.5, 1348.5, 201.0, 14.9],
        # September
        [2, 1879.0, 1783.4, 95.6, 5.4, ],
        # October
        [3, 1654.1, 1376.7, 277.4, 20.2],
        # November
        [4, 1352.0, 1230.5, 121.5, 9.9],
        # December
        [5, 1711.9, 1539.9, 172.0, 11.2],
        # January
        [6, 1943.6, 1801.9, 141.7, 7.9],
        # February
        [7, 1220.0, 995.2, 224.8, 22.6],
        # March
        [8, 1499.7, 1278.6, 221.1, 17.3],
        # April
        [9, 2859.2, 2580.2, 279.0, 10.8],
        # May
        [10, 1541.2, 1324.3, 216.9, 16.4],
        # June
        [11, 2365.3, 2237.1, 128.2, 5.7],
        # Year-to-Date
        [21058.2, 18826.3, 2231.9, 11.9]
    ]
]

chosen_year = input('Type in a year in the format "2023" : ')

# finding_chosen_year takes the first value of the first list in the found year. Then it prints it.

finding_chosen_year = [year[0][0] for year in yearly_revenue_lists if year[0][0] == chosen_year]

for found_year in finding_chosen_year:
    print(found_year)

for index, outer_list in enumerate(yearly_revenue_lists):
    for inner_list in outer_list[0]:
        if inner_list == int(chosen_year):
            found_year_index = index


year = yearly_revenue_lists[found_year_index]

# The function to present the user with the graph for the Actual and Forecast Revenue Data for the specified year

def revenue_graph(rounded_average_actual_revenue, rounded_average_forecast_revenue):
    pyplot.plot([month[1] for month in year[1:13]])
    pyplot.plot([month[2] for month in year[1:13]])
    pyplot.title('Monthly Actual Revenue (FY2023)')

    pyplot.text(6, 4600, f'Average Actual : {rounded_average_actual_revenue}', fontsize=12)
    pyplot.text(5.7, 4200, f'Average Forecast : {rounded_average_forecast_revenue}', fontsize=12)

    pyplot.grid(True, linestyle='solid', alpha=0.5)

    pyplot.ylabel('Monthly Revenue (in millions of US Dollars)')
    pyplot.ylim(500, 5000)

    pyplot.xlabel('Month (starting from July as 0)')
    pyplot.xlim(-1, 12)
    custom_x_ticks = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    pyplot.xticks(custom_x_ticks)

    for month in year[1:13]:
        x = month[0]
        y = month[1]
        pyplot.scatter(x, y, color='blue', label=f'{x}, {y}')
    for month in year[1:13]:
        x = month[0]
        y = month[2]
        pyplot.scatter(x, y, color='orange', label=f'{x}, {y}')

    pyplot.legend(fontsize='small', ncol=2, loc='upper left')
    pyplot.show()

# The function to present the user with the graph for the Percent Error of Fiscal Year 2023

def percent_error_graph(rounded_average_percent_error):
    pyplot.plot([month[4] for month in year[1:13]])
    pyplot.title('Monthly Percent Error (FY2023)')

    pyplot.text(6, 90, f'Average Error : {rounded_average_percent_error}%', fontsize=12)

    pyplot.grid(True, linestyle='solid', alpha=0.5)

    pyplot.ylabel('Percent Error')
    pyplot.ylim(0, 100)

    pyplot.xlabel('Month (starting from July as 0)')

    pyplot.xlim(-1, 12)
    custom_x_ticks = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    pyplot.xticks(custom_x_ticks)

    for month in year[1:13]:
        x = month[0]
        y = month[4]
        pyplot.scatter(x, y, color='blue', label=f'{x}, {y}%')
    
    pyplot.legend(fontsize='small', loc='upper left', ncol=1)
    pyplot.show()

# The function for accessing both the Actual/Forecast Revenue and Percent Error Graphs for Fiscal Year 2023

def graphs():
    # Some of the usability functions 

    def go_back():
        print('Go back (y/n)')
        go_back = input('Type here : ')

        if go_back == 'y':
            graphs()
        elif go_back == 'n':
            pass
        else:
            go_back = input('Type here : ')

# Crunching the numbers
            
# Printing the year
            
    print(f'Year : {chosen_year}')
            
# Actual Revenue Data

    average_actual_revenue = numpy.mean([month[1] for month in year[1:13]])
    rounded_average_actual_revenue = round(average_actual_revenue, 1)
    print(f'Average Actual Revenue : ${rounded_average_actual_revenue}')

    maximum_actual_revenue = numpy.max([month[1] for month in year[1:13]])
    maximum_actual_revenue_index = [month[1] for month in year[1:13]].index(maximum_actual_revenue)
    maximum_actual_revenue_month = month_dictionary[maximum_actual_revenue_index]
    print(f'Maximum Actual Revenue : ${maximum_actual_revenue} in {maximum_actual_revenue_month}')

    minimum_actual_revenue = numpy.min([month[1] for month in year[1:13]])
    minimum_actual_revenue_index = [month[1] for month in year[1:13]].index(minimum_actual_revenue)
    minimum_actual_revenue_month = month_dictionary[minimum_actual_revenue_index]
    print(f'Minimum Actual Revenue : ${minimum_actual_revenue} in {minimum_actual_revenue_month}\n')

# Forecast Revenue Data

    average_forecast_revenue = numpy.mean([month[2] for month in year[1:13]])
    rounded_average_forecast_revenue = round(average_forecast_revenue, 1)
    print(f'Average Revenue Forecast : ${rounded_average_forecast_revenue}')

    maximum_forecast_revenue = numpy.max([month[2] for month in year[1:13]])
    maximum_forecast_revenue_index = [month[2] for month in year[1:13]].index(maximum_forecast_revenue)
    maximum_forecast_revenue_month = month_dictionary[maximum_forecast_revenue_index]
    print(f'Maximum Forecast Revenue : ${maximum_forecast_revenue} in {maximum_forecast_revenue_month}')

    minimum_forecast_revenue = numpy.min([month[2] for month in year[1:13]])
    minimum_forecast_revenue_index = [month[2] for month in year[1:13]].index(minimum_forecast_revenue)
    minimum_forecast_revenue_month = month_dictionary[minimum_forecast_revenue_index]
    print(f'Minimum Forecast Revenue : ${minimum_forecast_revenue} in {minimum_forecast_revenue_month}\n')

# Percent Error Data

    average_percent_error = numpy.mean([month[4] for month in year[1:13]])
    rounded_average_percent_error = round(average_percent_error, 1)
    print(f'Average Percent Error : {rounded_average_percent_error}%')

    maximum_percent_error = numpy.max([month[4] for month in year[1:13]])
    maximum_percent_error_index = [month[4] for month in year[1:13]].index(maximum_percent_error)
    maximum_percent_error_month = month_dictionary[maximum_percent_error_index]
    print(f'Maximum Percent Error : {maximum_percent_error}% in {maximum_percent_error_month}')

    minimum_percent_error = numpy.min([month[4] for month in year[1:13]])
    minimum_percent_error_index = [month[4] for month in year[1:13]].index(minimum_percent_error)
    minimum_percent_error_month = month_dictionary[minimum_percent_error_index]
    print(f'Maximum Percent Error : {minimum_percent_error}% in {minimum_percent_error_month}')

# Separator

    print('\U00012605 \U00012605 \U00012605 \U00012605 \U00012605 \U00012605 \U00012605 \U00012605 \U00012605 \U00012605 \U00012605 \U00012605 \U00012605 \U00012605 \U00012605 \U00012605  \n')

# Choices

    print('Show me the Actual/Forecast Revenue Graph (a)')
    print('Show me the Percent Error Graph (b)')
    choice = input('Type your choice here : ')

    if choice == 'a':
        revenue_graph(rounded_average_actual_revenue, rounded_average_forecast_revenue)

        print('\n')
        go_back()
    elif choice == 'b':
        percent_error_graph(rounded_average_percent_error)

        go_back()
    else:
        choice = input('Type your choice here : ')

graphs()