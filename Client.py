import socket
import ImageMessenger
import json
import base64
import sys
import re

def sendMessage(HOST,PORT,toSend = None):
    if not toSend:
        #initdata, encode all to base64
        DatatoSend = ImageMessenger.sStartProcess()
        toSend = {}
        toSend['Image'] = base64.b64encode(DatatoSend[0])
        toSend['Length'] = DatatoSend[1]
        toSend = json.dumps(toSend)

    # Create a socket (SOCK_STREAM means a TCP socket)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        received = ""
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(toSend + "\n")
        sock.shutdown(socket.SHUT_WR)
        while True:
            incdata = sock.recv(1024)
            received+=incdata
            if not incdata:
                print "Completed"
                break
    finally:
        sock.close()

if __name__ == '__main__':
    if(len(sys.argv) < 2):
        sys.exit("Please enter IP and PORT address to connect to. e.g Client <IP> <PORT>, excluding brackets")
    else:
        #check and make sure IP first then Port
        toBeChecked = re.match(r"\d+\.\d+\.\d+.\d+",sys.argv[1])
        if not toBeChecked:
            sys.exit("Format Error. IP address should be in the form of 123.456.789.123")
        #check and make sure port is proper
        toBeChecked = re.match(r"^[0-9]+$",sys.argv[2])
        if not toBeChecked:
            sys.exit("Format Error. Port should be an integer. e.g 123456")
        sendMessage(sys.argv[1],int(sys.argv[2]))

