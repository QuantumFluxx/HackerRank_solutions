{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "59348c94",
   "metadata": {},
   "source": [
    "## Solution:\n",
    "```bash\n",
    "sum=0\n",
    "read N\n",
    "\n",
    "for i in $(seq 1 $N); do\n",
    "    read number\n",
    "    sum=$(( $sum + $number ))\n",
    "done\n",
    "\n",
    "printf \"%.3f\\n\" `echo \"$sum / $N\" | bc -l`\n",
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
