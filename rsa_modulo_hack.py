from Crypto.Util.number import inverse
from hashlib import sha256
from Crypto.Cipher import AES
from tqdm import trange, tqdm

n = 72741423208033405403492275698762968936514657314823442485453559870105200118330405900858299998747406127848670334407387228444029070060538220448699667905891284937839901536444798774307744865631349770845980738192442639071823803272283670943732769371979418893953521892212745135191661138195973757608889180051128601323
e = 65537

rsa_encrypted_key = int('4da0230d2b8b46e3a7065f32c46df019739cc002a208cc37767a82c3e94edfc3440fa4b24a32274e35d5ddceaa33505c4f2a57281c3a5d6d4db3a0dbdbb30dbf373241319ce4a7fdd1780b6bafc86e37d283c9f9787c567434e2fc29c988fb05fd411fe4453ea40eb45fc41a423839b485e238dd2530fba284e9b07a0bba6546', 16)
aes_encrypted_message = bytes.fromhex('ce8f36aa844ab00319bcd4f86460a10d77492c060b2c2a91615f4cd1f2d0702e76b68f1ec0f11d15704ba52c5dacc60018d5ed87368464acd030ce6230efdbff7b18cba72ccaa9455a6fe6021b908dd1')

# Decrypt via AES
def decrypt_aes(aes_key_int, ciphertext):
    aes_key = sha256(str(aes_key_int).encode()).digest()
    cipher = AES.new(aes_key, AES.MODE_ECB)
    decrypted_message = cipher.decrypt(ciphertext)
    return decrypted_message

# Encrypt via RSA
def rsa_encrypt(value):
    return pow(value, e, n)

rsa_encrypted_values = set()
value_dict = {}

# Generate possible values of RSA encryption for the range 2**20 to 2**21 + 1
for i in trange(2**20, 2**21 + 1, desc="Generating RSA-Encrypted Values"):
    encrypted_value = rsa_encrypt(i)
    rsa_encrypted_values.add(encrypted_value)

    # Add key: encrypted value
    # Add value: integer
    value_dict[encrypted_value] = i

key1, key2 = 0, 0
for factor1 in tqdm(rsa_encrypted_values, desc="Searching for Factors"):
    factor2 = (rsa_encrypted_key * inverse(factor1, n)) % n

    # Does a match exist?
    if factor2 in rsa_encrypted_values:
        key1 = value_dict[factor1]
        key2 = value_dict[factor2]
        print(f"Factors found! key1 = {key1}, key2 = {key2}")
        break

if key1 and key2:
    aes_key = key1 * key2
    decrypted_message = decrypt_aes(aes_key, aes_encrypted_message)
    print("Decrypted Message:", decrypted_message)
else:
    print("No valid factors found.")
