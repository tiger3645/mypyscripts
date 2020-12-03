import requests
import hashlib
import sys


def request_api_data(query_char):
    '''
    Requests all the cracked passwords given the five starting characters of a SHA1 hash.

    Arguments:
    query_char -- first five characters of our SHA1 hashed password.

    Returns:
    data -- list containing all cracked hashes starting with query_char.
    '''
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f'Error fetching: {res.status_code}.\nCheck the API and try again.')
    return res


def pwned_api_check(password):
    '''
    Checks whether a password has been cracked.

    Arguments:
    password -- the password we are checking.

    Returns:
    pwned -- boolean value indicating whether the given password has been cracked or not.
    '''
    hashed_password = hashlib.sha1(password.encode('utf-8'))
    hashed_password = hashed_password.hexdigest().upper()
    first5_char, tail = hashed_password[:5], hashed_password[5:]
    response = request_api_data(first5_char)
    response = (line.split(':') for line in response.text.splitlines())
    for h, count in response:
        if h == tail:
            return count
    return 0


def main(password_list):
    for password in password_list:
        count = pwned_api_check(password)
        if count:
            print(
                f'{password} was found {count} times. Looks like you need to change that password.')
        else:
            print(
                f'{password} was not found. Go ahead!')
    return 'Done!'


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
