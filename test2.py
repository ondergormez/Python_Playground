# TODO: Add shebang
from ecdsa import VerifyingKey
from ecdsa import SECP256k1

with open("privateKey.pem") as private_key_file:
    private_key = VerifyingKey.from_pem(private_key_file.read())

print(private_key)

SigningKey.from_pem()

vk = sk.verifying_key
signature = sk.sign(b"message")
assert vk.verify(signature, b"message")
