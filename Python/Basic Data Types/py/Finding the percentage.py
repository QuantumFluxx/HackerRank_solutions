{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "a3bc0c14",
   "metadata": {},
   "source": [
    "## Solution:\n",
    "```python\n",
    "if __name__ == '__main__':\n",
    "    N = int(input())\n",
    "    stud_marks = {}\n",
    "\n",
    "for line in range(N):\n",
    "    info = input().split(\" \")\n",
    "    grades = list(map(float, info[1:]))\n",
    "    stud_marks[info[0]] = sum(grades) / float(len(grades))\n",
    "\n",
    "print(\"%.2f\" % round(stud_marks[input()], 2))\n",
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
