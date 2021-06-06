def main():
    while True:
     user_input = input("Please type in an acronym of a weekday: ")

     user_input = user_input.lower()

     if (user_input == "mon"):
         print("Monday")
     elif (user_input == "tue"):
         print("Tuesday")
     elif (user_input == "wed"):
         print("Wednesday")
     elif (user_input == "thur"):
         print("Thursday")
     elif (user_input == "fri"):
         print("Friday")
     elif(user_input == "lol"):
         print("Laugh Out Loud")
     else:
         print("Incorrect acronym")

     user_input = input("Do you want to search again? If not, type 'no'. ")
     user_input = user_input.lower()
     if user_input == "no":
        break


if __name__ == "__main__":
    main()


