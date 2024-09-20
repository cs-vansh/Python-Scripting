import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
from tkinter import filedialog
import hashlib
import requests

def on_drop(event):
    global file_path
    file_path = event.data
    print("File dropped:", file_path)
    drop_area.delete(1.0, tk.END)
    drop_area.insert(tk.END, file_path + "\n")

def browse_files():
    global file_path
    file_path = filedialog.askopenfilename()
    if file_path:
        print("Selected file:", file_path)
        drop_area.delete(1.0, tk.END)
        drop_area.insert(tk.END, file_path + "\n")

def scan_file():
    global file_path
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        # Read the file in chunks to handle large files efficiently
        chunk_size = 4096
        while chunk := f.read(chunk_size):
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()

def query_malware(hash_value):
    api_url = "https://mb-api.abuse.ch/api/v1/"

    params = {
        "query": "get_info",
        "hash": hash_value
    }

    response = requests.post(api_url, data=params)

    if response.status_code == 200:   #request successful
        data = response.json()

        if data['query_status'] == 'hash_not_found':
            label_result.config(text="This is Not Malware.", fg="green")
        elif data['query_status'] == 'sha256_hash':
            if 'malware' in data['tags']:  # Check if 'malware' tag is present
                label_result.config(text="Alert! This is a Malware.", fg="red")
            else:
                label_result.config(text="Be cautious! This could be a Malware.", fg="orange")
        else:
            label_result.config(text="Unexpected response from MalwareBazaar API.", fg="blue")

def scan_and_update_label():
    global file_path
    hash_value = scan_file()
    label_hash.config(text="SHA256 Hash: " + hash_value)
    query_malware(hash_value)

root = TkinterDnD.Tk()
root.title("Malware Detector")

# drop area for drag and drop file upload
drop_area = tk.Text(root, height=10, width=50)
drop_area.pack(pady=10)

#drag and drop logic
drop_area.drop_target_register(DND_FILES) 
drop_area.dnd_bind('<<Drop>>', on_drop)

browse_button = tk.Button(root, text="Browse Files", command=browse_files)
browse_button.pack()

scan_button = tk.Button(root, text="Scan", command=scan_and_update_label)
scan_button.pack()

label_hash = tk.Label(root, text="") #SHA256 hash value
label_hash.pack()

label_result = tk.Label(root, text="") #for malware results
label_result.pack()

root.mainloop()
