{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Find the match"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the new number: 1\n",
      "Enter the new number: 2\n",
      "Enter the new number: 3\n",
      "Enter the new number: 4\n",
      "Enter the new number: 5\n",
      "Enter the new number: 6\n",
      "Enter the new number: 7\n",
      "Enter the new number: 1\n",
      "Your list:  [1, 2, 3, 4, 5, 6, 7, 1]\n",
      "It's a match!\n"
     ]
    }
   ],
   "source": [
    "list_y = []\n",
    "\n",
    "for i in range(0,8):\n",
    "    new_no = int(input(\"Enter the new number: \"))\n",
    "    list_y.append(new_no)\n",
    "    \n",
    "print(\"Your list: \",list_y)\n",
    "match = False\n",
    "\n",
    "for i in range(0,8):\n",
    "    if list_y[i] == 1:\n",
    "        for j in range(i+1,8):\n",
    "            if list_y[j] == 5:\n",
    "                for k in range(j+1,8):\n",
    "                    if list_y[k] == 1:\n",
    "                        match = True \n",
    "                    else: continue\n",
    "            else: continue\n",
    "    else: continue\n",
    "        \n",
    "if match == False: print(\"It's Gone!\")\n",
    "else: print(\"It's a match!\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
