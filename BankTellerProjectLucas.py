#!/usr/bin/env python
# coding: utf-8

# # Bank Teller
# 

# In this project you will be implementing code that emulates transactions performed between a bank-teller and a customer. 

# The prerequisites for this project are Python 3 syntax, functions and control flow. Let's jump right into it!

# ### 1. Initializing savings and checking account values. 
# 
# Creates two variables, one named `checking_balance` and the other `savings_balance`. Assign them both the value of zero. Use these as your starting bank balances.

# In[1]:


#accounts
checking_balance = 0

savings_balance = 0


# ### 2. Create a function to check the Balance
# 
# ##### step 1. Check account_type and return the respective balance
#     
# Define a function named `check_balance()` that accepts three parameters `account_type`, `checking_balance` and `savings_balance`. `account_type` represents a string which can either be `"savings"` or `"checking"`. `checking_balance` and `savings_balance`represent the respective number balances.
#    
# #####  step 2. Check account_type and return the respective balance
#     
# Within the function named `check_balance()`, create an if...elif...else statement. Within each if statement return the customers balance based on the type of `account_type` they requested.
#    
# ##### step 3. Assigning the savings_balance
#    
# Within the first `if` statement use an equal operator to check whether `account_type` is the same as `"savings"`. If that is true, set the new variable `balance` to the value of `savings_balance`.
#    
# ##### step 4. Assigning the checking_balance
#    
# Within the second `elif` statement use an equal operator to check whether `account_type` is the same as `"checking"`. If that is true, set the variable `balance` to the value of `checking_balance`.
#    
# ##### step 5. Return an error statement if there are no matching account_type
#    
# Within the `else` statement, return an error statement given that there were no matches for the previous `if...elif` statements. Within the else statement, `return` `"Unsuccessful, please enter \"checking\" or \"savings\""`
#    
# ##### step 6. Create a balance statement
#    
# Under the `if` statements, create a new variable called `balance_statement` and assign it a value that consists of strings and variables. Concatenate the variables `account_type` and `balance` into the account statement. Remember to cast `balance` to a string using `str()` in the statement. The statement should be: "Your `account_type` balance is `balance`".
#    
# ##### step 7. Return balance statement
#    
# Under the `balance_statement` assignment, close out the `check_balance()` function by adding a `return` statement that returns the `balance_statement` variable. 

# In[2]:


checking_balance = 0

savings_balance = 0
def check_balance(account_type, checking_balance, savings_balance):
    if account_type == "savings":
        balance = savings_balance 
    elif account_type == "checking":
        balance = checking_balance
    else:
        return "Unsuccessful, please enter \"checking\" or \"savings\""
    balance_statement = "Your " + account_type + " balance is " + str(balance)
    return balance_statement


# ### 3. Calling and Printing the check_balance() function for Checking Account

# Now that you have completed the `check_balance()` function, call it inside a `print()` function. Call the `check_balance()` function with these arguments; `"checking"`, `checking_balance` and `savings_balance`. The latter two were already initialized at the start of the project. Your checking balance should print.

# In[3]:


print(check_balance("checking", checking_balance, savings_balance))


# ### 4. Calling and Printing the check_balance() function for Savings Account

# On the next line, inside a `print()` function call the `check_balance()` function with these arguments; `"savings"`, `checking_balance` and `savings_balance`. Your savings balance should print. 

# In[4]:


print(check_balance("savings", checking_balance, savings_balance))


# # 5. Create a function to make a deposit
# 
# ##### step 1. define function
# Define a function named `make_deposit()` that accepts four parameters `account_type`, `amount`, `checking_balance` and `savings_balance`. The `amount` represents the amount to be deposited. 
#   
# ##### step 2. Initialize deposit_status variable
# Inside the deposit function, start by creating a variable named `deposit_status` and assign it to a an empty string
#    
# ##### step 3. Ensure deposit is greater than 0 
# Write an if statement that checks whether the passed in `amount` is greater than 0. Step 5 will continue putting code inside this `if` statement if `amount` is greater than 0.
# 
# ##### step 4. Error if amount is less than 0
# Write a corresponding `else` statement if the `if` statement fails. Within that `else`, assign the variable `deposit_status` to the string value `"unsuccessful, please enter an amount greater than 0"`
#   
# ##### step 5. Checking account_type
# Within the `if` statement that ensures that the amount is greater than 0, write inner `if...elif...else` statements. Within each if statement add the passed in `amount` to the customers balance based on the type of `account_type` they requested and also set `deposit_status` to `"successful"` or an error message. 
#   
# ##### step 6. Deposit to Savings account
# Within the first nested `if` statement check whether `account_type` is equivalent to `"savings"`. Then within this `if` statement on the next line add `amount` to `savings_balance` using the `+=` assignment operator. On the next line assign the string value `"successful"` to the variable `deposit_status`.
#   
# ##### step 7. Deposit to Checking account
# Within the next nested `elif` statement check whether `account_type` is equivalent to `"checking"`. Then within this `elif` statement on the next line add `amount` to `checking_balance` using the `+=` assignment operator. On the next line assign the string value `"successful"` to the variable `deposit_status`.
#   
# ##### step 8. Assign an error statement if there are no matching account_type
# Within the next nested `else` statement, assign the string value `"Unsuccessful, please enter \"checking\" or \"savings\""` to the variable `deposit_status`.
#   
# ##### step 9. Create a deposit statement
# Outside of all the `if` statements but still in the function, compose a statement composing of strings and variables used in this function. Then assign it to the new `deposit_statement` variable. The statement should be: "Deposit of `amount` to your `account_type` account was `deposit_status`". 
# 
# ##### step 10. Print deposit statement
# On the next line, write a print statement with the `deposit_statement` as an argument. This will print the deposit statement anytime the deposit function is called. 
# 
# ##### step 11. Return savings_balance and checking_balance
# On the next line return both the `savings_balance` and `checking_balance`. This will conclude the `make_deposit()` function.

# In[5]:


#make deposit function
def make_deposit(account_type, amount, checking_balance,savings_balance):
    deposit_status = ""
    if amount > 0:
        if account_type == "savings":
            savings_balance += amount
            deposit_status = "successful"
        elif account_type == "checking":
            checking_balance += amount
            deposit_status = "successful"
        else:
            deposit_status = "Unsuccessful, please enter \"checking\" or \"savings\""
    else:
        deposit_status = "unsuccessful, please enter an amount greater than 0"
        
    deposit_statement = "Deposit of " + str(amount) + " to your " + account_type + " account was " + deposit_status + "."
    
    #print function
    print(deposit_statement)
    return savings_balance, checking_balance


# ### 6. Call deposit function and make a savings deposit
# 
# On the next line, call the `make_deposit()` function with these arguments; `"savings"`, `10`,`checking_balance` and `savings_balance`. Assign the function call to the matching `checking_balance` and `savings_balance` variables that are also being returned by the function. That is how the new balances are being updated. 

# In[6]:


savings_balance, checking_balance = make_deposit("savings", 10,checking_balance, savings_balance)


# ### 7. Print savings balance call after making a savings deposit
# 
# Now that a deposit has been made to the savings account, print your savings balance. Call the `check_balance()` function with these arguments; `"savings"`, `checking_balance` and `savings_balance` within a print function. Your new savings balance should print.

# In[7]:


print(check_balance("savings", checking_balance, savings_balance))


# ### 8. Call deposit function and make a checking deposit
# 
# On the next line, call the `make_deposit()` function with these arguments; `"checking"`, `200`,`checking_balance` and `savings_balance`. Assign the function call to the matching `checking_balance` and `savings_balance` variables that are also being returned by the function. 

# In[8]:


savings_balance, checking_balance = make_deposit("checking", 200,checking_balance, savings_balance)


# ### 9. Print checking balance call after making a checking deposit
# 
# Now that a deposit has been made to the checking account, print our new checking balance. Call the `check_balance()` function with these arguments; `"checking"`, `checking_balance` and `savings_balance` within a print function. Your new checking balance should print.

# In[9]:


print(check_balance("checking", checking_balance, savings_balance))


# ### 10. Create a function to make a withdrawal
# 
# ##### step 1. define function
# Define a function named `make_withdrawal()` that accepts four parameters `account_type`, `amount`, `checking_balance` and `savings_balance`. The `amount` represents the withdrawal amount. 
# 
# ##### step 2. Initialize withdrawal_status variable
# Inside the withdrawal function, start by creating a variable named `withdrawal_status` and assign it to an empty string. 
# 
# ##### step 3. Initialize an error message
# On the next line create a variable named `fail` and assign it to the value `"unsuccessful, please enter amount less than balance"` 
# 
# ##### step 4. Checking account_type
# Write `if...elif...else` statements. Within each if statement check whether the `account_type` is equivalent to `savings_balance` or `checking_balance`. If neither, throw an error in the else statement.
# 
# ##### step 5. Withdrawal from savings account
# The first `if` statement should check whether `account_type` is equivalent to `"savings"`. 
# 
# ##### step 6. Ensure withdrawal is less than savings account
# Then write an inner `if...else` that checks if the withdrawal amount is greater than the savings balance. If the amount is indeed greater, in the else statement, assign `withdrawal_status` to the variable `fail`.
# 
# ##### step 7. Subtract amount from savings account
# Within the inner `if` statement, subtract `amount` from the `savings_balance` using the `-=` assignment operator. On the next line assign the string value `"successful"` to the variable `withdrawal_status`. 
# 
# ##### step 8. Withdrawal from checking account
# The next `elif` statement should check whether `account_type` is equivalent to `"checking"`. 
# 
# ##### step 9. Ensure withdrawal is less than checking account
# Then write an inner `if...else` that checks if the withdrawal amount is greater than the checking balance. If the amount is indeed greater, in the else statement, assign `withdrawal_status` to the variable `fail`.
# 
# ##### step 10. Subtract amount from checking account
# Within the inner `if` statement, subtract `amount` from the `checking_balance` using the `-=` assignment operator. On the next line assign the string value `"successful"` to the variable `withdrawal_status`. 
# 
# ##### step 11. Assign an error statement if there are no matching account_type
# Within the last `else` statement, assign the string value `"unsuccessful, please enter \"checking\" or \"savings\""` to the variable `withdrawal_status`.
# 
# ##### step 12. Create a withdrawal statement
# Outside of all the `if` statements but still in the function, create a statement composing of strings and variables used in this function. Then assign it to the new `withdrawal_statement` variable. The withdrawal statement should be: "Withdrawal of `amount` from your `account_type` was `withdrawal_status`". 
# 
# ##### step 13. Print withdrawal statement
# On the next line, write a print statement with the `withdrawal_statement` as an argument. This will print the withdrawal statement anytime the deposit function is called. 
# 
# ##### step 14. Return savings_balance and checking_balance
# On the next line return both the `savings_balance` and `checking_balance`. This will conclude the `make_withdrawal()` function.

# In[10]:


#Withdrawal function
def make_withdrawal(account_type, amount, checking_balance, savings_balance):
    withdrawal_status = ""
    fail = "unsuccessful, please enter amount less than balance"
    if account_type == "savings":
        if amount <= savings_balance:
            savings_balance -= amount
            withdrawal_status = "successful"
        else:
            withdrawal_status = fail
    elif account_type == "checking":
        if amount < checking_balance:
            checking_balance -= amount
            withdrawal_status = "successful"
    else:
        withdrawal_status = "unsuccessful, please enter \"checking\" or \"savings\""
    
    withdrawal_statement = "Withdrawal of " + str(amount) + " from your " + account_type + " was " + withdrawal_status
    
    #print
    print(withdrawal_statement)
    
    return savings_balance,checking_balance


# ### 11. Call withdrawal function and make a savings withdrawal
# 
# On the next line, call the `make_withdrawal()` function with these arguments: `"savings"`, `11`,`checking_balance` and `savings_balance`. Assign the function call to the matching `checking_balance` and `savings_balance` variables that are also being returned by the function. That is how the new balances are being updated. 

# In[11]:


#calling withdrawal

savings_balance, checking_balance = make_withdrawal("savings", 11, checking_balance, savings_balance)


# ### 12. Print savings balance call, after making a savings withdrawal
# 
# Now that a withdrawal has been made from the savings account, print our savings balance. Call the `check_balance()` function with these arguments; `"savings"`, `checking_balance` and `savings_balance` within a print function. Your new savings balance should print. 

# In[12]:


print(check_balance("savings", checking_balance, savings_balance))


# ### 13. Call withdrawal function and make a checking withdrawal
# 
# On the next line, call the `make_withdrawal()` function with these arguments; `"checking"`, `170`,`checking_balance` and `savings_balance`. Assign the function call to the matching `checking_balance` and `savings_balance` variables that are also being returned by the function. That is how the new balances are being updated. 

# In[13]:


savings_balance, checking_balance = make_withdrawal("checking", 170,checking_balance, savings_balance)


# ### 14. Print checking balance call, after making a checking withdrawal
# 
# Now that a withdrawal has been made from the checking account, print our checking balance. Call the `check_balance()` function with these arguments; `"checking"`, `checking_balance` and `savings_balance` within a print function. Your new checking balance should print. 

# In[14]:


print(check_balance("checking", checking_balance, savings_balance))


# ### 15. Create a function to make a transfer between accounts
# 
# ##### step 1. define function
# Define a function named `acc_transfer()` that accepts five parameters `acc_from`, `acc_to`, `amount`, `checking_balance` and `savings_balance`.
# 
# ##### step 2. Initialize transaction_status variable
# Inside the transfer function, start by creating a variable named `transaction_status` and assign it to a an empty string. 
# 
# ##### step 3. Initialize an error message
# On the next line create a variable named `trans_error` and assign it to the value `"unsuccessful, please enter amount less than "` 
# 
# ##### step 4. Account Transfer
# Write `if...elif...else` statements. The `if` statement will check if the transfer is from savings to checking account. The `elif` statement will check if the transfer is from checking to savings account. If neither, throw an error in the else statement.
# 
# ##### step 5. Ensure transfer is less than savings account
# Within the first `if` statement, write an inner `if...else` that checks if the transfer amount is greater than the savings balance. If the amount is indeed greater, in the else statement, assign `transaction_status` to the variable `trans_error` + `str(savings_balance)`.
# 
# ##### step 6. Transfer amount from savings to checking account
# Within the inner `if` statement, subtract `amount` from the `savings_balance` using the `-=` assignment operator. On the next line, add `amount` to the `checking_balance` using the `+=` assignment operator. Then on the next line assign the string value `"successful"` to the variable `transaction_status`. 
# 
# ##### step 7. Ensure transfer is less than checking account
# Within the following `elif` statement, write an inner `if...else` that checks if the transfer amount is greater than the checking balance. If the amount is indeed greater, in the else statement, assign `transaction_status` to the variable `trans_error` + `str(checking_balance)`.
# 
# ##### step 8. Transfer amount from checking to savings  account
# Within the inner `if` statement, subtract `amount` from the `checking_balance` using the `-=` assignment operator. On the next line, add `amount` to the `savings_balance` using the `+=` assignment operator. Then on the next line assign the string value `"successful"` to the variable `transaction_status`. 
# 
# ##### step 9. Assign an error statement if there are no matching account_type
# Within the last `else` statement, assign the string value `"unsuccessful, please enter \"checking\" or \"savings\""` to the variable `transaction_status`.
# 
# ##### step 10. Create a transfer statement
# Outside of all the `if` statements but still in the function, compose a statement composing of strings and variables used in this function. Then assign it to the new `transaction_statement` variable. The transfer statement should be; "Transfer of `amount` from your `cc_from` to your `acc_to` account was `transaction_status`".
# 
# ##### step 11. Print transfer statement
# On the next line, write a print statement with the `transaction_statement` as an argument. This will print the transfer statement anytime the transfer function is called. 
# 
# ##### step 12. Return savings_balance and checking_balance
# On the next line return both the `savings_balance` and `checking_balance`. This will conclude the `acc_transfer()` function.

# In[15]:


def acc_transfer(acc_from, acc_to, amount, checking_balance, savings_balance):
    transaction_status = ""
    trans_error == "unsuccessful, please enter amount less than "
    
    if acc_from == "Savings" and acc_to == "Checking":
        if amount <= savings_balance:
            savings_balance -= amount
            checking_balance += amount
            transaction_status = "Successful"
        else:
            transaction_status = trans_error + str(savings_balance)

    elif acc_from == "checking" and acc_to == "savings":
        if amount <= checking_balance:
            checking_balance -= amount
            savings_balance += amount
            transaction_status = "Successful"
        else:
            transaction_status = trans_error + str(checking_balance)
    else:
        transaction_status = "unsuccessful, please enter \"checking\" or \"savings\""
    
    transaction_statement = "Transfer of" + amount + "from your" + cc_from + "to your" + acc_to + "account was" + transaction_status + "."
    print(transaction_statement)
    return savings_balance, checking_balance


# ### 16. Call transfer function and make a checking to savings transfer
# 
# On the next line, call the `acc_transfer()` function with these arguments; `"checking"`, `"savings"`, `40`,`checking_balance` and `savings_balance`. Assign the function call to the matching `checking_balance` and `savings_balance` variables that are also being returned by the function. 

# In[16]:


def acc_transfer(acc_from, acc_to, amount, checking_balance, savings_balance):
    transaction_status = ""
    trans_error = "unsuccessful, please enter amount less than "
    
    if acc_from == "Savings" and acc_to == "Checking":
        if amount <= savings_balance:
            savings_balance -= amount
            checking_balance += amount
            transaction_status = "successful"
        else:
            transaction_status = trans_error + str(savings_balance)

    elif acc_from == "checking" and acc_to == "savings":
        if amount <= checking_balance:
            checking_balance -= amount
            savings_balance += amount
            transaction_status = "successful"
        else:
            transaction_status = trans_error + str(checking_balance)
    else:
        transaction_status = "unsuccessful, please enter \"checking\" or \"savings\""
    
    transaction_statement = "Transfer of " + str(amount) + " from your " + acc_from + " to your " + acc_to + " account was " + transaction_status + "."
    print(transaction_statement)
    return savings_balance, checking_balance

savings_balance, checking_balance = acc_transfer("checking", "savings", 40 ,checking_balance, savings_balance)


# ### 17. Print checking balance after making a checking to savings transfer
# 
# Now that a transfer has been made from the checking to savings account, print your checking balance. Call the `check_balance()` function with these arguments; `"checking"`, `checking_balance` and `savings_balance` within a print function. Your new checking balance should print. 

# In[17]:


print(check_balance("checking", checking_balance, savings_balance))


# ### 18. Print savings balance after making a checking to savings transfer
# 
# Now that a transfer has been made from the checking to savings account, print your savings balance. Call the `check_balance()` function with these arguments; `"savings"`, `checking_balance` and `savings_balance` within a print function. Your new savings balance should print. 

# In[18]:


print(check_balance("savings", checking_balance, savings_balance))


# ### 19. Call transfer function and make a savings to checking transfer
# 
# On the next line, call the `acc_transfer()` function with these arguments; `"savings"`, `"checking"`, `5`,`checking_balance` and `savings_balance`. Assign the function call to the matching `checking_balance` and `savings_balance` variables that are also being returned by the function. That is how the new balances are being updated.
# 

# In[19]:


savings_balance, checking_balance = acc_transfer("savings", "checking", 5,checking_balance, savings_balance)


# ### 20. Print checking balance after making a savings to checking transfer
# 
# Now that a transfer has been made from the savings to checking account, print your checking balance. Call the `check_balance()` function with these arguments; `"checking"`, `checking_balance` and `savings_balance` within a print function. Your new checking balance should print.

# In[20]:


print(check_balance("checking", checking_balance, savings_balance))


# ### 21. Print saving balance after making a savings to checking transfer
# 
# Now that a transfer has been made from the savings to checking account, print your saving balance. Call the `check_balance()` function with these arguments; `"savings"`, `checking_balance` and `savings_balance` within a print function. Your new saving balance should print.

# In[21]:


print(check_balance("savings", checking_balance, savings_balance))


# ### 22. Conclusion
# 
# Congrats on completing a simple Python for Finance off-platform project. Feel free to change the variables to test the different possible outcomes. 

# In[ ]:





# In[ ]:




