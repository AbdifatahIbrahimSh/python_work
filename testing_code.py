"""test the fucntions """

import unittest
from tested import get_formated_name

# loop through and print each time a neatly formated name 
# while True:
#     first = input("What is your first name: ")
#     if first == 'q':
#         break
#     last = input("What is your last name: ")
#     if last == 'q':
#         break

#     full_name = get_formated_name(first, last)
#     print(f"\tNeatly formated name: {full_name}\n")


# creates a class of of tests 
class NamesTestCase(unittest.TestCase):
    """Test for tested.py functions"""

    def test_first_last_name(self):
        """Do names like Samia Mukhtar works"""

        formated_name = get_formated_name('samia', 'mukhtar', 'abdirahman')
        self.assertEqual(formated_name, 'Samia Abdirahman Mukhtar')


if __name__ == '__main__':
    unittest.main()
