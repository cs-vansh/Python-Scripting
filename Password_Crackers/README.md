# Password_Cracker

## Dictionary Password Cracker

This Python script allows you to perform a dictionary-based password attack using the SHA-256 algorithm. It reads a dictionary file, hashes each word, and compares the hashed values with a target hash to find the password.

## Usage
1. Run the script: `DictionaryPassCracker.py`
2. Enter the target hash you want to crack and the path to the dictionary file.
3. The script will read a dictionary file and attempt to find a matching password.
4. If a password is found, it will be displayed; else, a message will indicate that the password is not in the dictionary.

----------

## Brute Force Password Cracker

This Python script demonstrates a brute-force attack to crack a password hash using the SHA-256 algorithm. The code includes a function for hashing passwords and another for performing the brute-force attack.

## Usage
1. Run the script: `BruteForcePassCracker.py`
2. Enter the target hash you want to crack.
3. Specify the maximum length of the password for the brute-force attack.
4. Optionally, provide a custom character set, or press Enter to use the default character set.
5. If the password is found, it is displayed; else, "Password not found" is returned.
