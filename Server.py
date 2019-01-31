import SocketServer
import json
import base64
import sys
import Client #my own client.py

class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    print "#########  Server Started #########"
    def handle(self):
        buffer = ""
        print "Connection Accepted from " + self.client_address[0]
        # self.request is the TCP socket connected to the client
        print "receiving data.."
        while True:
            self.data = self.request.recv(1024).strip()
            if not self.data:
                break
            else:
                buffer+=self.data
        self.request.sendall(buffer)
        print "Completed"
        print "{} wrote:".format(self.client_address[0])
        Message = getMessage(buffer)
        if(len(sys.argv) == 2):
            print Message
        else:
            counter = 2
            while(counter < len(sys.argv)):
                print "Forwarding message to %s %s" % (sys.argv[counter],sys.argv[counter+1])
                forwardMessage(sys.argv[counter],int(sys.argv[counter+1]),buffer)
                counter+=2

def getMessage(Input):
    Input = json.loads(Input)
    f = open("received.jpg","wb")
    for k,v in Input.iteritems():
        if k == 'Image':
            oImageData = base64.b64decode(v)
            f.write(oImageData)
        if k == 'Length':
            Length = v
    return oImageData[Length:]


def forwardMessage(HOST,PORT,Message):
    try:
        Client.sendMessage(HOST,int(PORT),Message)
        print "Message sent"
    except:
        print "Failed to send to %s %s" %(HOST,PORT)
    return

if __name__ == "__main__":
    if(len(sys.argv) < 2):
        sys.exit("Please enter a PORT to listen to. e.g Server <Port>. By default, it is bound to localhost:<Port>")
    elif((len(sys.argv)-2)%2 != 0): #need to reduce length by 2, to exclude sys.argv[0] and sys.argv[1]
        sys.exit("Did not specify correct number of Port:IP pairs")

    # Create the server, binding to localhost on port
    server = SocketServer.TCPServer(("0.0.0.0", int(sys.argv[1])), MyTCPHandler)
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()