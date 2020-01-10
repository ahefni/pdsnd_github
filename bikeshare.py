import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#CSV File
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_DATA = ('january','february','march','april','may','june')

#User input
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = str(input('Would you like to see data for Chicago, New York, or Washington?\n')).lower()
            if city not in CITY_DATA:
                print('That is not a valid input')
            else:
                break
        except ValueError:
            print('That is not a valid input')
        except KeyboardInterrupt:
            print('Bye Bye')
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = str(input('Would you like to see data for January, February ,..., June? Type all to select all months\n')).lower()
            if month not in MONTH_DATA and month != 'all':
                print('That is not a valid input')
            else:
                break
        except ValueError:
            print('That is not a valid input')
        except KeyboardInterrupt:
            print('Bye Bye')
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = str(input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? Type all to select all days\n')).lower()
            if day not in ('monday','tuesday','wednesday','thursday','friday','saturday','sunday','all'):
                print('That is not a valid input')
            else:
                break
        except ValueError:
            print('That is not a valid input')
        except KeyboardInterrupt:
            print('Bye Bye')
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    df["Start End Station"] = df['Start Station'].map(str) + ', ' + df['End Station'].map(str)
    if month != 'all':
        months = MONTH_DATA
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('The most common month: ',df['month'].mode()[0])

    # display the most common day of week
    print('The most common day: ',df['day_of_week'].mode()[0])

    # display the most common start hour
    print('The most common start hour: ',df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('Most commonly used start station: ',df['Start Station'].mode()[0])

    # display most commonly used end station
    print('Most commonly used end station: ',df['End Station'].mode()[0])


    # display most frequent combination of start station and end station trip
    print('Most frequent combination of start station and end station trip: ',df['Start End Station'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('total travel time: ', df['Trip Duration'].sum())

    # display mean travel time
    print('mean travel time: ',df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('counts of user types: ', df['User Type'].value_counts())

    # Display counts of gender
    if 'Gender' in df.columns:
        print('counts of gender: ', df['Gender'].value_counts())

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('earliest year of birth: ', df['Birth Year'].min())
        print('most year of birth: ', df['Birth Year'].max())
        print('most common of birth: ', df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df,first_request=0):
    while True:
        try:
            display_rows = str(input('Would you like to see %s data from the selected sheet? Enter yes or no.\n'%('some' if first_request == 0 else 'the following'))).lower()
            if display_rows not in ['yes', 'no']:
                print('That is not a valid input')
            else:
                break
        except ValueError:
            print('That is not a valid input')
        except KeyboardInterrupt:
            print('Bye Bye')
            break

    if display_rows == 'yes':
        print(df[first_request:first_request+5])
        first_request = first_request + 5
        display_data(df,first_request)



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
