import subprocess
import hashlib

def run(user_input):
    # Intentionally vulnerable: shell injection
    subprocess.call("echo " + user_input, shell=True)

def hash_password(pw):
    # Intentionally weak hashing
    return hashlib.md5(pw.encode()).hexdigest()
# trigger scan
#live demo
