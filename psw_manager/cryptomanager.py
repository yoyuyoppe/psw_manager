import secrets
import string

def encrypted(password: str) -> str:
    psw_to_list = list(password)
    crypto_pws = ''
    for i in range(len(psw_to_list)):
        curr_chr = psw_to_list[i]
        newChr = chr(ord(curr_chr) + (i+1))
        crypto_pws += newChr

    return crypto_pws


def decrypted(password: str) -> str:
    psw_to_list = list(password)
    crypto_pws = ''
    for i in range(len(psw_to_list)):
        curr_chr = psw_to_list[i]
        newChr = chr(ord(curr_chr) - (i+1))
        crypto_pws += newChr

    return crypto_pws


def generate_password():
	alphabet = string.ascii_letters + string.digits + string.punctuation
	password = ''.join(secrets.choice(alphabet) for i in range(8))
	return password