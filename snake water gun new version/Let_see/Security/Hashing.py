import hashlib

def Hashing(passwd):
        
    # create a new MD5 hash object
    md5_hash = hashlib.md5()

    # update the hash object with the message
    md5_hash.update(passwd.encode())

    # get the hexadecimal representation of the hash digest
    hash_digest = md5_hash.hexdigest()
    
    return hash_digest
