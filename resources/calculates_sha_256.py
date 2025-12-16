import hashlib
import sys

def sha256_file(filepath):
    hash_sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()

filepath = "datasets/C3/pn_generated_distribution_KDE.parquet"
print(sha256_file(filepath))