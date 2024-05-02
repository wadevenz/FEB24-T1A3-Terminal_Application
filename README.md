# T1A3 Terminal Application

## Terminal Bank

### Wade Venz
A simple application where users interacting with the terminal will be able to engage in a virtual pseudo-bank, creating an account, withrawing and depositing arbitrary imaginary money running a total balance. 


[**GitHub**](https://github.com/wadevenz/FEB24-T1A3-Terminal_Application)


### Features
The basic functionality of this application revolves around the creation of a central csv file that initialises with three headers; name, pin and balance. User inputs will populate these fields as list and will be called upon for features listed below. 

#### Create Account
In the initial menu, it will enable the user to create an account. The user will input a name and a unique 4 digit PIN which will be stored in a csv file. A bonus of "$100" is also added to balance with a print message to indicate this has been done. 

##### How it works
An initial intermediate handle function is called which utilises two seperate functions to independently return user input for 'name' and 'PIN' respectively. The PIN input is run through conditional statements to assure it contains only digits and is only 4 characters long. If the conditions return 'True' then 'create_account' function is called. An error message is printed if conditions are not met and returns to initial menu. The 'create_account' function contains one other function called the 'get_account' function which opens the file and reads as a Dictionary. It is designed to return the 'row' where user 'pin' input matches the corresponding title, if not to return 'None'. In 'create_account', a 'None' will print a message requiring a unique PIN, however if 'row' is returned from 'get_account', the file is opened in write mode and the row is written to next line. The 'initial_balance' set to 100 is also written in balance and a print message is then displayed to user. 

#### Access Account
The same initial menu also allows users to access accounts already created with the use of PIN the user has self determined. This option will open a secondary menu from which the other features operate. 
##### How it works
Reusing the 'ask_pin' function from before, the users 'pin' input is then run through the 'get_account' function again. If the 'get_account' function does not return 'None', the row it returns is then assigned to the varibale 'current_user'. Each key from the dictionary of the row in 'current_user' is the assigned as parameters to the secodray menu alongside the file name. Because the secondary menu is accessed with the information relating to user from the file, user pin is no longer required until returning to initial menu.

#### View Balance
This displays the current users remaining balance. 
##### How it works
Utilising the 'get_account' function, the balance is assigned to a variable and the printed to screen. 

#### Withdraw
User is able to input a value amount which is subtracted from running balance. A printed message is then displayed informing user of transaction. 
##### How it works

#### Deposit
User is able to input a value amount which is subtracted from running balance. A printed message is then displayed informing user of transaction. 
#### Remove Account
#### Return and Exit

#### Menus

### Styling

### Getting Started / Help

### Using the Application

### Implementation
A link to Trello Board, which tracks progress through application development.

[**Trello**](https://trello.com/invite/b/KILIAHaw/ATTIb8887dfc104ceaad83abb75cca741b9bAF9170F3/terminal-app)
Prioritisation via color coding where red was highest priority.



### References

https://docs.python.org/3/library/csv.html

https://docs.pytest.org/en/8.2.x/

https://docs.python.org/3/library/os.path.html

https://dslackw.gitlab.io/colored/

https://peps.python.org/pep-0008/#introduction