#
# Copyright 2014 Alex Lowe <lengau@gmail.com>
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

DEFAULT_STORAGE_MODULUS = 1000


def fibo(storage_modulus=DEFAULT_STORAGE_MODULUS):
    """Returns the Fibonacci numbers.

    Description: https://en.wikipedia.org/wiki/Fibonacci_number
    Sequence: https://oeis.org/A000045

    Args:
        storage_modulus: The storage modulus to be used.
    Returns:
        A Lucas object containing the Fibonacci sequence.
    """
    return Lucas([0, 1], storage_modulus)


def lucas_num(storage_modulus=DEFAULT_STORAGE_MODULUS):
    """Returns the Lucas numbers.

    Description: https://en.wikipedia.org/wiki/Lucas_number
    Sequence: https://oeis.org/A000032

    Args:
        storage_modulus: The storage modulus to be used.
    Returns:
        A Lucas object containing the Lucas numbers.
    """
    return Lucas([2, 1], storage_modulus)


def brady(storage_modulus=DEFAULT_STORAGE_MODULUS):
    """Returns the Brady numbers.

    Description: https://youtu.be/D8ntDpBm6Ok
    Sequence: https://oeis.org/A247698

    Args:
        storage_modulus: The storage modulus to be used.
    Returns:
        A Lucas object containing the Brady numbers.
    """
    return Lucas([2308, 4261], storage_modulus)


class Lucas(object):
    """Lucas sequences.

    Generates a Lucas sequence based on any two integers P and Q.
    More about Lucas sequences: https://en.wikipedia.org/wiki/Lucas_sequence
    Inspired by Numberphile: https://youtu.be/D8ntDpBm6Ok

        This class creates a somewhat list-like object for a Lucas sequence.
    The biggest difference from a user perspective is that a Lucas object is
    read-only. In order to modify the sequence being analysed, one must create
    a new Lucas object. It's worth noting that Lucas objects also only store
    every thousandth pair by default. This can be set at initialization by
    setting storage_modulus.
    """
    def __init__(self, initialization_vector, storage_modulus=1000):
        object.__init__(self)

        self._storage_modulus = storage_modulus if storage_modulus >= 2 else 2
        self._sequence = [initialization_vector]

    @classmethod
    def _calculate_from_base(cls, base, distance):
        """Generates a pair of items at a given distance from a base pair.

        e.g. If base contains the 100th and 101st items of the sequence and
        distance is 10, this function will return the 110th and 111th items.

        Args:
            base: A list containing the base items
            distance: A list containing the distance to calculate.
        """
        penultimate = base[0]
        ultimate = base[1]
        for _ in range(distance):
            next = ultimate + penultimate
            penultimate = ultimate
            ultimate = next
        return [penultimate, ultimate]

    def _generate_pair(self, key):
        """Generates a pair of items at the last storage point before key.

        Equivalent to:
        [self[int(key/self._storage_modulus) * self._storage_modulus],
         self[int(key/self._storage_modulus) * self._storage_modulus + 1]]

        For example, self._generate_pair(1999) will return the 1000th and
        1001st items in the sequence.

        Args:
            key: An integer containing the number to store sums to.
        Returns:
            The last storage pair before key.
        """
        expected_length = int(key/self._storage_modulus) + 1
        current_length = len(self._sequence)
        if current_length >= expected_length:
            return self._sequence[expected_length - 1]

        self._sequence.extend(
            [[None, None]] * (expected_length - current_length))
        for i in range(current_length, expected_length):
            self._sequence[i] = self._calculate_from_base(
                self._sequence[i-1], self._storage_modulus)
        return self._sequence[expected_length-1]

    def __getitem__(self, key):
        """Gets the (key)th item of the sequence.

        Args:
            key: Which item to retrieve
        Returns: The (key)th item of the sequence, zero-indexed.
        """
        stored_pair = self._generate_pair(key)
        distance = key % self._storage_modulus
        return self._calculate_from_base(stored_pair, distance)[0]
