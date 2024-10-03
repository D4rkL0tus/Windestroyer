import threading
import os
import sys
import time

# Where the main structure of the program executes
def main():
    MainMenu = """
                    --Windows 10 Debloater--
                          Version 1.0
             [1] Remove All Bloat  [2] Interactive Process
             [3] Select Which Bloat to Remove
             [4] Exit

             
    """
    ClearScreen()
    MainMenu = str(MainMenu)
    print(MainMenu)
    MainMenuInput = input("[Enter an Option]: ")

    # Match statement used for user input selection.
    match str((MainMenuInput)):
        case "1":
            try:
                print("PLACEHOLDER")
                ClearScreen()
            except:
                print("There was an issue with performing an action,")
                print("Redirecting back to the main menu")
                time.sleep(0.5)
                ClearScreen()
                main()
        case "2":
            try:
                print("PLACEHOLDER")
                time.sleep(0.5)
                ClearScreen()
            except:
                print("There was an issue performing an action")
                print("Redirecting back to the main menu")
                time.sleep(0.5)
                ClearScreen()
                main()
        case "3":
            try:
                print("PlCAEHOLDER!")
            except:
                print("There was an issue performing an action")
                print("Redirecting back to the main menu")
                time.sleep(0.5)
                ClearScreen()
                main()
        case "4":
            try:
                ExitInput = input("Are you sure you would like to exit? [Y/N]: ")
                
                if  ExitInput.capitalize() == "Y":
                    print("Exiting...")
                    time.sleep(2)
                    ClearScreen()
                    exit()
                elif ExitInput.capitalize() == "N":
                    print("Returning back to the main menu")
                    time.sleep(0.5)
                    ClearScreen()
                    main()
                else:
                    print("")
                    print("")
                    print("You have typed an incorrect character --> " + ExitInput)
                    print("Returning to the main menu!")
                    time.sleep(2)
                    ClearScreen()
                    main()
            except:
                print("There was an issue with your performed action")
                print("Returning to the main menu")
                time.sleep(0.5)
                ClearScreen()
        case _:
            try:
                ClearScreen()
                main()
            except:
                print("There was an issue\nExiting...")
                time.sleep(0.5)
                return 1
"""
    A function used to
    clear the screen by executing a system call
    dependent on which operating system is running.
"""
def ClearScreen():
    OperatingSystems = ["Win32", "Linux"]
    OSPlatform = sys.platform
    if OSPlatform == OperatingSystems[0].lower():
        try:
            os.system('cls')
        except:
            print("There was an issue executing a system call.")
            return 1
    elif OSPlatform == OperatingSystems[1].lower():
        try:
            os.system('clear')
        except:
            print("There was an issue exeucting a system call")
            return 1       
    else:
        return 1
    

if __name__ == '__main__':
    try:
        main()
    except:
        exit()