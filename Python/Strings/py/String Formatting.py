{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "1cfb454a",
   "metadata": {},
   "source": [
    "## Solution:\n",
    "```python\n",
    "def print_formatted(number):\n",
    "    width = len(\"{0:b}\".format(number))\n",
    "    for i in range(1, number + 1):\n",
    "        print(\"{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}\".format(i, width=width))\n",
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
