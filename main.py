# This is program for creating passwords
# sys could be used alternatively instead of argparse
# to receive cmd variables

# import sys
import string
import random
import argparse


def create_password(length=8, upper=False, lower=False,
                    digits=False, pun=False):
    """
    This is a brilliant password creator enjoy it then!

    :param length: length of the password
    :param upper: determines if password has uppercase letters
    :param lower: determines if password has lowercase letters
    :param digits: determines if password has digits in it
    :param pun: determines if password has punctuations in it
    :return: In case inputs are correctly set, it makes a password

    """

    pool = ''
    if lower:
        pool += string.ascii_lowercase
    if upper:
        pool += string.ascii_uppercase
    if digits:
        pool += string.digits
    if pun:
        pool += string.punctuation
    if pool == '':
        print('Criteria is not met')
        return
    password = random.choices(pool, k=length)
    password = ''.join(password)

    print('Your password is %str ' % password)


if __name__ == '__main__':
    # parse user data from command line
    parser = argparse.ArgumentParser(description='Creating password is easy',
                                     epilog='How was that!')
    parser.add_argument('-q', '--length', type=int, help='length of password')
    parser.add_argument('-u', '--upper', help='uppercase letters',
                        action='store_true')
    parser.add_argument('-l', '--lower', help='lowercase letters',
                        action='store_true')
    parser.add_argument('-d', '--digits', help='digits are in!',
                        action='store_true')
    parser.add_argument('-p', '--pun', help='punctuations are in',
                        action='store_true')

    args = parser.parse_args()
    # print(args)

    # create password
    create_password(length=args.length, upper=args.upper, lower=args.lower,
                    digits=args.digits, pun=args.pun)
