
# Author: Michael Olimpo

## Summary:
Client.py: Embeds sys info into a carrier picture(in this case it's a jpg) and 
forwards the data to a particular IP PORT
```Python
exec: python Client.py <Server IP> <Server Port>
```
Server.py: Receives data from client.py and displays the embedded message. It can also act as a message forwarder
```Python
exec: python Server.py <Server Port to listen to>
```
## Requirements:
    1. Python 2.7
    2. Windows 10

## NOT TESTED ON:
    1. Python 3
    2. Linux/Unix
    3. OSX
---

### The software comprises 4 components
    1. Client.py # The client
    2. Server.py # The server
    3. GetInfo.py # Grabs the system info
    4. ImageMessenger.py # Embeds the message

Design:

    The implementation was to embed the message at the end of the JPG.
    Algo:
        1. Get length of carrier image.
        2. Embed message at end of image. (this does not disrupt the structure of the image and image application can still open it just fine.)
        3. Send JSON object with 2 Keys. 1 containing Embed Image data, 2 Length of original image.
        4. Server will receive this JSON object, and extract the message from the start offset of the Length of the original image, to the end of the modified image.

