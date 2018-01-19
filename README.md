# Password Strength Calculator

The program checks user's password by strength criteria list. Criteria list includes following:

1. the use of both upper-case and lower-case letters (case sensitivity)
2. inclusion of one or more numerical digits
3. inclusion of special characters, such as @, #, $
4. prohibition of words found in a password blacklist
5. prohibition of passwords that match the format of calendar dates and telephone numbers.

Furthermore evaluates the password from 0 to 10. If programm finds password in blacklist file, a warning message with score of 0 will appear in console. You can create your own blacklist file(the program works only with the "UTF-8" encoding) or add weak passwords into example file (blacklist.txt). More examples of bad passwords you can find [here](https://github.com/danielmiessler/SecLists/tree/master/Passwords).

# Quickstart
The program takes path to text blacklist file with weak passwords as an argument (for example, blacklist.txt).

Example of script launch on Windows, Python 3.5:

``` bash

$ python password_strength.py blacklist.txt

```

After that needs to type your password for test and will see strength password score. For example:

``` bash

Type your password:
User's password: 12345
Password strength score: 0-password from blacklist

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
