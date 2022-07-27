{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "3c4abc4d",
   "metadata": {},
   "source": [
    "## Task\n",
    "The provided code stub reads two integers,  and , from STDIN.\n",
    "\n",
    "Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .\n",
    "\n",
    "No rounding or formatting is necessary.\n",
    "\n",
    "Example\n",
    "\n",
    "a = 3\n",
    "\n",
    "b = 5\n",
    "\n",
    "The result of the integer division 3//5=0.\n",
    "The result of the float division is 3/5=0.6.\n",
    "Print:\n",
    "```\n",
    "0\n",
    "0.6\n",
    "```\n",
    "\n",
    "## Solution:\n",
    "```python\n",
    "if __name__ == '__main__':\n",
    "    a = int(raw_input())\n",
    "    b = int(raw_input())\n",
    "    print(a//b)\n",
    "    print(a/b)\n",
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
