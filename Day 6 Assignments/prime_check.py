% % writefile
prime.py


def prime_check(num):
    prime_number = True

    if (num == 1 or num == 2):
        print(prime_number)

    else:
        for i in range(2, num):
            if (num % i) == 0:
                prime_number = False
                print(prime_number)
                break

            else:
                print(prime_number)
                break

% % writefile
test_prime.py

import unittest
import prime


class Testprime_check(unittest.TestCase):
    def test_num(self):
        num = 4
        result = prime.prime_check(num)
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()

!python
test_prime.py