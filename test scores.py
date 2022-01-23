#Program takes user input of student test scores & stores them in a local text file as a mock school database.
#Why are you peeking at my code though?

print("Welcome, please enter appropriate student information & test result for saving to the school database.")
#Function allows for code to be reran without restarting program from scratch
def main():
    x, q, y, z = input("Enter student name, subject, class & grade each seperated by a comma: ").split(",")

    #Removes any unnecessary spaces in users input
    name = x.strip()
    subject = q.strip()
    classname = y.strip()
    grade = z.strip()

    #Returns the now stripped user input for confirmation prior to the saving process
    print("\n" + "[Information Entered]")
    print("Student Name: " + name)
    print("Subject: " + subject)
    print("Class: " + classname)
    print("Grade: " + grade + "\n")

    def saving():
        #Asks user to confirm selection before saving data
        save = input("Do you wish to save this data to the database? [Y/N]: ")
        if save == "Y" or save == "y":
            filename = input("Please enter a filename: ")
            #Opens/creates file & writes data within it.
            f = open(filename + ".txt", "a")
            f.write("Name: " + name + "\n")
            f.write("Subject: " + subject + "\n")
            f.write("Class: " + classname + "\n")
            f.write("Grade: " + grade + "\n\n")
            f.close()
            print("Data has been saved to a text file named " + filename + ".txt")
            restart = input("Would you like to repeat process? [Y/N]: ")
            if restart == "Y" or restart == "y":
                print("")
                main()
            else:
                input("\n" + "Understood, press Enter to terminate program.")

        #Process following a decision to not save data.
        elif save == "N" or save == "n":
            print("OK, prior entry deleted.")
            restart = input("Would you like to try again? [Y/N]: ")
            if restart == "Y" or restart == "y":
                print("")
                main()
            else:
                print("\n" + "Understood, terminating program")
                exit()
        else:
            print("User Inputting Error: Please only use Y/N: ")
            saving()
            
    saving()
main()
#Main must be triggered here or program will not start
