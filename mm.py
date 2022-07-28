from padding_oracle import PaddingOracle
from optimized_alphabets import json_alphabet

import requests


def oracle(cipher_hex):
    headers = {'Cookie': 'vals={}'.format(cipher_hex)}
    r = requests.get('https://web.ctf.devclub.in/web/6/', headers=headers)
    response = r.content

    if b'Invalid padding bytes.' not in response:
        return True
    else:
        return False


o = PaddingOracle(oracle, max_retries=-1)

cipher = 'fe62409edff143b113fa9e8cead4cc27338191a51eeeac94e197179eb8adbfb8596f996d6eddca93c059e3dc35f7bef36b57a5611250ec4528c11e1573799d2178c54c034b9ea8fda8ae9a4a41c67763'
plain, _ = o.decrypt(cipher, optimized_alphabet=json_alphabet())
print('Plaintext: {}'.format(plain))