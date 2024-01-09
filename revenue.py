import matplotlib.pyplot as pyplot
import numpy

import sys
import time

def program():
    # Used to match indexes to the name of the month

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

    # A bunch of data that took me way too long to type out

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
            [2, 1879.0, 1783.4, 95.6, 5.4],
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
            ['YTD', 21058.2, 18826.3, 2231.9, 11.9]
        ],
        # Fiscal Year 2022
        [
            [2022],
            # [(Month, shown as a number starting with July as 0), (Actual Revenue), (Revenue Forecast), (Difference), (Percent Error)]
            # July
            [0, 1334.9, 1269.1, 65.8, 5.2],
            # August
            [1, 1376.2, 1272.6, 103.6, 8.1],
            # September
            [2, 1908.7, 1648.4, 260.3, 15.8],
            # October
            [3, 1370.5, 1233.2, 137.3, 11.1],
            # November
            [4, 1349.9, 1269.9, 80.0, 6.3],
            # December
            [5, 1663.4, 1485.2, 178.2, 12.0],
            # January
            [6, 2025.4, 1801.5, 223.9, 12.4],
            # February
            [7, 1135.3, 893.3, 242.0, 27.1],
            # March
            [8, 1462.9, 1238.9, 224.0, 18.1],
            # April
            [9, 3329.6, 2399.9, 929.7, 38.7],
            # May
            [10, 1732.4, 1425.7, 306.7, 21.5],
            # June
            [11, 2501.4, 2121.8, 379.6, 17.9],
            # Year-to-Date
            ['YTD', 21190.7, 18059.6, 3131.1, 17.3]
        ],
        # Fiscal Year 2021
        [
            [2021],
            # [(Month, shown as a number starting with July as 0), (Actual Revenue), (Revenue Forecast), (Difference), (Percent Error)]
            # July
            [0, 1999.3, 1190.9, 808.4, 67.9],
            # August
            [1, 1360.2, 1220.8, 139.4, 11.4],
            # September
            [2, 1621.5, 1625.4, 3.9, 0.2],
            # October
            [3, 1196.3, 1182.9, 13.4, 1.1],
            # November
            [4, 1233.1, 1222.4, 10.7, 0.9],
            # December
            [5, 1457.8, 1422.2, 35.5, 2.5],
            # January
            [6, 1822.8, 1585.4, 237.4, 15.0],
            # February
            [7, 1022.7, 916.1, 106.5, 11.6],
            # March
            [8, 1161.3, 1177.3, 16.0, 1.4],
            # April
            [9, 2230.4, 2253.1, 22.7, 1.0],
            # May
            [10, 1878.3, 1285.7, 592.6, 46.1],
            # June
            [11, 2423.8, 2041.9, 381.9, 18.7],
            # Year-to-Date
            ['YTD', 19407.4, 17124.1, 2283.3, 13.3]
        ],
        # Fiscal Year 2020
        [
            [2020],
            # [(Month, shown as a number starting with July as 0), (Actual Revenue), (Revenue Forecast), (Difference), (Percent Error)]
            # July
            [0, 1129.1, 1131.2, 2.1, 0.2],
            # August
            [1, 1114.1, 1073.3, 40.8, 3.8],
            # September
            [2, 1709.7, 1633.4, 76.3, 4.7],
            # October
            [3, 1188.1, 1153.3, 34.8, 3.0],
            # November
            [4, 1120.3, 1071.8, 48.5, 4.5],
            # December
            [5, 1531.4, 1516.1, 15.2, 1.0],
            # January
            [6, 1587.6, 1541.6, 46.0, 3.0],
            # February
            [7, 922.6, 905.4, 17.3, 1.9],
            # March
            [8, 1097.6, 1160.5, 62.9, 5.4],
            # April
            [9, 1234.2, 2220.2, 986, 44.4],
            # May
            [10, 952.4, 1172.1, 219.7, 18.7],
            # June
            [11, 1787.5, 2087.8, 300.3, 14.4],
            # Year-to-Date
            ['YTD', 15374.5, 16666.7, 1292.2, 7.8]
        ],
        # Fiscal Year 2019
        [
            [2019],
            # [(Month, shown as a number starting with July as 0), (Actual Revenue), (Revenue Forecast), (Difference), (Percent Error)]
            # July
            [0, 1172.1, 1167.2, 4.9, 0.4],
            # August
            [1, 1059.8, 1090.5, 30.7, 2.8],
            # September
            [2, 1607.8, 1496.5, 111.3, 7.4],
            # October
            [3, 1158.5, 1209.5, 51.0, 4.2],
            # November
            [4, 1048.1, 1059.1, 11.0, 1.0],
            # December
            [5, 1473.7, 1401.2, 72.5, 5.2],
            # January
            [6, 1491.8, 1511.2, 19.4, 1.3],
            # February
            [7, 786.4, 811.5, 25.1, 3.1],
            # March
            [8, 1149.3, 1134.7, 14.6, 1.3],
            # April
            [9, 2274.6, 2131.1, 143.5, 6.7],
            # May
            [10, 1139.7, 1192.7, 53.0, 4.4],
            # June
            [11, 2044.3, 1957.1, 87.3, 4.5],
            # Year-to-Date
            ['YTD', 16406.2, 16162.3, 243.9, 1.5]
        ],
        # Fiscal Year 2018
        [
            [2018],
            # [(Month, shown as a number starting with July as 0), (Actual Revenue), (Revenue Forecast), (Difference), (Percent Error)]
            # July
            [0, ],
            # August
            [1, ],
            # September
            [2, ],
            # October
            [3, ],
            # November
            [4, ],
            # December
            [5, ],
            # January
            [6, ],
            # February
            [7, ],
            # March
            [8, ],
            # April
            [9, ],
            # May
            [10, ],
            # June
            [11, ],
            # Year-to-Date
            ['YTD', ]
        ],
    ]

    # The end of the data!
    # The start of all of the fun stuff!

    chosen_year = int(input('Type in a year in the format "2023" : '))

    # finding_chosen_year takes the first value of the first list in the found year. Then it prints it.

    try:
        finding_chosen_year = [year[0][0] for year in yearly_revenue_lists]

        for found_year in finding_chosen_year:
            if found_year == chosen_year:
                print(found_year)
            else:
                pass

        for index, outer_list in enumerate(yearly_revenue_lists):
            for inner_list in outer_list[0]:
                if inner_list == chosen_year:
                    found_year_index = index

        year = yearly_revenue_lists[found_year_index]
    except NameError:
        print('No matches were found!')
        print('Please try again! Program will close in 3 seconds.')
        time.sleep(3)
        sys.exit()

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

        def rerun():
            print('Rerun the program (y/n)')
            rerun = input('Type here : ')

            if rerun == 'y':
                program()
            elif rerun == 'n':
                go_back()
            else:
                rerun = input('Type here : ')

        def go_back():
            print('Go back (y/n)')
            go_back = input('Type here : ')

            if go_back == 'y':
                graphs()
            elif go_back == 'n':
                rerun()
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
        print(f'Minimum Percent Error : {maximum_percent_error}% in {maximum_percent_error_month}')

        minimum_percent_error = numpy.min([month[4] for month in year[1:13]])
        minimum_percent_error_index = [month[4] for month in year[1:13]].index(minimum_percent_error)
        minimum_percent_error_month = month_dictionary[minimum_percent_error_index]
        print(f'Maximum Percent Error : {minimum_percent_error}% in {minimum_percent_error_month}')

    # Separator

        print('\U00012605 \U00012605 \U00012605 \U00012605 \U00012605 \U00012605 \U00012605 \U00012605 \U00012605 \U00012605 \U00012605 \U00012605 \U00012605 \U00012605 \U00012605 \U00012605  \n')

    # Choices

        print('Show me the Actual/Forecast Revenue Graph (a)')
        print('Show me the Percent Error Graph (b)')
        print('Or rerun the program with a different year (r)')
        choice = input('Type your choice here : ')

        if choice == 'a':
            revenue_graph(rounded_average_actual_revenue, rounded_average_forecast_revenue)

            print('\n')
            go_back()
        elif choice == 'b':
            percent_error_graph(rounded_average_percent_error)

            go_back()
        elif choice == 'r':
            print('\n')
            program()
        else:
            choice = input('Type your choice here : ')

    graphs()

program()