{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "3ca6dcdf",
   "metadata": {},
   "source": [
    "## Description\n",
    "An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.\n",
    "\n",
    "In the Gregorian calendar, three conditions are used to identify leap years:\n",
    "* The year can be evenly divided by 4, is a leap year, unless:\n",
    "  + The year can be evenly divided by 100, it is NOT a leap year, unless:\n",
    "    + The year is also evenly divisible by 400. Then it is a leap year.\n",
    "    \n",
    "This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. Source\n",
    "\n",
    "## Task\n",
    "\n",
    "Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.\n",
    "\n",
    "Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.\n",
    "\n",
    "## Solution:\n",
    "```python\n",
    "def is_leap(year):\n",
    "    '''Checking whether year is a leap year'''\n",
    "    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)\n",
    "\n",
    "year = int(raw_input())\n",
    "print is_leap(year)\n",
    "```"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
