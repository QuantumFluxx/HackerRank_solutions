{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "b705e488",
   "metadata": {},
   "source": [
    "## Solution:\n",
    "```bash\n",
    "#!/bin/bash\n",
    "read X\n",
    "read Y\n",
    "if (( $X > $Y ))\n",
    "then\n",
    "    echo \"X is greater than Y\"\n",
    "fi\n",
    "\n",
    "if (( $X == $Y))\n",
    "then\n",
    "    echo \"X is equal to Y\"\n",
    "fi\n",
    "\n",
    "if(( $X < $Y))\n",
    "then\n",
    "    echo \"X is less than Y\"\n",
    "fi\n",
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
