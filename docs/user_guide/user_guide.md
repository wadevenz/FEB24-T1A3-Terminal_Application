# User Guide

## Terminal Bank

Welcome to the user guide for the Terminal Bank application. The following is a standard run through of what the application will look like and its major features. This user guide will also highlight some potential barriers you may encounter.

### Welcome Menu
![Welcome Menu](/docs/user_guide/open_menu.png)

This is the initial screen once opening the application. As you can see there are 3 options provided here each labelled '1', '2' and '3'. To choose an option just type the corresponding number into the terminal and press 'Enter'. Firstly, lets create an account. Type '1' into your terminal and press 'Enter'.

### Creating an account
![Create Account](/docs/user_guide/name_pin.png)

After selecting to create an account, you will be immediately asked to enter your name and then a 4 digit PIN. In this case we have entered the name 'Test' and the PIN '0000' into the terminal. 
Please note that if the PIN input does not contain only 4 digits, the error message below will display.

![Invalin PIN](/docs/user_guide/invalid_pin.png)

Once you have correctly entered your name and a valid PIN, a message will display, confirming you have opened an account. 

![open account](/docs/user_guide/open_acc_print.png)

You will notice that a bonus $100 has been added to the balance to be able to utilise any feature immediately. 

### Accessing your account
![Welcome Menu](/docs/user_guide/open_menu.png)

Now back at the start, lets access the account we have just opened. Enter '2' into the terminal.

![Accessed Menu](/docs/user_guide/accessed_menu.png)

We've made it to the main menu inside the account. From here we can select all the major features of the application. 

### Viewing your balance
![View balance](/docs/user_guide/balance_view.png)

By entering '1' from the access menu we can view our current balance. As we have just created the account it will display $100, however interaction with other features may change your balance in the future. 

### Withdraw
Now lets withdraw some imaginary funds. Enter '2' from the access menu and you will be asked to input an amount.

![enter amount](/docs/user_guide/enter_amount.png)

For example, lets witdraw $50 by inputting the number '50' into our terminal. Success!

![withdraw](/docs/user_guide/print_withdraw.png)

However, if you attempted to input a number greater than what you have in your balance you would receive a message stating "Insufficient Funds".

![Insufficient](/docs/user_guide/insufficient_err.png)

Now we have $50 in our account, let's put some more in.

### Deposit
Back at the access menu, we can enter '3' to utilise the deposit feature. 

![deposit](/docs/user_guide/print_deposit.png)

Here we entered the number '25' and deposited $25. As you can see our new total balance is $75.

There may be an error encountered when inputting an amount value. Only digits will be accepted otherwise you will see displayed an error message. If this happens, no problems! Just try again.

![err type](/docs/user_guide/type_err.png)


### Removing an account
While in the access menu you can remove your current account. Enter '4' in the menu. You will then be asked to confirm your decision by inputing Y or N. 
If you enter Y:

![removal Y](/docs/user_guide/removal_y_msg.png)

You have successfully removed your account and your total balance will be displayed. The application will take you back to the opening menu.

If you enter N:

![removal N](/docs/user_guide/removal_n_msg.png)

Your account remains with the balance in place.

### Another poosible error
![invalid option](/docs/user_guide/invalid_option_err.png)

Before we exit return to the opening menu and exit, there is another possible error that can be encountered. While in menus, if an option that is not displayed is entered, you will receive the error message above and you will be returned to the menu you came from. 

### Returning to opening menu and exiting. 
![Accessed Menu](/docs/user_guide/accessed_menu.png)

Now we have used the features of this application, we can go back to the opening Welcome menu to either Create a new account, Access another existing account, or Exit the application.
Enter '5' to go back.

![Welcome Menu](/docs/user_guide/open_menu.png)

If we are all done with the application you can exit by pressing '3' from the Welcome menu.

Hope you have found this guide useful, Thanks again for using the Terminal Bank application!

![thank you](/docs/user_guide/final_msg.png)