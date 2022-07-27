{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "ea7d35d5",
   "metadata": {},
   "source": [
    "## Solution:\n",
    "```sql\n",
    "SELECT DISTINCT CITY\n",
    "FROM STATION\n",
    "WHERE MOD(ID, 2) = 0\n",
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
