{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "e6cd6f86",
   "metadata": {},
   "source": [
    "## Solution:\n",
    "```bash\n",
    "#!/bin/bash\n",
    "read x\n",
    "read y\n",
    "read z\n",
    "if ((($x == $y) && ($y == $z)))\n",
    "\tthen\n",
    "\techo \"EQUILATERAL\"\n",
    "elif ((($x == $y) || ($x == $z) || ($y == $z)))\n",
    "\tthen\n",
    "\techo \"ISOSCELES\"\n",
    "else\n",
    "\techo \"SCALENE\"\n",
    "fi \n",
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
