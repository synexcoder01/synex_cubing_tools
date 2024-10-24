import os
import random
import datetime
import sys
os.system('cls')

if getattr(sys, 'frozen', False):
    script_dir = os.path.dirname(sys.executable)
else:
    script_dir = os.path.dirname(os.path.abspath(__file__))

def new_session():
    all_scrambles = []
    os.system('cls')
    print("You chose to start a new session.\n")
    print("Please provide the name of the session you want to create.\n")
    session_name = input()

    session_path = os.path.join(script_dir, "your_sessions", f"{session_name}.csv")
    
    if os.path.exists(session_path):
        os.system('cls')
        print("This session is already existing. Please continue an existing session. Returning to the main menu...\n")
        return
    os.system('cls')
    print("You chose to create a new session with the name: " + session_name + "\n")
    
    scrambles_path = os.path.join(script_dir, "dev_files", "scrambles.txt")
    with open(scrambles_path, "r", encoding="utf-8") as file:
        for line in file:
            all_scrambles.append(line.strip())

    while True:
        current_scramble = all_scrambles[random.randint(0, len(all_scrambles)-1)]
        current_solve = 1
        print("The scramble for the ",current_solve,". solve is: ",current_scramble,'\n',sep='')
        print("If you are done, please provide the time for this solve.\nPlease provide the time in seconds.\nMake sure you use '.' as a decimal point, not ','.\nMake sure you did not write letters or other symbols in the time.\n\nIf you want to leave, type 'exit'\n")
        time = input()
        if time == "exit":
            os.system('cls')
            break
        else:
            while True:
                try:
                    time = float(time)
                    break
                except ValueError:
                    os.system('cls')
                    print("You did not provide a valid time. Please provide the time in seconds, using '.' as the decimal point.\n")
                    time = input()
            dateandtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            os.system('cls')
            print("Do you want to save this solve? (write anything, to save, write 'no', to not save)\n")
            save = input()
            if save == "no":
                os.system('cls')
                print("You chose not to save this solve.\n")
            else:
                os.system('cls')
                print("You chose to save this solve.\n")
                if not os.path.exists(session_path):
                    with open(session_path, "w", encoding="utf-8") as session_file:
                        session_file.write('No.;Time;Comment;Scramble;Date;P.1\n')
                        session_file.write(f'{current_solve};{time:.2f};;{current_scramble.strip()};{dateandtime};{time:.2f}\n')
                else:
                    with open(session_path, "r", encoding="utf-8") as session_file:
                        lines = session_file.readlines()
                        current_solve = int(lines[-1].split(";")[0].strip()) + 1
                    with open(session_path, "a", encoding="utf-8") as session_file:
                        session_file.write(f'{current_solve};{time:.2f};;{current_scramble.strip()};{dateandtime};{time:.2f}\n')

    return

def continue_session():
    os.system('cls')
    print("You chose to continue an existing session.\n")
    print("Please provide the name of the session you want to continue.\n")
    
    available_sessions = [f for f in os.listdir(os.path.join(script_dir, "your_sessions")) if f.endswith('.csv')]
    
    if not available_sessions:
        os.system('cls')
        print("No existing sessions found. Please start a new session. Returning to the main menu...\n")
        return
    else:
        print("Available sessions:")
        for session in available_sessions:
            print(session.replace('.csv', ''))
        
    print("\n")
    session_name = input()
    
    os.system('cls')
    
    session_path = os.path.join(script_dir, "your_sessions", f"{session_name}.csv")

    all_scrambles = []
    scrambles_path = os.path.join(script_dir, "dev_files", "scrambles.txt")
    with open(scrambles_path, "r", encoding="utf-8") as file:
        for line in file:
            all_scrambles.append(line.strip())

    while True:
        current_scramble = all_scrambles[random.randint(0, len(all_scrambles)-1)]
        with open(session_path, "r", encoding="utf-8") as session_file:
            lines = session_file.readlines()
            current_solve = int(lines[-1].split(";")[0].strip()) + 1
        print("The scramble for the ",current_solve,". solve is: ",current_scramble,'\n',sep='')
        print("If you are done, please provide the time for this solve.\nPlease provide the time in seconds.\nMake sure you use '.' as a decimal point, not ','.\nMake sure you did not write letters or other symbols in the time.\n\nIf you want to leave, type 'exit'\n")
        time = input()
        if time == "exit":
            os.system('cls')
            break
        else:
            while True:
                try:
                    time = float(time)
                    break
                except ValueError:
                    os.system('cls')
                    print("You did not provide a valid time. Please provide the time in seconds, using '.' as the decimal point.\n")
                    time = input()
            dateandtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            os.system('cls')
            print("Do you want to save this solve? (write anything, to save, write 'no', to not save)\n")
            save = input()
            if save == "no":
                os.system('cls')
                print("You chose not to save this solve.\n")
            else:
                os.system('cls')
                print("You chose to save this solve.\n")
                if not os.path.exists(session_path):
                    with open(session_path, "w", encoding="utf-8") as session_file:
                        session_file.write('No.;Time;Comment;Scramble;Date;P.1\n')
                        session_file.write(f'{current_solve};{time:.2f};;{current_scramble.strip()};{dateandtime};{time:.2f}\n')
                else:
                    with open(session_path, "r", encoding="utf-8") as session_file:
                        lines = session_file.readlines()
                        current_solve = int(lines[-1].split(";")[0].strip()) + 1
                    with open(session_path, "a", encoding="utf-8") as session_file:
                        session_file.write(f'{current_solve};{time:.2f};;{current_scramble.strip()};{dateandtime};{time:.2f}\n')

def manage_sessions():
    os.system('cls')
    print("You chose to manage your sessions.\n")
    print("Please provide the name of the session you want to manage.\n")

    available_sessions = [f for f in os.listdir(os.path.join(script_dir, "your_sessions")) if f.endswith('.csv')]
    
    if not available_sessions:
        os.system('cls')
        print("No existing sessions found. Please start a new session. Returning to the main menu...\n")
        return
    else:
        print("Available sessions:")
        for session in available_sessions:
            print(session.replace('.csv', ''))
        
    print("\n")
    session_name = input()
    if not os.path.exists(os.path.join(script_dir, "your_sessions", f"{session_name}.csv")):
        os.system('cls')
        print("This session is not existing. Returning to the main menu...\n")
        return
    else:
        os.system('cls')
        print("You chose to manage the session: ", session_name, "\n")
        print("What do you want to do? (delete - d, rename - r, exit - anything else)\n")
        manage_session_question = input()
        
        if manage_session_question == "d":
            os.system('cls')
            print("Are you sure you want to delete the session? (yes/no)\n")
            sure = input()
            if sure == "yes":
                os.system('cls')
                print("You chose to delete the session: ", session_name, "\n")
                os.remove(os.path.join(script_dir, "your_sessions", f"{session_name}.csv"))
                print("The session was successfully deleted.\n")
                return
            else:
                os.system('cls')
                print("You did not choose to delete the session. Returning to the main menu...\n")
                return
        elif manage_session_question == "r":
            os.system('cls')
            print("You chose to rename the session: ", session_name, "\n")
            print("Please provide the new name for the session.\n")
            new_session_name = input()
            os.rename(os.path.join(script_dir, "your_sessions", f"{session_name}.csv"), 
                      os.path.join(script_dir, "your_sessions", f"{new_session_name}.csv"))
            os.system('cls')
            print("The session was successfully renamed.\n")
            return
        else:
            os.system('cls')
            print("You did not choose a valid option. Returning to the main menu...\n")
            return
        

#main menu def

def main_menu():
    print("What do you want to do? (Choose a number)\n\n1: Start a new, or continue an existing session.\n2: View your statistics.\n3: Import an external (csv) session into one of your existing sessions.\n4: Manage your sessions.\n")
    main_menu_question = input()

    if main_menu_question == "1":
        os.system('cls')
        print("If you want to start a new session, just type 'new'.\nIf you want to continue an existing session, type 'cont'.\n")
        new_or_continue = input()
        if new_or_continue == "new":
            new_session()
        elif new_or_continue == "cont":
            continue_session()
        else:
            os.system('cls')
            print("You did not choose a valid option. Returning to main menu...\n")
            return

    elif main_menu_question == "2":
        os.system('cls')
        print("You chose to view your statistics.\n")
        print("Please provide the name of the session you want to view the statistics of.")
        os.system('cls')
        print("work in progress")
        return
        session_name = input()
        #we run the view statistics def

    elif main_menu_question == "3":
        os.system('cls')
        print("work in progress")
        return
        print("You chose to import an external (csv) session into one of your existing sessions.")
        print("READ CAREFULLY!\nPlease have the file you want to import, in the 'import_session' folder.\nMake sure it is named 'import.csv'\nConfirm, that it is formatted in the correct way.\nMake sure, you only have one file in the 'import_session' folder.\nOnly import csv files, that were exported from cstimer.net. We will support more types of files, in future updates.\nWhen you import it into a session, aknowledge, that you don't overwrite any of your previous solves, and the new, imported solves, will be added to the end of your session. In the future, we will add a feature, that will import the times, to the exact date, you did that solve.\nPlease aknowledge, that if you mess up one of the steps, your session can be permanently corrupted. The developers are not responsible for any data loss!\nType anything that is not 'yes', and you will be directed back to the main menu, exit the program, and do these steps. When you are done, come back here. If you want to proceed, then type 'yes'.")
        import_confirmation = input()
        if import_confirmation == "yes":
            os.system('cls')
            print("You chose to proceed.\n")
            print("Please provide the name of the session you want to import the session into.")
            internal_session_name = input()
            #we run the import session def
        else:
            os.system('cls')
            print("You did not choose to proceed. Returning to main menu...\n")
            return
    
    elif main_menu_question == "4":
        manage_sessions()

#main program
while True:
    main_menu()
