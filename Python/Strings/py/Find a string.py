{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "c6bd6a4c",
   "metadata": {},
   "source": [
    "## Solution:\n",
    "```python\n",
    "def count_substring(string, sub_string):\n",
    "    count = 0\n",
    "    for i in range(len(string) - len(sub_string) + 1):\n",
    "        if string[i: i + len(sub_string)] == sub_string:\n",
    "            count += 1\n",
    "    return count\n",
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
