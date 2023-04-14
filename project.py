import pandas as pd
import time


start=time.time()
citys ={"chicago":"chicago.csv",#Add chicago datafile 
       "new_york":"york_city.csv",#Add new_york datafile
       "washington":"washington.csv"}#Add washington datafile
cities=("chicago","new_york","washington")
months = ['january', 'february', 'march', 'april', 'may', 'june', 'august', 'september', 'october', 'november', 'december', 'all']
days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all']

def get_city():
    """ Asks the user to specify a city, month, and day.
        city -> name of the city
        month -> name of the month 
        day -> name of the day of
    """

    print('Hello! Let is explore some US bikeshare data!')
    # get user input for city (chicago, new york, washington)>>>
    while True:
        city=input("would you like to see\nnew_york, chicago or washington ?\n").lower()
        if city not in cities:
            print("Sorry,Please enter valid city.")
            continue
        else:
            break
    #get user input for month (All, January, February, March, April, May, June, August,...,December)
    while True:
        month = input("Enter the month you want to see. \nAll, January, February, March, April, May, June, August,...,December\n").lower()    
        if month not in months:
            print("Sorry,Please enter a valid month.")
            continue
        else:
            break
    #get user input for day of week (All, Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday)
    while True:
        day=input("Enter the day you want to see. \nAll, Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday\n").lower()
        if day not in days:
            print("Sorry,Please enter a valid day.")
            continue
        else:
            break 


    return city, month, day

def Data(city, month, day):
    #load data file
    data=pd.read_csv(citys[city])
    #convert the Start Time column to datetime(convert to int)
    data["Start Time"] = pd.to_datetime(data["Start Time"])
    #extract month from (Start Time) to create new columns
    data["ST month"] = data["Start Time"].dt.month
    #extract day from (Start Time) to create new columns
    data["ST days"] = data["Start Time"].dt.day_name()
    #extract Hour from (Start Time) to create new columns
    data["Hour"]=data["Start Time"].dt.hour
    #Merge (Start Station)+(End Station) put in (Start To End)
    data["Start To End"]=data["Start Station"] + " >to>> " +  data["End Station"]

    if month != "all":
    #use the index of the months list to get the corresponding int
        month = months.index(month) + 1
        data = data[data["ST month"] == month]
    if day != "all":
    #make day to create the new dataframe
        data = data[data["ST days"] == day.title()]  
    print("        loading time is {} seconds.".format(f"{time.time()-start:.4f}"))
    print("_"*60)

    return data

def Time(data):
    '''print statistics on the most times of travel'''
    #Calculate the code start time
    start=time.time()
    #display the most common month
    print("Most common month : {}".format(data["ST month"].mode()[0]))
    #display the most common day
    print("Most common day : {}.".format(data["ST days"].mode()[0]))
    #display the most common hour
    print("Most common hour : {} , And Count {}".format(data["Hour"].mode()[0],data["Hour"].value_counts().values[0]))
    #display the time start function
    print("this time is {} seconds.".format(f"{time.time()-start:.4f}"))

def station(data):
    '''Displays statistics on the most stations'''
    #Calculate the code start time
    start=time.time()
    #display the most common Start Station and count of it
    most_ST=data["Start Station"].mode()[0]
    print("Most common Start Station : {} , And Count {}".format(most_ST,data["Start Station"].value_counts()[most_ST]))
    #display the most common End Station and count of it
    most_SE=data["End Station"].mode()[0]
    print("Most common End Station : {} , And Count {}".format(most_SE,data["End Station"].value_counts()[most_SE]))
    #display the Most Common Trip from Start to End and count of it
    most_STE=data["Start To End"].mode()[0]
    print("Most Common Trip from Start to End: {} , And Count {}".format(most_STE,data["Start To End"].value_counts()[most_STE]))  
    #display the time start function
    print("this time is {} seconds.".format(f"{time.time()-start:.4f}"))

def trip(data):
    '''Displays statistics on the total and average trip'''
    #Calculate the code start time
    start=time.time()
    total_travel = data["Trip Duration"].sum()
    #display total travel time by seconds and count of it
    print("Tatal Travel time : {} Seconds , And Count {}".format(total_travel,data["Trip Duration"].value_counts().sum()))
    #display total travel time by Hours,Minutes,Seconds and count of it
    print("The Total Travel Time is {} Hours, {} Minutes, and {} seconds.".format(total_travel//3600,total_travel//60%60,total_travel%60))
    avg_travel = data["Trip Duration"].mean()
    avg_travel = float(f"{avg_travel:.2f}")
    #display Avg travel time by seconds and count of it
    print("Avg Travel time : {} Seconds".format(avg_travel))
    #display Avg travel time by Hours,Minutes,Seconds and count of it
    print("Avg Travel time : {} Hours, {} Minutes, and {} seconds.".format(avg_travel//3600,avg_travel//60%60,float(f"{avg_travel%60:.2f}")))
    #display the time start function
    print("this time is {} seconds.".format(f"{time.time()-start:.4f}"))

def user(data):
    '''Displays statistics on bikeshare users'''
    #Calculate the code start time
    start=time.time()
    print("User Type Stats:")
    #Display counts of user types
    print(data["User Type"].value_counts().to_string())
    #Display Gender of user types 
    if "Gender" in data.columns:
        print("Gender Stats:")
        print(data["Gender"].value_counts().to_string())
        
    else:
        print("Gender information is not available for this dataset.")
    if 'Birth Year' in data.columns:
    #Display earliest of user types
        print("Earliest Birth Year : {}".format(data['Birth Year'].min()))
    #Display most recent of user types
        print("Most recent Birth Year : {}".format(data['Birth Year'].max()))
    #Display most common of user types
        print("Most Common Year : {}".format(data['Birth Year'].mode()[0]))


    else:
        print("Earliest Year is not available for this dataset.")
        print("Most recent Birth Year is not available for this dataset.")
        print("Most Common Year is not available for this dataset.")
    #display the time start function
    print("this time is {} seconds.".format(f"{time.time()-start:.4f}"))

def individual_data(data):
    ''' Ask user if they want to see 5 individual trip data.'''

    #Calculate the code start time
    start=time.time()
    start_data = 0
    end_data = 5
    length = len(data.index)
    while start_data < length:
        raw_data = input("\nWould you like to see individual trip data? Enter 'yes' or 'no'.\n").lower()
        if raw_data == 'yes':
            print("\nDisplaying only 5 rows of data.\n")
            if end_data > length:
                end_data = length
            print(data.iloc[start_data:end_data])
            start_data += 5
            end_data += 5
        else:
            break
    #display the time start function
    print("this time is {} seconds.".format(f"{time.time()-start:.4f}"))

def main():
    while True:
        city, month, day = get_city()
        print("_"*60)
        print("        chosise City > {} , Month > {} , Day > {} .".format(city, month, day))
        
        data = Data(city, month, day)
        Time(data)
        print("_"*60)
        station(data)
        print("_"*60)
        trip(data)
        print("_"*60)
        user(data)
        print("_"*60)
        individual_data(data)
        print("_"*60)
        restart = input("Would you like to restart? Yes or No.").lower()
        if restart != 'yes':
            break
main()



