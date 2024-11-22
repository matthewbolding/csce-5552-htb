# CSCE 5552 Cybersecurity Essentials
## Hack the Box Project

This reposity contains the code we used to hack the box.

To use the repostory, create a virtual environment, activate it, install the dependencies, and run whichever method you see fit.

```bash
$ python3 -m venv .htb
$ source source .htb/bin/activat
$ pip install -r requirements.txt
```

### Repository Contents
The only files from the Hack the Box project is in the `htb` folder. The `htb/secret.py` file is added so that errors do not arise, and the `flag` variable should be filled in to the secret. The secret is intentionally not posted to preserve the box's challenge.

Other files include:
- `time_hack.py`: an attempt to hack the box by seeding the `randint` various UNIX-epoch times stamps in an attempt to regenerate the two keys based on the time of file creation.
- `brute_force_hack.py`: iterates through all possible key pairs, RSA encrypts the product of the two keys, and compares this cipher text to the given cipher text.
- `rsa_modulo_hack.py`: exploits the unpadded nature and homogeneity properties of RSA encryption via modular arithmetic to obtain the key pair.

### Group Members
Matthew Bolding, Don Daubert, Ty Richardson

