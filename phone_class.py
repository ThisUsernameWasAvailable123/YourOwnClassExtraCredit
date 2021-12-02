"""
Assignment 10.1: Your Own Class
Aidan Sterling
purpose: practice making classes by making a class that simulates a real world object
"""

#Phone class: phone objects can call eachother using a class attribute called network
class Phone:
    #create a class attribute called network to allow phones to communicate with eachother
    __network = {"phones":{}, "calls":{}}
    #create a new phone
    def __init__(self, name, number):
        #set the phone's user's name
        self.__name = name
        #add the phone to the network
        self.__network["phones"][number] = self
        #make a new phone start with a blank contact list
        self.__contacts = {}
        #set the phones number
        self.__number = number

    #a method that allows one phone to call another through the network
    def call(self, number):
        #if the user intered a name from the contact list, use that contacts number
        for i in self._Phone__contacts.keys():
            if self._Phone__contacts[i]["name"] == number:
                number = i
                break
        #try finding the numbers name in the phones contact list
        #if found, say calling {cantact's name}
        try:
            print(f"calling {self._Phone__contacts[number]['name']}")
        #if its not found, say calling {phone number}
        except KeyError:
            print(f"calling {number}")
        #try to find a phone that has the number in the network and start a call with it
        try:
            self._Phone__network["phones"][number]
            self._Phone__network["calls"][(self._Phone__number, number)] = {"status":"ringing", "current speach":""}
            #return true because a call was made
            return True
        #if no phone matches the number give an error message
        except KeyError:
            print("no phone found with given number")
        #return false if no call was made
        return False
    
    #a function that ends a call by hanging up
    def hang_up(self, needs_to_be_active = False):
        #loop through phone calls
        for numbers in self._Phone__network["calls"].keys():
            #find the other number in each call
            other_number = "ERROR"
            #loop through phones in call
            for i in numbers:
                #if it finds one that isnt it then it sets other number to i
                if i != self._Phone__number:
                    other_number = i
            
            #if the call thats being ended doesent need to be active and the phone is in the call
            if not needs_to_be_active and self._Phone__number in numbers:
                #end the call
                self._Phone__network["calls"][numbers]["status"] = "ended"
                print("the call has ended")
                #stop looping through calls
                break
            #if the call thats being ended needs to be active and the phone is in the call
            if needs_to_be_active and self._Phone__number in numbers and self._Phone__network["calls"][numbers]["status"] == "active":
                #end the call
                self._Phone__network["calls"][numbers]["status"] = "ended"
                print("the call has ended")
                #stop looping through calls
                break

    #getter method for the phones contact list
    def get_contacts(self):
        return self._Phone__contacts
    #method that adds a new contact to the phones contact list
    def add_contact(self, number, name):
        self._Phone__contacts[number] = {"name":name}
    #deletes all contacts
    def del_contacts(self):
        self._Phone__contacts = {}
    #getter for the phone's phone number
    def get_number(self):
        return self._Phone__number
    #getter for a phones contact list that returns it as a string
    def get_contact_str(self):
        output = ""
        start = True
        for contact in self._Phone__contacts.keys():
            if start:
                output += f"\t\tname: {self._Phone__contacts[contact]['name']}, number: {contact}"
                start = False
            else:
                output += f"\n\t\tname: {self._Phone__contacts[contact]['name']}, number: {contact}"
        return output

    #setter for the phone's phone number
    def set_number(self, number):
        self._Phone__number = number
    #getter for the phone's user's name
    def get_name(self):
        return self._Phone__name
    #setter for the phone's user's name
    def set_name(self, name):
        self._Phone__name = name
    
    #connect phone to network, returns weather the user should be able to keep on enering commands with a bool
    def __search_network(self):
        #loop through calls
        for numbers in self._Phone__network["calls"].keys():
            #if the phone is in a call that has ended
            if self._Phone__number in numbers and self._Phone__network["calls"][numbers]["status"] == "ended":
                print("the call has ended")
                #delete that call
                del self._Phone__network["calls"][numbers]
                break
        #loop through calls
        for numbers in self._Phone__network["calls"].keys():
            #if the phone is in a call that has been denied
            if self._Phone__number in numbers and self._Phone__network["calls"][numbers]["status"] == "denied":
                print("the call was denied")
                #delete that call
                del self._Phone__network["calls"][numbers]
                break
        #loop through calls
        for numbers in self._Phone__network["calls"].keys():
            #if the phone is in a call that has been ignored
            if self._Phone__number in numbers and self._Phone__network["calls"][numbers]["status"] == "ignored":
                print("the recipiant missed your call, please try again later")
                #delete that call
                del self._Phone__network["calls"][numbers]
                break
        #loop through calls
        for numbers in self._Phone__network["calls"].keys():
            #if the phone is in a call that is waiting to be answered by it
            if self._Phone__number == numbers[1] and self._Phone__network["calls"][numbers]["status"] == "ringing":
                #request the user to answer the call
                self._Phone__call_requested(numbers)
                #if the user answered it
                if self._Phone__network["calls"][numbers]["status"] == "active":
                    #return false meaning they dont get to enter any more commands
                    return False
                if self._Phone__network["calls"][numbers]["status"] == "denied":
                    #say the call has ended
                    print("the call has ended")
                break
        #loop through calls
        for numbers in self._Phone__network["calls"].keys():
            #if the phone is in an active call
            if self._Phone__number in numbers and self._Phone__network["calls"][numbers]["status"] == "active":
                #print what was last said
                print(self._Phone__network["calls"][numbers]["current speech"])
                #get the other phone number in the call
                other_number = "ERROR"
                #loop through the numbers in the call
                for i in numbers:
                    #if it finds one that isnt it then it sets other number to i
                    if i != self._Phone__number:
                        other_number = i
                #try finding the other callers name to tell the user who is talking
                try: 
                    other_name = self._Phone__contacts[other_number]["name"]
                #if it cant find the name, use 'unknown caller' as the name
                except KeyError:
                    other_name = "unknown caller"
                #ask user the say something or hang up
                user_input = input("input what you say or type 'hang up': ")
                #if they typed 'hang up', hang up
                if user_input == "hang up":
                    self.hang_up()
                #otherwise, send the text to the call
                else:
                    self._Phone__send_speech(numbers, user_input)
                return False
        return True
    
    #a method that handles answering, denieing, and ignoring incoming calls
    def __call_requested(self, numbers, attempt_number = 2):
        #try to tell the user the name of the caller from contacts
        try:
            print(f"incoming call from {self._Phone__contacts[numbers[0]]['name']}")
        #if it cant find the name, use 'unknown caller' as the name
        except KeyError:
            print("incoming call from unknown caller")
        #ask the user to answer or deny the call
        user_input = input("enter answer or deny: ")
        #if the user answers
        if user_input == "answer":
            #hang up active calls the phone is in
            self.hang_up(True)
            #activate the call
            self._Phone__network["calls"][numbers]["status"] = "active"
            print("call started")
            #and ask the user to say somthing or hang up
            user_input = input("input what you say or type 'hang up': ")
            #if the user hangs up, hang up
            if user_input == "hang up":
                self.hang_up()
            #otherwise, send the users speech
            else:
                self._Phone__send_speech(numbers, user_input)
        #if the user denys the call
        elif user_input == "deny":
            #set the call's status to denied
            self._Phone__network["calls"][numbers]["status"] = "denied"
        #if something else was entered
        else:
            #try again if there have been less than the input attempt number of tries
            if attempt_number > 0:
                self._Phone__call_requested(numbers, attempt_number - 1)
            #if the number of tries excedes the limit, set the calls status to ignored
            else:
                self._Phone__network["calls"][numbers]["status"] = "ignored"
                print(f"you missed a phone call")
    #send the input speech to a call
    def __send_speech(self, numbers, speech):
        self._Phone__network["calls"][numbers]["current speech"] = f"{self._Phone__name} says: {speech}"

    def __str__(self):
        return f"name: {self._Phone__name}, number: {self._Phone__number}, contacts: {len(self._Phone__contacts)}"

    #simulate a phone
    def update(self):
        #show whitch phone is being updated
        print(f"----{self._Phone__name}----")
        #search network for calls that need handleing and if the user can still enter commands afterwards
        if self._Phone__search_network():
            user_input = ""
            #let the user enter commands
            while user_input != "continue":
                user_input = input(">>> ")
                #if the user enters the call command
                if user_input == "call":
                    #call the call method and have the user input the number or contacts name
                    if self.call(input("input a phone number or a contacts name to call: ")):
                        #stop the user from entering more commands if the call was successfull
                        break
                #if the user enters the add contact command
                elif user_input == "add contact":
                    #call the add_contact method and have the user input a number and a name for the contact
                    self.add_contact(input("input a phone number: "), input("input a name: "))
                #if the user enters the show phone command
                elif user_input == "show phone":
                    #use the str magic method to print the phone
                    print(self)
                elif user_input == "exit":
                    #print ending program message
                    print("ending program...")
                    #end program
                    return True
                #if the user enters the help command
                elif user_input == "help":
                    #print the possible commands
                    print("the valid commands are: 'call', 'add contact', 'show phone', 'continue', 'exit', and 'help'")
            return False

#define the main function
def main():
    #this demo program allows the user to set up phones in a network and then simulate those phone
    #if the simulate loop should run
    simulate = True
    #create black list that will hold Phone objects
    phones = []
    #print intructional message
    print("enter commands to setup a network of phones, enter 'help' for a list of valid commands")
    #setup command loop
    while True:
        #print the symbol that shows the user that they can enter a command
        user_input = input(">>> ")
        #help command
        if user_input == "help":
            #print valid commands
            print("'auto', 'create phone', 'show phones', 'edit phone', 'start', exit', 'help'")
        #auto command
        if user_input == "auto":
            #reset list of phones
            phones = []
            #create two phones
            phones.append(Phone("phone1", "123-456-7890"))
            phones.append(Phone("phone2", "098-765-4321"))
            #add contacts to those phones
            phones[0].add_contact("098-765-4321", "phone2")
            phones[1].add_contact("123-456-7890", "phone1")
            #show phones afterwords
            user_input = "show phones"
        #create phone command
        if user_input == "create phone":
            #add a new phone object to the list using user input
            phones.append(Phone(input("    enter a name: "), input("    enter a phone number: ")))
        #show phones command
        if user_input == "show phones":
            #loop through phones in phone list and print their names
            for phone in phones:
                print(f"    {phone.get_name()}")
        #edit phone command
        if user_input == "edit phone":
            #ask the user to enter a phones name
            phone_name = input("    enter the name of the phone you want to edit: ")
            flag = False
            #check if that phone is in the list
            for phone in phones:
                if phone.get_name() == phone_name:
                    flag = True
                    found_phone = phone
            #if it is, allow the user to edit it
            if flag:
                #print the phone thats being edited
                print(f"    {found_phone}")
                #the command loop for editing a phone
                while True:
                    #print the symbol that shows the user that they can enter a command
                    command = input("    >>> ")
                    #help command while edeting a phone
                    if command == "help":
                        #print list of valid commands
                        print("\t'add contact', 'change number', 'change name'\n\t'show contacts', 'delete contacts', 'start', 'back', 'exit', 'help'")
                    #add contact command
                    if command == "add contact":
                        #add contact to phone using user input
                        found_phone.add_contact(input("\tenter a phone number: "), input("    enter a name: "))
                    #change number command
                    if command == "change number":
                        #change the phones number using user input
                        found_phone.set_number(input("\tenter a new number"))
                    #change name command
                    if command == "change name":
                        #change the phones name using user input
                        found_phone.set_name(input("\tenter a new name"))
                    #show contacts command
                    if command == "show contacts":
                        #show contacts using the get_contact_str method
                        print(found_phone.get_contact_str())
                    #delet contacts command
                    if command == "delete contacts":
                        #deletes all contacts using the del_contacts method
                        found_phone.del_contacts()
                        print("\tcontacts deleted")
                    #start method
                    if command == "start":
                        #leave edit phone loop and start simulation
                        user_input = "start"
                        break
                    if command == "exit":
                        #leave edit phone loop and start simulation
                        user_input = "exit"
                        break
                    #back method
                    if command == "back":
                        #break out of editing loop
                        break
            else:
                #if no phone with give name print error message
                print(f"no phone found with the name: '{phone_name}'")
        #start command
        if user_input == "start":
            #print starting simulation message
            print("starting simulation...")
            #leave setup loop and start simulation
            break
        if user_input == "exit":
            #print starting simulation message
            print("ending program")
            #dont start sumulation loop
            simulate = False
            #leave setup loop
            break
    #simulate the phones
    while simulate:
        #loop through all phones
        for phone in phones:
            #update all phones
            if phone.update():
                #if the update method returns True, end program
                simulate = False
                #break out of loop
                break

#call the main function
if __name__ == "__main__":
    main()
