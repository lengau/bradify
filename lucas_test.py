#!/usr/bin/env python3
#
# Copyright 2014 Alex Lowe <email>
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# 
#

import unittest
from unittest import mock
from lucas import Lucas

BRADY_NUMBERS = [2308, 4261, 6569, 10830, 17399, 28229, 45628, 73857, 119485,
                 193342, 312827, 506169, 818996, 1325165, 2144161, 3469326,
                 5613487, 9082813, 14696300, 23779113, 38475413, 62254526,
                 100729939, 162984465, 263714404, 426698869, 690413273,
                 1117112142, 1807525415, 2924637557, 4732162972, 7656800529]

FIBONACCI_NUMBERS = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377,
                     610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657,
                     46368, 75025, 121393, 196418, 317811, 514229, 832040,
                     1346269, 2178309, 3524578, 5702887, 9227465, 14930352,
                     24157817, 39088169]

LUCAS_NUMBERS = [2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, 322, 521, 843,
                 1364, 2207, 3571, 5778, 9349, 15127, 24476, 39603, 64079,
                 103682, 167761, 271443, 439204, 710647, 1149851, 1860498,
                 3010349, 4870847, 7881196, 12752043, 20633239, 33385282]


class testCalculateFromBaseGivesCorrectResult(unittest.TestCase):
    def setUp(self):
        # Called before the first testfunction is executed
        pass

    def tearDown(self):
        # Called after the last testfunction was executed
        pass

    def test_brady_numbers(self):
        for starting_point in range(len(BRADY_NUMBERS)-2):
            for number in range(starting_point, len(BRADY_NUMBERS)-1):
                self.assertEqual(
                    BRADY_NUMBERS[number:number+2],
                    Lucas._calculate_from_base(
                        BRADY_NUMBERS[starting_point:starting_point + 2],
                        number - starting_point))

    def test_fibonacci_numbers(self):
        for starting_point in range(len(FIBONACCI_NUMBERS)-2):
            for number in range(starting_point, len(FIBONACCI_NUMBERS)-1):
                self.assertEqual(
                    FIBONACCI_NUMBERS[number:number+2],
                    Lucas._calculate_from_base(
                        FIBONACCI_NUMBERS[starting_point:starting_point + 2],
                        number - starting_point))

    def test_lucas_numbers(self):
        for starting_point in range(len(LUCAS_NUMBERS)-2):
            for number in range(starting_point, len(LUCAS_NUMBERS)-1):
                self.assertEqual(
                    LUCAS_NUMBERS[number:number+2],
                    Lucas._calculate_from_base(
                        LUCAS_NUMBERS[starting_point:starting_point + 2],
                        number - starting_point))


class testGeneratePair(unittest.TestCase):
    def setUp(self):
        # Called before the first testfunction is executed
        pass

    def tearDown(self):
        # Called after the last testfunction was executed
        pass

    @mock.patch('lucas.Lucas._calculate_from_base')
    def test_no_use_lookup(self, mock_calculator):
        sequence = Lucas([0,0], 10)
        sequence._generate_pair(15)
        mock_calculator.assert_called_once_with([0,0], 10)

    @mock.patch('lucas.Lucas._calculate_from_base')
    def test_use_lookup(self, mock_calculator):
        sequence = Lucas([0,0], 10)
        sequence._generate_pair(5)
        self.assertFalse(mock_calculator.called)

if __name__ == "__main__":
    unittest.main()
