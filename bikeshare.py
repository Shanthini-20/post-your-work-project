
# Bikeshare Data Analysis Program
# This script allows users to explore bikeshare data
# by city, month, and day of the week.
``

import time
import pandas as pd

# CITY_DATA maps city names to their CSV files
CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')

    city = input('Enter city (chicago, new york city, washington): ').lower()
    while city not in CITY_DATA:
        city = input('Please enter a valid city: ').lower()

    month = input('Enter month (all, january, february, ..., june): ').lower()
    day = input('Enter day of week (all, monday, tuesday, ... sunday): ').lower()

    print('-' * 40)
    return city, month, day

def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name().str.lower()
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()

    if month != 'all':
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day]

    return df

def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    print('Most common month:', df['month'].mode()[0])
    print('Most common day:', df['day_of_week'].mode()[0])
    print('Most common start hour:', df['Start Time'].dt.hour.mode()[0])

    print("This took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def station_stats(df):
    print('\nCalculating The Most Popular Stations...\n')
    print('Most common start station:', df['Start Station'].mode()[0])
    print('Most common end station:', df['End Station'].mode()[0])

def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    print('Total travel time:', df['Trip Duration'].sum())
    print('Average travel time:', df['Trip Duration'].mean())

def user_stats(df):
    print('\nCalculating User Stats...\n')
    if 'User Type' in df.columns:
        print(df['User Type'].value_counts())

    if 'Gender' in df.columns:
        print(df['Gender'].value_counts())

    if 'Birth Year' in df.columns:
        print('Earliest year:', int(df['Birth Year'].min()))
        print('Most recent year:', int(df['Birth Year'].max()))
        print('Most common year:', int(df['Birth Year'].mode()[0]))

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nRestart? (yes/no): ').lower()
        if restart != 'yes':
            break

if __name__ == "__main__":
    main()
