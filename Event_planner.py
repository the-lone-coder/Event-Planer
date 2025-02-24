# Importing the necesary libs
import pickle
import os

# Asks if this is the first time using the program
print('Is this your first time using this program? [Y/N]')
first_time_user = input()

# Runs the case where the valuable is equal to Y or y 
if first_time_user == 'Y':
    print('Please input your name:') ; user_name = input()
    print('Hello ' + user_name)

    # Saves provided data in a .pkl file
    user_data_save = [user_name]
    user_data_save_file = 'user_data.pkl'
    with open(user_data_save_file, 'wb') as data_file:
        pickle.dump(user_data_save, data_file)

elif first_time_user == 'N':     
     # Checks if user data file exists
    if os.path.exists('user_data.pkl'):
        print('Loading file...')

        # Opens the file using the pickle.load funtion from the pickle library
        with open('user_data.pkl', 'rb') as file:
            loaded_user_data = pickle.load(file)

            # Loads and displays the user data
            print('Hello ' + loaded_user_data[0])

    else:
        print('The user_data file does not exist, please create one with by inputing Y during the startup questionaire')
        exit(1)
else:
    print('The argument you gave does not exist')
    exit(1)

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
    
    #Asks the user if they want to add any notes
    print('Do you wish to add any notes? [Press Y/N]')
    add_notes=input()

        # Checks the case where the user wants to add notes
    if add_notes == 'Y':
        print('Please input your note:')
        event_note = input()

    # Saves the details in case the user addsa an event note
        print('Saving the details...')
        print('Please name the save file (Name must end in .pkl)')
        save_file_name = input()
        event_details=[event_name, event_date, person_count, event_note]
        with open(save_file_name , 'wb') as file:
            pickle.dump(event_details, file)



        #Checks the case where the user does not want to add any notes
    if add_notes == 'N':
        print('No notes will be added, continuing with the creation process')


    # Saves the details if the user doesn't add any note

    print('Saving the details...')
    print('Please name the save file (Name must end in .pkl)')
    save_file_name = input()
    event_details=[event_name, event_date, person_count]
    with open(save_file_name , 'wb') as file:
        pickle.dump(event_details, file)

    # Checks the case if the user loads an event

if plan_or_load == "L":

    # Asks user for the save file name
    print('Input the filename ending in .pkl') ; inputed_save_file = input()
    # Checks if the file name specified coresponds to any files other than events

    if inputed_save_file == 'user_data.pkl':
        print('You are trying to load a file that coresponds to the user data.')
        exit(1)

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
            print('Notes: ' + loaded_data[3])  
     
    # Returns an error in case of the file not existing
    else:
        print('The given file does not exist')
        exit(1)    
