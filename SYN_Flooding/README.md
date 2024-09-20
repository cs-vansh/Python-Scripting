# SYN_Flooding

__Note: Please use this script responsibly and only in authorized testing scenarios. Unauthorized use may result in serious consequences.__

This script demonstrates a simple SYN flood attack using Scapy, a Python library for crafting and sending network packets. It takes advantage of the way the three-way handshake occurs:

- __SYN (Synchronize):__ The client initiates a connection by sending a SYN packet to the server. This packet contains the initial sequence number for the connection.

- __SYN-ACK (Synchronize-Acknowledge):__ Upon receiving the SYN packet, the server responds with a SYN-ACK packet. In this packet:

  - The server acknowledges the receipt of the SYN packet.
  - The server allocates resources for the connection.
  - The server opens a port for the communication to take place.

- __ACK (Acknowledge):__ Finally, the client sends an ACK packet to the server, confirming the receipt of the SYN-ACK packet. This ACK packet also acknowledges the server's allocated resources and the opened port.

![1642843418224_2cDnqtQfqo_threeway](https://github.com/cs-vansh/SYN_Flooding/assets/104628209/28e97729-482c-431f-8abf-69b7231ac440)

A __SYN flooding attack__ involves overwhelming a target server with a large number of SYN packets, exploiting the server's resources and potentially causing a __Denial of Service(DOS)__. 


## Usage

1. Install the required dependencies using:

```bash
    pip install scapy
```

2. Update the script with the appropriate values for the source and target IP addresses.

```python
    src = 'yyy.yyy.yyy.yyy'  # Replace with the source IPv4 address 
    trgt = 'zzz.zzz.zzz.zzz'  # Replace with the target IPv4 address 
```


