#!/usr/bin/python3
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

import argparse
import lucas

import mpmath


def bradify():
    """Iteratively calculates the ratios of Lucas sequence numbers.

    Spoiler: It approaches the golden ratio.
    """
    argument_parser = argparse.ArgumentParser(
        description='Watch the ratios of numbers in a Lucas series approach '
                    'the golden ratio (φ).')
    argument_parser.add_argument('-i', '--iterations',
                                 help='Maximum number of iterations.',
                                 type=int, default=1000)
    argument_parser.add_argument('-p', '--precision',
                                 help='Digits of precision to calculate',
                                 type=int, default=100)
    sequences = argument_parser.add_mutually_exclusive_group(required=True)
    sequences.add_argument('-f', '--fibonacci', dest='special_case',
                           action='store_const', const='f',
                           help='The Fibonacci numbers')
    sequences.add_argument('-l', '--lucas', dest='special_case',
                           action='store_const', const='l',
                           help='The Lucas numbers')
    sequences.add_argument('-b', '--brady', dest='special_case',
                           action='store_const', const='b',
                           help='The Brady numbers')
    sequences.add_argument('-a',
                           type=str, dest='sequence_definition',
                           help='A generic sequence')
    args = argument_parser.parse_args()

    if args.special_case:
        if args.special_case == 'f':
            sequence = lucas.fibo()
        elif args.special_case == 'l':
            sequence = lucas.lucas_num()
        elif args.special_case == 'b':
            sequence = lucas.brady()
    else:
        definition = args.sequence_definition.split(',')
        definition[0] = int(definition[0])
        definition[1] = int(definition[1])
        sequence = lucas.Lucas(definition, 5)

    mpmath.mp.dps = args.precision * 2
    previous = mpmath.mpf(sequence[0])
    oldphi=1000
    for i in range(1, args.iterations):
        current = mpmath.mpf(sequence[i])
        try:
            phi = current/previous
        except ZeroDivisionError:
            phi = float('NaN')
        print('φ[%d] = %s' % (i, mpmath.nstr(phi, args.precision)))
        if abs(oldphi - phi) < 10**(-args.precision) and i > 2:
            break
        previous = current
        oldphi = phi



if __name__ == '__main__':
    bradify()
