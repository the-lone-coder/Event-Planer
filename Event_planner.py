# Importing the necesary libs
import pickle
import os
# Greeting the user
print('Please input your name:') ; user_name=input()
print('Hello ' + user_name)

# Asking the user what they want to do, plan an event, or load from memory
print('What would you like to do?')
print('Plan a new event [Press N]')
print('Load a existing event [Press L]')
plan_or_load=input()

# Checks the value of the user input 
    # Checks the case if the user wants to create a new event

if plan_or_load == "N":
    print('How would you like to name the event?')
    event_name = input()
    print('What date would you like the event to take place on?')
    event_date = input()
    print('How many persons will you invite?')
    person_count = input()
    person_count = int(person_count)

    # Saves the details
    print('Saving the details...')
    print('Please name the save file (Name must end in .pkl)')
    save_file_name = input()
    event_details=[event_name, event_date, person_count ]
    with open(save_file_name , 'wb') as file:
        pickle.dump(event_details, file)

    # Checks the case if the user loads an event

if plan_or_load == "L":

    # Asks user for the save file name
    print('Input the filename ending in .pkl') ; inputed_save_file = input()
    
    # Checks if the file exists
    if os.path.exists(inputed_save_file):
        print('Loading file...')

        # Opens the file using the pickle.load funtion from the pickle library
        with open(inputed_save_file, 'rb') as file:
            loaded_data = pickle.load(file)

            # Prints out the details
            print('Your event details are') 
            print('Event name: ' + loaded_data[0]) 
            print('Event date: ' + loaded_data[1]) 
            print('Number of people invited: ' + str(loaded_data[2]))  
    
    # Returns an error in case of the file not existing
    else:
        print('The given file does not exist')
        exit(1)    
