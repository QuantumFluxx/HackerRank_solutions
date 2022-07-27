{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "158631fa",
   "metadata": {},
   "source": [
    "## Solution:\n",
    "```python\n",
    "thickness = int(input()) #This must be an odd number\n",
    "c = 'H'\n",
    "\n",
    "# Top Cone\n",
    "for i in range(thickness):\n",
    "    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))\n",
    "\n",
    "# Top Pillars\n",
    "for i in range(thickness+1):\n",
    "    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))\n",
    "\n",
    "# Middle Belt\n",
    "for i in range((thickness+1)//2):\n",
    "    print((c*thickness*5).center(thickness*6))\n",
    "\n",
    "# Bottom Pillars\n",
    "for i in range(thickness+1):\n",
    "    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))\n",
    "\n",
    "# Bottom Cone\n",
    "for i in range(thickness):\n",
    "    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "581df44e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "    H    \n",
      "   HHH   \n",
      "  HHHHH  \n",
      " HHHHHHH \n",
      "HHHHHHHHH\n",
      "  HHHHH               HHHHH             \n",
      "  HHHHH               HHHHH             \n",
      "  HHHHH               HHHHH             \n",
      "  HHHHH               HHHHH             \n",
      "  HHHHH               HHHHH             \n",
      "  HHHHH               HHHHH             \n",
      "  HHHHHHHHHHHHHHHHHHHHHHHHH   \n",
      "  HHHHHHHHHHHHHHHHHHHHHHHHH   \n",
      "  HHHHHHHHHHHHHHHHHHHHHHHHH   \n",
      "  HHHHH               HHHHH             \n",
      "  HHHHH               HHHHH             \n",
      "  HHHHH               HHHHH             \n",
      "  HHHHH               HHHHH             \n",
      "  HHHHH               HHHHH             \n",
      "  HHHHH               HHHHH             \n",
      "                    HHHHHHHHH \n",
      "                     HHHHHHH  \n",
      "                      HHHHH   \n",
      "                       HHH    \n",
      "                        H     \n"
     ]
    }
   ],
   "source": [
    "thickness = int(input()) #This must be an odd number\n",
    "c = 'H'\n",
    "\n",
    "# Top Cone\n",
    "for i in range(thickness):\n",
    "    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))\n",
    "\n",
    "# Top Pillars\n",
    "for i in range(thickness+1):\n",
    "    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))\n",
    "\n",
    "# Middle Belt\n",
    "for i in range((thickness+1)//2):\n",
    "    print((c*thickness*5).center(thickness*6))\n",
    "\n",
    "# Bottom Pillars\n",
    "for i in range(thickness+1):\n",
    "    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))\n",
    "\n",
    "# Bottom Cone\n",
    "for i in range(thickness):\n",
    "    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))"
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
