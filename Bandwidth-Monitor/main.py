import time
import psutil
import tkinter as tk

def update_bandwidth():
    global last_received, last_sent, last_total

    try:
        interval = int(entry_interval.get()) * 1000
        if interval <= 0:
            interval = 1000  # default to 1 second if the input is non-positive
    except ValueError:
        interval = 1000  # default to 1 second if the input is invalid


    bytes_received = psutil.net_io_counters().bytes_recv
    bytes_sent = psutil.net_io_counters().bytes_sent

    bytes_total = bytes_received + bytes_sent

    new_received = bytes_received - last_received
    new_sent = bytes_sent - last_sent
    new_total = bytes_total - last_total

    mb_new_received = new_received / 1024 / 1024
    mb_new_sent = new_sent / 1024 / 1024
    mb_new_total = new_total / 1024 / 1024

    label_received.config(text=f"Received: {mb_new_received:.3f} MB")
    label_sent.config(text=f"Sent: {mb_new_sent:.3f} MB")
    label_total.config(text=f"Total: {mb_new_total:.3f} MB")

    last_received = bytes_received
    last_sent = bytes_sent
    last_total = bytes_total

    root.after(interval, update_bandwidth)
    
def bring_to_top():
    root.lift()
    root.after(1000, bring_to_top)

last_received = psutil.net_io_counters().bytes_recv
last_sent = psutil.net_io_counters().bytes_sent
last_total = last_received + last_sent

root = tk.Tk()
root.title("Bandwidth Monitor")

# Making the window always on top
root.attributes('-topmost', True)

# window transparency
root.attributes('-alpha', 0.8)

label_received = tk.Label(root, text="Received: 0 MB", font=("Helvetica", 14))
label_received.pack()

label_sent = tk.Label(root, text="Sent: 0 MB", font=("Helvetica", 14))
label_sent.pack()

label_total = tk.Label(root, text="Total: 0 MB", font=("Helvetica", 14))
label_total.pack()

# Frame for update interval label and entry
frame_interval = tk.Frame(root)
frame_interval.pack(pady=5)

interval_label = tk.Label(frame_interval, text="Update Interval (seconds):", font=("Helvetica", 12))
interval_label.pack(side=tk.LEFT, padx=5)
entry_interval = tk.Entry(frame_interval, width=5)
entry_interval.insert(0, "1")  # default value
entry_interval.pack(side=tk.LEFT, padx=5)


update_bandwidth()

bring_to_top()

root.mainloop()
