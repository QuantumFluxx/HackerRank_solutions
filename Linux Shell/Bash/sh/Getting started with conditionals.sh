{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "8e56a278",
   "metadata": {},
   "source": [
    "## Solution:\n",
    "```bash\n",
    "#!/bin/bash\n",
    "read word\n",
    "if [[($word == 'y') || ($word == 'Y')]]\n",
    "then\n",
    "    echo \"YES\"\n",
    "        elif [[($word == 'n') || ($word == 'N')]]\n",
    "        then\n",
    "        echo \"NO\"\n",
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
