dictionary={}


while True:

    print("What would you like to do?")

    print("Add Participant")
    print("See Participant")
    print("Exit")

    assign=("Add Participant")
    view=("See Participant")
    done=("Exit")

    inp=input("Please choose:")

    if inp == assign:
        name=input("Enter name:")
        print("Select Event:")
        print(f'1.CS , 2.GoogleIt , 3.Treasure Hunt')
        decision=input()
        dictionary[name]=decision

    elif inp == view:
        print (dictionary)

    elif inp != assign and inp != view:
        print('Please Try Again ')  
        if inp==done:
            break

    




