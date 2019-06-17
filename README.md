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
| Behaviour        | Input           | Outcome  |
| ------------- |:-------------:| -----:|
| Short codes display | User keys in `li` | Input fields for the names and password appear |
| Input fields accept input | User adds his/her name and password | Password locker account is created |
| Other short codes appear | User keys in `ca` | User enters account name and username |
| Options for password input display | User enters `ep` | User can input preferred password |
| Options for password input display | User keys in `gp` | An 8 character password is generated automatically |
| Short codes reappear | User keys in `da` | The accounts are displayed by the name,username and password |
| Short codes displayed | User keys in`lo` | The user logs out of his/her password locker account |
| Initial short codes appear | User keys in `ex` | User exits the application |

## Technologies used

Technologies used to write the application are:
- Python

## Known bugs and malfunctions
There are no known bugs.If found please contact the developer through [email](https://www.gmail.com).

#### License and copyright information

[MIT license](https://github.com/Kibet1816/Password-locker/blob/master/license.md)

Copyright (c) 2019 Denis Kibet
