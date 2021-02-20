import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#CITY_DATA=pd.read_csv(F:\udacity\chicago.csv)
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    city = ''
    while city not in CITY_DATA.keys():
        print("\nPlease choose your city:")
        print("\n1. Chicago 2. New York City 3. Washington")
        city = input().lower()
        if city not in CITY_DATA.keys():
            print("\nPlease check your input")
        print('city is',city)
        
        MONTH_DATA = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
    month = ''
    while month not in MONTH_DATA.keys():
        print("\nPlease enter the month between January to June:")
        month = input().lower()
        if month not in MONTH_DATA.keys():
            print("\nYou have entered wrong month.")
            print("\n You have entered",month)
        
    DAY_LIST = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = ''
    while day not in DAY_LIST:
        print("\nPlease enter a day in the week:")
        day = input().lower()
        if day not in DAY_LIST:
            print("\n You have entered wrong day")
            
        print("\n You have entered ",day)
        print('-'*80)
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
    print('\nLoading the data...\n')
    #df = pd.read_csv("F:\\udacity\\chicago.txt")
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df

def time_status(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    print("Most Popular Month : {popular_month}")
    df['month'] = df['Start Time'].dt.month
    print(df['month'].mode()[0])
    
    # TO DO: display the most common day of week
    print("\nMost Popular Day: {popular_day}")
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    print(df['day_of_week'].mode()[0])
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print(df['hour'].mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used start station: ")
    print(df['Start Station'].mode()[0])
    
    # TO DO: display most commonly used end station
    print("\nThe most commonly used end station:")
    print(df['End Station'].mode()[0])
        
    # TO DO: display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    print("\nThe most frequent combination of trips are from:")
    print(df['Trip'].mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    print("The total trip duration is {total_duration}: ")
    print(df['Trip Duration'].sum())
    
    # TO DO: display mean travel time
    print("The average trip duration is {total_duration}: ")
    print(round(df['Trip Duration'].mean()))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_status(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # TO DO: Display counts of user types
    print("The types of users by number are given below:\n")
    print(df['User Type'].value_counts())
    
    # TO DO: Display counts of gender
    try:
        print("\nThe types of users by gender are given below:\n")
        print(df['Gender'].value_counts())
    except:
        print("\nThere is no 'Gender' column")
    
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print("\nThe earliest year of birth:\n")
        print(int(df['Birth Year'].min()))
        print("\nThe recent year of birth:\n")
        print(int(df['Birth Year'].max()))
        print("\nThe common year of birth:\n")
        print(int(df['Birth Year'].mode()[0]))
    except:
        print("There is no birth year column")
    print("\nThis took %s seconds." % (time.time() - start_time))
    
def show_raw_data(df):
    '''method to print the selected data frame, 5 at a time '''
    choice = input("Would you like to see raw data? [Y/n] : ")
    choice = choice.upper()

    start = 0
    if choice == 'Y':
        for row in df.iterrows():
            print(row)
            start += 1
            if start != 0 and start % 5 == 0:
                choice = input("Would you like to see raw data? [Y/n] : ")
                if choice.upper() != 'Y':
                    break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_status(df)
        station_stats(df)
        trip_duration_stats(df)
        user_status(df)
        show_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


main()