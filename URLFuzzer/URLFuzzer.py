import requests

base_url = input("Enter the base URL (example: https://www.google.com/): ").rstrip('/')
wordlist_path = input("Enter the wordlist file path (Provide absolute path): ").strip()
extensions_input = input("Enter file extensions to try (comma-separated, e.g., .php,.html), or leave blank for none: ").strip()

extensions = []
if extensions_input:
    for ext in extensions_input.split(','):
        ext = ext.strip()
        if ext:
            extensions.append(ext)


success_paths = []

try:
    with open(wordlist_path, 'r') as f:
        for line in f:
            base_path = line.strip()
            if not base_path:  # Stop at first empty line
                break

            paths_to_test = [base_path] 
            if extensions: 
                paths_to_test += [base_path + ext for ext in extensions]

            for path in paths_to_test:
                url = base_url + '/' + path.lstrip('/')
                try:
                    response = requests.get(url)
                    print(f"/{path} - Status code: {response.status_code}")
                    if response.status_code == 200:
                        success_paths.append(path)
                except requests.RequestException as e:
                    print(f"Error requesting {url}: {e}")

except FileNotFoundError:
    print(f"File not found: {wordlist_path}")
    exit()

print("---------------------------------------------------------------")
if success_paths:
    print("\nURLs with 200 status code:")
    for path in success_paths:
        print(f"/{path}")
else:
    print("No URLs with 200 status code found.")
print("---------------------------------------------------------------")
