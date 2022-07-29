{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "92760312",
   "metadata": {},
   "source": [
    "## Solution:\n",
    "```bash\n",
    "declare -A a\n",
    "f() {\n",
    "    local d=$1 l=$2 r=$3 c=$4\n",
    "    [[ $d -eq 0 ]] && return\n",
    "    for ((i=l; i; i--)); do\n",
    "        a[$((r-i)).$c]=1\n",
    "    done\n",
    "    ((r -= l))\n",
    "    for ((i=l; i; i--)); do\n",
    "        a[$((r-i)).$((c-i))]=1\n",
    "        a[$((r-i)).$((c+i))]=1\n",
    "    done\n",
    "    f $((d-1)) $((l/2)) $((r-l)) $((c-l))\n",
    "    f $((d-1)) $((l/2)) $((r-l)) $((c+l))\n",
    "}\n",
    "read n\n",
    "f $n 16 63 49\n",
    "for ((i=0; i<63; i++)); do\n",
    "    for ((j=0; j<100; j++)); do\n",
    "        if [[ ${a[$i.$j]} ]]; then\n",
    "            printf 1\n",
    "        else\n",
    "            printf _\n",
    "        fi\n",
    "    done\n",
    "    echo\n",
    "done\n",
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
