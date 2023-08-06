import os

from .Kuznechik import Kuznechik

KEY_PATH = 'keys'

if not os.path.exists(os.path.join(KEY_PATH, 'key')):
    key = Kuznechik.generate_key()
else:
    with open(os.path.join(KEY_PATH, 'key'), 'rb') as file:
        key = file.read()

cryptographer = Kuznechik(key)
encrypted_data = cryptographer.encrypt('Петров Петр Петрович 4512 231123 ул. Пушкина д. Колотушкина')
print(encrypted_data)
decripted_data = cryptographer.decrypt(encrypted_data)
print(decripted_data)