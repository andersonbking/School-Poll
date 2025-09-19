responses = {}
#set a flag to indicate that the polling is active
polling_active = True
while polling_active:
    #prompt for name and response
    name = input ("What is your name? ")
    response = input ("What school do you plan on attending? ")
    #store responses in a dictionary
    responses [name] = response
    #find out who else will take the pole
    repeat = input("Would you like to let another person respond? ")
    if repeat == 'no':
        polling_active = False

#Polling is complete. Show the results.
print("---Poll Results---")
for name, reponse in responses.items():
    print(f"{name} will go to {reponse}.")


