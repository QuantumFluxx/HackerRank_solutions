{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "e6e5332c",
   "metadata": {},
   "source": [
    "## Solution:\n",
    "```python\n",
    "if __name__ == '__main__':\n",
    "    s = input()\n",
    "    print(any([char.isalnum() for char in s]))\n",
    "    print(any([char.isalpha() for char in s]))\n",
    "    print(any([char.isdigit() for char in s]))\n",
    "    print(any([char.islower() for char in s]))\n",
    "    print(any([char.isupper() for char in s]))\n",
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
