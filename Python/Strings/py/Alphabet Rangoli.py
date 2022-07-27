{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "713fad8f",
   "metadata": {},
   "source": [
    "## Solution:\n",
    "```python\n",
    "def print_rangoli(size):\n",
    "    alpha = \"abcdefghijklmnopqrstuvwxyz\"\n",
    "    data = [alpha[i] for i in range(n)]\n",
    "    items = list(range(n))\n",
    "    items = items[:-1]+items[::-1]\n",
    "    for i in items:\n",
    "        temp = data[-(i+1):]\n",
    "        row = temp[::-1]+temp[1:]\n",
    "        print(\"-\".join(row).center(n*4-3, \"-\"))\n",
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
