{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "c954a574",
   "metadata": {},
   "source": [
    "## Solution:\n",
    "```python\n",
    "def minion_game(string):\n",
    "    vowels = 'AEIOU'\n",
    "    Stuart_score, Kevin_score = 0, 0\n",
    "    length = len(string)\n",
    "    for start_idx in range(length):\n",
    "        score = length - start_idx\n",
    "        if string[start_idx] in vowels:\n",
    "            Kevin_score += score\n",
    "        else:\n",
    "            Stuart_score += score\n",
    "    if Stuart_score == Kevin_score:\n",
    "        print('Draw')\n",
    "    if Stuart_score > Kevin_score:\n",
    "        print('Stuart {}'.format(Stuart_score))\n",
    "    if Stuart_score < Kevin_score:\n",
    "        print('Kevin {}'.format(Kevin_score))\n",
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
