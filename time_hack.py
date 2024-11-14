import time
from random import randint, seed
from hashlib import sha256
from Crypto.Cipher import AES
from tqdm import tqdm

n = int("72741423208033405403492275698762968936514657314823442485453559870105200118330405900858299998747406127848670334407387228444029070060538220448699667905891284937839901536444798774307744865631349770845980738192442639071823803272283670943732769371979418893953521892212745135191661138195973757608889180051128601323", 10) 
e = 0x10001
c = int("4da0230d2b8b46e3a7065f32c46df019739cc002a208cc37767a82c3e94edfc3440fa4b24a32274e35d5ddceaa33505c4f2a57281c3a5d6d4db3a0dbdbb30dbf373241319ce4a7fdd1780b6bafc86e37d283c9f9787c567434e2fc29c988fb05fd411fe4453ea40eb45fc41a423839b485e238dd2530fba284e9b07a0bba6546", 16)
enc_secret = bytes.fromhex("ce8f36aa844ab00319bcd4f86460a10d77492c060b2c2a91615f4cd1f2d0702e76b68f1ec0f11d15704ba52c5dacc60018d5ed87368464acd030ce6230efdbff7b18cba72ccaa9455a6fe6021b908dd1")

start_timestamp = 1704931200
seconds_in_a_day = 86400
days_to_try = 14 

def check_seed(start_time, end_time, n, c, enc_secret, e):
    for t in tqdm(range(start_time, end_time), desc="Checking seeds"):
        seed(t)
        key1 = randint(1 << 20, 1 << 21)
        key2 = randint(1 << 20, 1 << 21)
        k = key1 * key2
        
        c_candidate = pow(k, e, n)

        if c_candidate == c:
            print(f"Debug: Correct seed found! Seed: {t}, key1: {key1}, key2: {key2}")
            aes_key = sha256(str(k).encode()).digest()
            cipher = AES.new(aes_key, AES.MODE_ECB)
            flag = cipher.decrypt(enc_secret)
            return t, flag
    return None

# Test seeds for 5 days starting from January 11th
for day_offset in range(-days_to_try, days_to_try + 1):
    start_time = start_timestamp + day_offset * seconds_in_a_day
    end_time = start_time + seconds_in_a_day
    print(f"Testing day offset: {day_offset}, from {start_time} to {end_time}")

    result = check_seed(start_time, end_time, n, c, enc_secret, e)
    if result:
        print(f"Found seed: {result[0]}")
        print(f"Recovered flag: {result[1]}")
        break