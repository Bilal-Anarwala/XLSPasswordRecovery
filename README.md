# XLSPasswordRecovery

In this project, I tackled an urgent request from Mr. Frank-Lee InTrouble, the new Human Resources Director at our consulting firm. After the sudden dismissal of the previous HR director, Mr. InTrouble found himself locked out of a crucial Excel spreadsheet containing secret codes required to process salary adjustments for the upcoming fiscal year.

The challenge was to recover access to the password-protected Excel file, as the former HR director, the only person who knew the password, was unreachable. Without these codes, payroll processing could not move forward, affecting all consultants in the company.

# Methodology

*To crack the Excel password, I used a Python-based approach leveraging the following tools and methods:

Python & msoffcrypto module: A Python library specifically designed for unlocking password-protected Microsoft Office files.*

*Dictionary Attack: I utilized a pre-existing list of common passwords stored in a text file to attempt various combinations on the Excel file.*

*Python Script: The script systematically tried each password from the list using the msoffcrypto library until the correct one, “secret,” was found.*

