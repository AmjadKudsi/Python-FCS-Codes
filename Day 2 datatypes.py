{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Data Types in Python"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1) Integers:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "int"
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a = 12\n",
    "type(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "12\n"
     ]
    }
   ],
   "source": [
    "print(a)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2) Float:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "metadata": {},
   "outputs": [],
   "source": [
    "b = 2.4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "float"
      ]
     },
     "execution_count": 133,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2.4\n"
     ]
    }
   ],
   "source": [
    "print(b)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "3) Strings:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 135,
   "metadata": {},
   "outputs": [],
   "source": [
    "String1 = (\"Hello\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "o\n"
     ]
    }
   ],
   "source": [
    "print(String1[-1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 139,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "llo\n"
     ]
    }
   ],
   "source": [
    "print(String1[2:]) String1."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 331,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'hello'"
      ]
     },
     "execution_count": 331,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "String1.casefold()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 332,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Hello'"
      ]
     },
     "execution_count": 332,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "String1.capitalize()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 333,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "       Hello        \n"
     ]
    }
   ],
   "source": [
    "s1 = String1.center(20)\n",
    "print(s1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 335,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 335,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "String1.count(\"l\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 336,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "b'Hello'\n"
     ]
    }
   ],
   "source": [
    "s2 = String1.encode()\n",
    "print(s2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 338,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "s3 = String1.endswith(\"o\")\n",
    "print(s3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 344,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "H         e         l         l         o\n"
     ]
    }
   ],
   "source": [
    "txt = \"H\\te\\tl\\tl\\to\"\n",
    "\n",
    "s4 =  txt.expandtabs(10)\n",
    "\n",
    "print(s4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 346,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n"
     ]
    }
   ],
   "source": [
    "s5 = String1.find(\"l\")\n",
    "print(s5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 350,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hel1o\n"
     ]
    }
   ],
   "source": [
    "s6 = (\"Hel{l}o\")\n",
    "print(s6.format(l = 1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "4) Lists:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 172,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['ENTC', 120, 'MECH', 130, 'COMP', [120, 120]]\n"
     ]
    }
   ],
   "source": [
    "list_of_students = [\"ENTC\",120,\"MECH\",130,\"COMP\",[120,120]]\n",
    "print(list_of_students)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 173,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['ENTC', 120, 'MECH', 130, 'COMP']"
      ]
     },
     "execution_count": 173,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list_of_students[:-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 174,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[120, 120]"
      ]
     },
     "execution_count": 174,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list_of_students[-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 175,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['ENTC', 120, 'MECH', 130, 'COMP', [120, 120], 'IT', 120]\n"
     ]
    }
   ],
   "source": [
    "list_of_students.append(\"IT\")\n",
    "list_of_students.append(120)\n",
    "print(list_of_students)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 176,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['ENTC', 120, 'MECH', 130, 'COMP', [120, 120], 'IT', 120]\n"
     ]
    }
   ],
   "source": [
    "backup_list = list_of_students.copy()\n",
    "print(backup_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 177,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 177,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list_of_students.count(120)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 178,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['ENTC', 120, 'MECH', 130, 'COMP', [120, 120], 'IT', 120, 'Civil', 120]\n"
     ]
    }
   ],
   "source": [
    "list3 = [\"Civil\",120]\n",
    "list_of_students.extend(list3)\n",
    "print(list_of_students)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 179,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n"
     ]
    }
   ],
   "source": [
    "x = list_of_students.index(\"COMP\")\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 180,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['MESCOE', 'ENTC', 120, 'MECH', 130, 'COMP', [120, 120], 'IT', 120, 'Civil', 120]\n"
     ]
    }
   ],
   "source": [
    "list_of_students.insert(0,\"MESCOE\")\n",
    "print(list_of_students)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 181,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['MESCOE', 'ENTC', 'MECH', 'COMP', 'IT', 'Civil']\n"
     ]
    }
   ],
   "source": [
    "list_of_students.pop(2)\n",
    "list_of_students.pop(3)\n",
    "list_of_students.pop(4)\n",
    "list_of_students.pop(-1)\n",
    "list_of_students.pop(-2)\n",
    "\n",
    "print(list_of_students)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 182,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['MESCOE', 'ENTC', 'MECH', 'COMP', 'IT']\n"
     ]
    }
   ],
   "source": [
    "list_of_students.remove(\"Civil\")\n",
    "print(list_of_students)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 183,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['IT', 'COMP', 'MECH', 'ENTC', 'MESCOE']\n"
     ]
    }
   ],
   "source": [
    "list_of_students.reverse()\n",
    "print(list_of_students)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 185,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['COMP', 'ENTC', 'IT', 'MECH', 'MESCOE']\n"
     ]
    }
   ],
   "source": [
    "list_of_students.sort()\n",
    "print(list_of_students)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 186,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[]\n"
     ]
    }
   ],
   "source": [
    "list_of_students.clear()\n",
    "print(list_of_students)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "5) Dictionary:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 210,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'name': 'COVID19', 'detected': 2020, 'type': 'infectious'}\n"
     ]
    }
   ],
   "source": [
    "virus = {\"name\": \"COVID19\",\n",
    "         \"detected\": 2020,\n",
    "         \"type\": \"infectious\"\n",
    "        }\n",
    "print(virus)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 211,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'name': 'COVID19', 'detected': 2020, 'type': 'infectious'}\n"
     ]
    }
   ],
   "source": [
    "backup = virus.copy()\n",
    "print(backup)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 212,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'name': 'nil', 'detected': 'nil', 'type': 'nil'}\n"
     ]
    }
   ],
   "source": [
    "a1 =\"nil\"\n",
    "thisdict = dict.fromkeys(virus,a1)\n",
    "print(thisdict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 213,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2020\n"
     ]
    }
   ],
   "source": [
    "a2 = virus.get(\"detected\")\n",
    "print(a2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 214,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "dict_items([('name', 'COVID19'), ('detected', 2020), ('type', 'infectious')])\n"
     ]
    }
   ],
   "source": [
    "a3 = virus.items()\n",
    "print(a3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 215,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "dict_keys(['name', 'detected', 'type'])\n"
     ]
    }
   ],
   "source": [
    "a4 = virus.keys()\n",
    "print(a4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 216,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'name': 'COVID19', 'detected': 2020}\n"
     ]
    }
   ],
   "source": [
    "virus.pop(\"type\")\n",
    "print(virus)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 217,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'name': 'COVID19'}\n"
     ]
    }
   ],
   "source": [
    "virus.popitem()\n",
    "print(virus)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 219,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "infectious\n",
      "{'name': 'COVID19', 'type': 'infectious'}\n"
     ]
    }
   ],
   "source": [
    "a5 = virus.setdefault(\"type\", \"infectious\")\n",
    "print(a5)\n",
    "print(virus)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 221,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'name': 'COVID19', 'type': 'infectious', 'detected': 2020}\n"
     ]
    }
   ],
   "source": [
    "virus.update({\"detected\": 2020})\n",
    "print(virus)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 222,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "dict_values(['COVID19', 'infectious', 2020])\n"
     ]
    }
   ],
   "source": [
    "a6 = virus.values()\n",
    "print(a6)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 223,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{}\n"
     ]
    }
   ],
   "source": [
    "virus.clear()\n",
    "print(virus)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "6) Sets:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 307,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'CPP', 'JAVA', 'PYTHON', 'C'}\n"
     ]
    }
   ],
   "source": [
    "proglangs = {\"C\", \"CPP\", \"JAVA\", \"PYTHON\"}\n",
    "print(proglangs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 308,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'CPP', 'C', 'JAVA', 'R', 'PYTHON'}\n"
     ]
    }
   ],
   "source": [
    "proglangs.add(\"R\")\n",
    "print(proglangs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 309,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'CPP', 'C', 'JAVA', 'R', 'PYTHON'}\n"
     ]
    }
   ],
   "source": [
    "backup = proglangs.copy()\n",
    "print(backup)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 310,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'CPP', 'C', 'JAVA', 'PYTHON'}\n"
     ]
    }
   ],
   "source": [
    "proglangs.discard(\"R\")\n",
    "print(proglangs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 311,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'R'}\n"
     ]
    }
   ],
   "source": [
    "b1 = backup.difference(proglangs)\n",
    "print(b1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 312,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'CPP', 'C', 'JAVA', 'PYTHON'}\n"
     ]
    }
   ],
   "source": [
    "b2 = {\"R\"}\n",
    "proglangs.difference_update(b2)\n",
    "print(proglangs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 313,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'JAVA'}\n"
     ]
    }
   ],
   "source": [
    "b3 = {\"JAVA\"}\n",
    "b4 = backup.intersection(b3)\n",
    "print(b4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 314,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'JAVA'}\n"
     ]
    }
   ],
   "source": [
    "backup.intersection_update(b3)\n",
    "print(backup)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 315,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 315,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "proglangs.isdisjoint(backup)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 316,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 316,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "backup.issubset(proglangs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 317,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 317,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "backup.issuperset(proglangs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 318,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'C', 'JAVA', 'PYTHON'}\n"
     ]
    }
   ],
   "source": [
    "proglangs.pop()\n",
    "print(proglangs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 319,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'C', 'PYTHON'}\n"
     ]
    }
   ],
   "source": [
    "proglangs.remove(\"JAVA\")\n",
    "print(proglangs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 320,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'JAVA'}\n",
      "{'C', 'PYTHON'}\n",
      "{'JAVA', 'PYTHON', 'C'}\n"
     ]
    }
   ],
   "source": [
    "print(backup)\n",
    "print(proglangs)\n",
    "b5 = proglangs.symmetric_difference(backup)\n",
    "print(b5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 321,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'C', 'JAVA', 'PYTHON'}\n",
      "{'JAVA'}\n"
     ]
    }
   ],
   "source": [
    "proglangs.symmetric_difference_update(backup)\n",
    "print(proglangs)\n",
    "print(backup)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 322,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'JAVA', 'R', 'PYTHON', 'C'}\n"
     ]
    }
   ],
   "source": [
    "b6 = proglangs.union(b2)\n",
    "print(b6)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 324,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'C', 'R', 'JAVA', 'PYTHON'}\n"
     ]
    }
   ],
   "source": [
    "proglangs.update(b6)\n",
    "print(proglangs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 325,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "set()\n"
     ]
    }
   ],
   "source": [
    "proglangs.clear()\n",
    "print(proglangs)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "7) Tuples"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 326,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('Integers', 'float', 'Strings', 'Lists', 'Dictionary', 'Sets', 'Tuples', 'Boolean')\n"
     ]
    }
   ],
   "source": [
    "datatypes = (\"Integers\",\"float\",\"Strings\",\"Lists\",\"Dictionary\",\"Sets\",\"Tuples\",\"Boolean\")\n",
    "print(datatypes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 328,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 328,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "datatypes.count(\"Integers\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 329,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n"
     ]
    }
   ],
   "source": [
    "x = datatypes.index(\"Dictionary\")\n",
    "print(x)"
   ]
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
