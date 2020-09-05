# Pytest Framework

The problem: At my job we had a custom built Windows 10 application. There was no automation for the application and it was hard to get the application to launch with WinAppDriver.

The solution: Using Python, Winium, Selenium and PyAutoGui I was able to launch the application and find elements to interact with on the UI. I could then successfully write test cases for this application and connect to the SQL Server using PYODBC.


# Tech/Framework Used

Pytest - Allowed me to run the test suite

# Features

This project allows you to launch applications that WinAppDriver cannot launch. Any custom or older applications can be executed with Winium. When Elements cannot be found you can use PyAutoGui to click on the screen or write any text to a text box when Selenium cannot locate the element.

# Tests

Using the Pytest Framework I am able to execute tests as follows:

pytest -s .\tests\test_supplier_orders.py

# How to use?

Clone the repository and open in your IDE. Create a virtual enviroment and activate it. Then install the requirements.txt file using PIP.

pip -r install requirements.txt

You are then ready to create page objects and test files and execute them using Pytest.
