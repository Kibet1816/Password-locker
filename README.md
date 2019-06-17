# Password Locker

## Description

 This is a CLI application that allows a user to store multiple passwords relevant to the account created.

## Authors

This program was written by [Denis Kibet](https://github.com/Kibet1816)

## Setup and usage instructions

- Clone this repository or download the zip.
- In your terminal, run  `./run.py` to use the application.
- Create your own account by using the short code `li`.
- Enjoy the application.

## BDD
| Input        | Behaviour           | Outcome  |
| ------------- |:-------------:| -----:|
| Keys in `li` | Application loads | Input fields for the names and password appear |
| Adds the names and prefered password | User creates an account in password locker | Short commands for navigation appear |
| Keys in `ca` | Input fields appear | User enters account name and username |
| Keys in `ep` in password field | Input field for custom password appears | User can input preferred password |
| Keys in `gp` in password field | Automatic password is generated | Account is created |
| Keys in `da` | All acounts are loaded | The accounts are displayed by the name,username and password |

## Technologies used

Technologies used to write the application are:
- Python

## Known bugs and malfunctions
There are no known bugs.If found please contact the developer through [email](https://www.gmail.com).

#### License and copyright information

[MIT license](https://github.com/Kibet1816/Password-locker/blob/master/license.md)

Copyright (c) 2019 Denis Kibet
