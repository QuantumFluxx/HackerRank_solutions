{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "bd30b661",
   "metadata": {},
   "source": [
    "## Solution:\n",
    "```Python\n",
    "if __name__ == '__main__':\n",
    "    std = []\n",
    "    for _ in range(int(input())):\n",
    "        name = input()\n",
    "        score = float(input())\n",
    "        std.append([name, score])\n",
    "    \n",
    "    min_num = std[0][1]\n",
    "    index = [0]\n",
    "    for i in range(1, len(std)):\n",
    "        if std[i][1] < min_num:\n",
    "            min_num = std[i][1]\n",
    "            index[0] = i\n",
    "    \n",
    "    for i in range(len(std)):\n",
    "        if std[i][1] == min_num and i not in index:\n",
    "            index.append(i)\n",
    "    index.reverse()    \n",
    "    for i in index:\n",
    "        std.pop(i)\n",
    "    sol = [std[0][0]]\n",
    "    min_num = std[0][1]\n",
    "    for i in range(1, len(std)):\n",
    "        if std[i][1] < min_num:\n",
    "            min_num = std[i][1]\n",
    "            sol[0] = std[i][0]\n",
    "        elif std[i][1] == min_num:\n",
    "            sol.append(std[i][0])\n",
    "    \n",
    "    sol.sort()\n",
    "    for i in sol:\n",
    "        print(i)\n",
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
