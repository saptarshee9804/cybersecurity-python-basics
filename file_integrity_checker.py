
import hashlib
import json
from pathlib import Path


def calculate_sha256(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


def main():
    file_name = input("Enter the file path: ").strip()
    path = Path(file_name)

    if not path.is_file():
        print("Error: File not found.")
        return

    current_hash = calculate_sha256(path)
    record_path = Path(str(path) + ".hash.json")

    if not record_path.exists():
        record = {
            "filename": path.name,
            "sha256": current_hash
        }

        record_path.write_text(
            json.dumps(record, indent=4),
            encoding="utf-8"
        )

        print("Original hash saved:", record_path)
        print("SHA-256:", current_hash)
        print("Keep this record safe for future checks.")

    else:
        record = json.loads(
            record_path.read_text(encoding="utf-8")
        )

        if current_hash == record["sha256"]:
            print("INTEGRITY VERIFIED: File has not changed.")
        else:
            print("WARNING: File contents have changed!")

        print("Current SHA-256:", current_hash)
        print("Recorded SHA-256:", record["sha256"])


if __name__ == "__main__":
    main()
