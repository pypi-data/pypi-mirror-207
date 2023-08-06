import os
from gostcrypto.gostcipher import GOST34122015Kuznechik

class Kuznechik:
    """
    Class for Kuznechik encoding
    
    :param key: 32byte key for encoding
    :type key: bytearray
    """
    def __init__(self, key: bytearray) -> None:
        self.key = key
        self.cipher_obj = GOST34122015Kuznechik(key)
        self.buffer_size = self.cipher_obj.block_size

    @staticmethod
    def _dump_key(key: bytearray, key_path: str = 'keys'):
        try:
            with open(os.path.join(key_path, 'key'), 'wb') as file:
                file.write(key)
        except FileNotFoundError:
            os.makedirs(key_path)
            Kuznechik._dump_key(key, key_path)

    @staticmethod
    def generate_key(key_path: str = 'keys') -> bytearray:
        """
        Generating key and key_file.
        
        :param key_path: path to folder for key_file
        :type key_path: str
        """
        key = os.urandom(32)
        Kuznechik._dump_key(key, key_path)
        return key

    def encrypt(self, data: str) -> str:
        """
        Encrypt data.
        
        :param data: data to encrypt
        :type data: str
        """
        data = data.encode()
        while 16 - (len(data) % 16) != 0 and 16 - (len(data) % 16) != 16:
            data += '0'.encode()
        encrypted_data = bytearray()
        for i in range(0, len(data), 16):
            encrypted_data += self.cipher_obj.encrypt(data[i:i+16])
        return encrypted_data.hex()

    def decrypt(self, data: str) -> str:
        """
        Decrypt data.
        
        :param data: data to encrypt
        :type data: str
        """
        encrypted_data = bytes.fromhex(data)
        decrypted_data = bytearray()
        for i in range(0, len(encrypted_data), 16):
            decrypted_data += self.cipher_obj.decrypt(encrypted_data[i:i+16])
        decrypted_data = list(decrypted_data.decode())
        i = len(decrypted_data) - 1
        while '0' in decrypted_data[i]:
            del decrypted_data[i]
            i -= 1
        return ''.join(decrypted_data)