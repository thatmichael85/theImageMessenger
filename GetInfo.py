"""
GetInfo

This Lib contains code to to get and return current machine information
Currently works for windows

"""
import os
import socket
import netifaces  # not a default Python package
import platform
import subprocess
import re


def getInfo():
    """
    This API returns the machine info.
    :return: Machine info in a dictionary
    """
    info = {}

    # get IPAddress
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8',80))
    info['IPaddress'] = s.getsockname()[0]

    # Get  MACaddress
    info['MACaddr'] = 'ABCD'#getMacAddress(socket.gethostbyname(socket.gethostname()))

    # Get Computer Name
    info['CompName'] = socket.gethostname()

    # Get username
    info['Username'] = os.environ.get("USERNAME")

    # Get disksize
    info['DiskSize'] = getDiskSize()

    return info


def getDiskSize():
    """
    This API returns the following:
    if Windows:
        it will return all the local disks, their letters and the size of each disk
    if Linux/Unix:
        TODO:
    if OSX:
        TODO:
    :return: results
    """
    OS = platform.system()
    results = {}
    if OS == 'Windows':
        s = subprocess.check_output('WMIC logicaldisk get caption,size')
        s = s.rstrip()
        s = s.split('\n')
        for each in s:
            matched = re.search(r'(\w:)\s*(\w+)', each)
            if matched is not None:
                results[matched.group(1)] = matched.group(2)  # returned value is in bytes
    return results


def getMacAddress(IPaddr):
    """
    This API returns the macAddress of the NIC that maches the input ipaddr
    :param IPaddr: Input IP
    :return: Mac address
    """
    i = netifaces.interfaces()
    for each in i:
        if netifaces.AF_INET in netifaces.ifaddresses(each):
            if IPaddr == netifaces.ifaddresses(each)[netifaces.AF_INET][0]['addr']:
                return netifaces.ifaddresses(each)[netifaces.AF_LINK][0]['addr']


if __name__ == "__main__":
    print getInfo()


