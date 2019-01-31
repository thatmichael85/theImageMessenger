import GetInfo
import json
import struct

def OpenImage(input):
    oImage = open(input,"rb").read()
    iImageLength = len(oImage)
    return oImage,iImageLength


def sStartProcess():
    oCarrier = OpenImage("CarrierPicture.jpg")
    message = GetInfo.getInfo()

    jsonData = json.dumps(message,ensure_ascii=True)

    #Append Message to End of image
    #This does not disrupt the structure of the JPG, JPG interpreters ignore data after EOI(0xFF 0xD9) frame marker
    Tag = [struct.pack("B",0xCA), struct.pack("B",0xFE)]
    OutputLength =struct.pack("L",len(jsonData))
    oEmbeddedMsg = oCarrier[0] + jsonData
    return oEmbeddedMsg,oCarrier[1]

if __name__ == '__main__':
    print sStartProcess()



