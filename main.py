import hashlib
import json

filename = 'README.md'

def write_validation_result(filename, text, provided_sha256, calculated_sha256, sha256_match, provided_md5, calculated_md5, md5_match):
    header = (
        "| String | Provided SHA256 | Calculated SHA256 | SHA256 Match | Provided MD5 | Calculated MD5 | MD5 Match |\n"
        "|--------|-----------------|-------------------|--------------|--------------|----------------|-----------|\n"
    )
    # Check if file exists and is empty or not
    try:
        with open(filename, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        content = ''
    with open(filename, 'a') as f:
        if not content:
            f.write(header)
        f.write(
            f'| "{text}" | {provided_sha256} | {calculated_sha256} | {sha256_match} | {provided_md5} | {calculated_md5} | {md5_match} |\n'
        )

with open('items.json', 'r') as f:
    data = json.load(f)

def validate_and_write_results(data, filename):
    for item in data:
        text = item['string']
        provided_sha256 = item.get('SHA256', '')
        provided_md5 = item.get('MD5', '')
        calculated_sha256 = hashlib.sha256(text.encode('utf-8')).hexdigest()
        calculated_md5 = hashlib.md5(text.encode('utf-8')).hexdigest()
        sha256_match = provided_sha256 == calculated_sha256
        md5_match = provided_md5 == calculated_md5
        write_validation_result(
            filename,
            text,
            provided_sha256,
            calculated_sha256,
            sha256_match,
            provided_md5,
            calculated_md5,
            md5_match
        )

def main():
    validate_and_write_results(data, filename)

if __name__ == "__main__":
    main()