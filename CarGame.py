command = ""
while command != "quit":
    command = input("> ").lower()
    if command == "start":
        print("Car started...")
    elif command == "stop":
        print("Car Stopped")
    elif command == "help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to quit 
        """)
    else:
        print("Sorry, I don't understand that")