**Description of the Phone class:**
The phone class models phones that can call each other. Each phone object can call
every other phone through a class attribute
	
**Class and data variables:**
      __network: a private class attribute that allows phones to communicate with eachother. __network is a dictionary with keys “phones” and “calls”. “Phones” has a dictionary of phones with their numbers as keys and phone objects as values. “Calls” has a dictionary of calls with a tuple: (phone number initiating call, phone number receiving call) as keys and a dictionary holding “status” and “current speech” as it keys.
      __name: a private data attribute that holds the phones name
      __contacts: a private data attribute that holds a phone’s contact list in a dictionary. This dictionary has phone numbers as keys and a dictionary holding contact info as values. Currently, it only holds the name of each contact. __contacts is not checked for accuracy, you can add contacts for phones that don’t exist.
      __number: a private data attribute that holds a phone’s phone number

**Methods:**
      call: a public method that calls another phone object with a given phone number, it does this by adding a call to the __network class attribute with a status of “ringing” and no current speech
      hang up: a public method that hangs up calls that a phone is in, it has a boolean argument. If it’s true then the method will hang up all active calls, if it isn’t then it will also hang up inactive calls
      get_contacts: a public getter method for contacts, returns the phone objects contact dictionary
      add_contact: a public method that adds a new contact to the phones contact list using its arguments: number and name
      del_contacts: a public method that deletes all of a phone’s contacts
      get_number: a public getter method that returns a phone’s phone number
      get_contact_str: a public method that returns a phones contact list as a formatted string. It returns the name and number of each contact on a separate line
      set_number: a public setter method that sets a phones phone number
      get_name: a public getter method that returns a phones name
      set_name: a public setter method that sets a phones name
      __search_network: a private method that searches through __network for calls that is is a part of. If a call’s status is ringing then it will request the user to answer it and if it is active then it will ask the user to talk or hang up. It also handles hanging up and ignoring calls on both ends. It does this using the __send_speech, and __call_requested methods
      __call_requested: a private method that handles answering, hanging up, or ignoring calls
      __send_speech: a p[rivate method that formats and sends text to other phones through calls in __network
      __str__: a magic method that handles string casting. It returns the name, number, and number of contacts of a phone object
      Update: a public method that handles simulating a phone. It allows the user to input commands for a phone to make calls, hang up, talk, add contacts, help with a list of possible commands, end the current update, or exit from the program

**Description of demo program:**
	The demo program allows the user to first set up a simulation of phone objects and then run it. The user can enter a variety of commands to create, edit, and view phones and then can run the simulation to control those phones while they are being simulated.


**Instructions to run the demo program:**
	**Instructions for the setup:**
The setup is where you create and edit phones to simulate. If you just use the ‘auto’ and then ‘start’ commands then it will run the simulation with a default setup
	**Commands for setting up a simulation:**
    --auto: automatically sets up two phones and their contact lists, after this you can use the ‘start’ command to start the simulation. The two phones are phone1 and phone2 and they have each other’s contact info. Phone1’s number is 123-456-7890 and phone2’s number is 098-765-4321.
    --create phone: creates a new phone and asks for the user to input a name and a number
    --show phones: prints the names of all phones
    --edit phone: allows the user to edit an existing phone by entering its name. After entering a phones name, the user can enter multiple commands to edit that phone
    --help: returns a list of valid commands
    --back: leaves the editing menu
    --add contact: adds a new contact to the phone and asks for a name and number
    --change number: lets the user change the phone’s phone number
    --change name: lets the user change the phone’s name
    --show contacts: prints the phones contact list
    --delete contacts: delete all of a phone’s contacts
    --start: stops the setup section and starts the simulation
    --exit: stops the program
    --start: stops the setup section and starts the simulation
    --exit: stops the program
	**Instructions for the simulation:**
In the simulation after setting up, it will flip back and forth between which phone you are controlling. To do a basic call, you can use the ‘call’ command and then type in ‘phone2’ when the simulation starts. It will then switch to the next phone which will be phone2 if you are using the default setting. You can choose to answer or deny the call. If you answer then you can type what you say or hang up. It will switch back and forth between which phone is talking until you hang up.
	**Commands for operating the simulation:**
    --call: calls another phone
    --add contact: allows the user to add a contact to the current phone by entering a name and number
    --Show phone: prints info about the current phone
    --exit: ends the program
    --help: prints a list of valid commands


