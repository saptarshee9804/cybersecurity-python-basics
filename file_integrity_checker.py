
import hashlib
from pathlib import Path


def calculate_sha256(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


def main():
    file_path = input("Enter the path of the file to check: ")
    path = Path(file_path)

    if not path.is_file():
        print("Error: File not found.")
        return

    file_hash = calculate_sha256(path)

    print("\nFile:", path.name)
    print("SHA-256:", file_hash)
    print("Integrity fingerprint calculated successfully.")


if __name__ == "__main__":
    main()
