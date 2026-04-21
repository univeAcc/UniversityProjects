friends = []
run=True
while run:
    choice = input("\nwana add new friends? y/n: ")
    if choice == "y":
        friend = input("enter your friend name: ")
        friends.append(friend)
        print("\nfriends list: ")
        for friend in friends:
            print(friend)
    else:
        run= False
        break
