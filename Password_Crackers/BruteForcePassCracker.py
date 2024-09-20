import hashlib
import itertools

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def brute_force(target_hash, max_length, charset):
    for length in range(1, max_length + 1):
        for combination in itertools.product(charset, repeat=length):
            password = ''.join(combination)
            hashed_password = hash_password(password)
            if hashed_password == target_hash:
                return password
    return None

if __name__ == "__main__":
    target_hash = input("Enter the target hash to crack: ")
    max_length = int(input("Enter the maximum length of the password: "))
    custom_charset = input("Enter a custom character set or press Enter to use the default character set: ")

    if not custom_charset:
        charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-=_+[]{}|;:'\",.<>/?"
    else:
        charset = custom_charset

    print(f"Using Brute Force Attack with a maximum password length of {max_length} and character set: {charset}")

    cracked_password = brute_force(target_hash, max_length, charset)

    if cracked_password:
        print(f"Password Cracked! The password is: {cracked_password}")
    else:
        print("Password not found.")
