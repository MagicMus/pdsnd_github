import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello!! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
def get_user_inputs():
    valid_cities = ['chicago', 'new york city', 'washington']

    while True:
        city = input("Please choose a City (Chicago, New York City, Washington): ").lower()
        if city in valid_cities:
            break
        else:
            print("Spelling mistake. Please enter again.")

    print("You have chosen", city.capitalize())

    # TO DO: get user input for month (all, january, february, ... , june)
    valid_months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

    while True:
        month = input("Please enter the name of a month (All, January, February, March, April, May, June): ").lower()
        if month in valid_months:
            break
        else:
            print("Spelling mistake. Please enter again.")

    print("You have chosen", month.capitalize())

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    valid_days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    while True:
        day = input("Please enter a specific day or choose All  (All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday): ").lower()
        if day in valid_days:
            break
        else:
            print("Spelling mistake. Please enter again.")

    print("You have chosen", day.capitalize())

    print('-'*40) 

    return city, month, day
user_inputs = get_user_inputs()


def display_data(df):
    """
    Displays raw data if the user specifies that they want to see it.
    """
    # Prompt the user to see raw data
    raw_data_prompt = input("Would you like to see the raw data? Enter 'yes' or 'no': ") 
    if raw_data_prompt.lower() == 'yes':
        # Display the first 5 rows of data
        print(df.head())
    # Initialize a counter to keep track of rows
        row_counter = 5
        # Continue prompting until the user chooses 'no'
        while True:
            # Prompt the user to see more data
            more_data_prompt = input("Would you like to see 5 more rows? Enter 'yes' or 'no': ")
            if more_data_prompt.lower() == 'yes':
                # Display the next 5 rows of data
                print(df[row_counter:row_counter+5])
                row_counter += 5
            else:
                break

# Load the Chicago data
chicago_df = pd.read_csv('chicago.csv')

# Load the Washington data
washington_df = pd.read_csv('washington.csv')         
                
 # Load the New York City data
new_york_city_df = pd.read_csv('new_york_city.csv')         

# Prompt the user to choose which city's data they want to see
city_prompt = input("Which city's data would you like to see? Enter 'chicago' or 'washington' or 'new york city: ")

# Display the data based on the user's choice
if city_prompt.lower() == 'chicago':
    display_data(chicago_df)
elif city_prompt.lower() == 'washington':
    display_data(washington_df)
elif city_prompt.lower() == 'new york city':
    display_data(new_york_city_df)
else:
    print("Invalid input. Please enter 'chicago' or 'washington' or 'new york city'.")

                                   
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

    return df

df = load_data(user_inputs[0], user_inputs[1], user_inputs[2])

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

print('\nCalculating The Most Frequent Times of Travel...\n')
start_time = time.time()
df['Start Time'] = pd.to_datetime(df['Start Time'])
    # TO DO: display the most common month
df['month'] = df['Start Time'].dt.month
most_common_month = df['month'].mode()[0]
print("The most common month is:", most_common_month)
    # TO DO: display the most common day of week
df['most_common_day'] = df['Start Time'].dt.weekday
most_common_day = df['most_common_day'].value_counts().idxmax()
day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
most_common_day_name = day_names[most_common_day]

print("The most common day is:", most_common_day_name)
    

    # TO DO: display the most common start hour
df['hour'] = df['Start Time'].dt.hour
most_common_hour = df['hour'].mode()[0]
print('Most Common Start Hour:', most_common_hour)
print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

print('\nCalculating The Most Popular Stations and Trip...\n')
start_time = time.time()

    # TO DO: display most commonly used start station
most_common_start_station = df['Start Station'].mode()[0]
print("The most commonly used start station is:", most_common_start_station)
    # TO DO: display most commonly used end station
most_common_end_station = df['End Station'].mode()[0]
print("The most commonly used end station is:", most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
df['Most frequent combination'] = df['Start Station'] + ' to ' + df['End Station']
most_frequent_combination = df['Most frequent combination'].mode()[0]
print("The most frequent combination of start station and end station trip is:", most_frequent_combination)
print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

print('\nCalculating Trip Duration...\n')
start_time = time.time()

    # TO DO: display total travel time
df['Start Time'] = pd.to_datetime(df['Start Time'])
df['End Time'] = pd.to_datetime(df['End Time'])
    
df['Travel Time'] = df['End Time'] - df['Start Time']
total_travel_time = df['Travel Time'].sum()
print("The total travel time is:", total_travel_time)

    # TO DO: display mean travel time
mean_travel_time = df['Travel Time'].mean()
mean_travel_time = df['Travel Time'].mean()
print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

print('\nCalculating User Stats...\n')
start_time = time.time()

    # TO DO: Display counts of user types
user_types = df['User Type'].value_counts()
print(user_types)
    # TO DO: Display counts of gender
    # Check if 'Gender' column exists in the DataFrame
if 'Gender' in df.columns:
    gender_counts = df['Gender'].value_counts()
    print(gender_counts)
else:
# Display a message indicating that gender count is not available
    print("Gender count is not available for the Washington.")
    # TO DO: Display earliest, most recent, and most common year of birth
# Check if 'Birth Year' column exists in the DataFrame
if 'Birth Year' in df.columns:
    earliest_birth_year = df['Birth Year'].min()
    most_recent_birth_year = df['Birth Year'].max()
    most_common_birth_year = df['Birth Year'].mode()[0]

    print("The earliest year of birth is:", earliest_birth_year)
    print("The most recent year of birth is:", most_recent_birth_year)
    print("The most common year of birth is:", most_common_birth_year)
    
else:
# Display a message indicating that birth year is not available 
    print("Birth Year is not available for the Washington dataset.")    
    

print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)

def get_filters():
    city = input("Enter the city: ").lower()
    month = input("Enter the month: ").lower()
    day = input("Enter the day: ").lower()
    return city, month, day

def main():
    while True:
        city, month, day = get_filters()
        
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
