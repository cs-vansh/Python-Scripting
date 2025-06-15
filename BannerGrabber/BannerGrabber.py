import socket

ip = input("Enter target IP address: ")
port = int(input("Enter target port: "))

# socket.AF_INET = socket family (IPv4 here), socket.SOCK_STREAM = socket type (TCP here)
# socket.AF_INET6 is for IPv6; socket.SOCK_DGRAM is for UDP
socket_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # connect to the target host by passing in the tuple containing ip and port to the socket object
    socket_object.connect((ip, port))

    # Send a minimal HTTP request
    socket_object.sendall(f"HEAD / HTTP/1.0\r\nHost: {ip}\r\n\r\n".encode())

    # receiving 2048 bytes of data, usually should be enough for the banner.
    response = socket_object.recv(2048).decode()


    socket_object.close()

    print("---------------------------------------------------------------")
    # Parse and print only the Server header (which usually contains the banner)
    for line in response.splitlines():
        if line.lower().startswith("server:"):
            print("Banner grabbed:", line)
            break
    else:
        print("No banner found. Printing the entire response.")
        print(response)

except Exception as e:
    print("Error:", e)