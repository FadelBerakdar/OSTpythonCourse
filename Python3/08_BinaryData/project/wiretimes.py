"""
create a program named wiretimes.py that reads the wireshark.bin data file
dumped from the wireshark program (to get it, right-click the link
http://courses.oreillyschool.com/Python3/software/wireshark.bin, select Save
Target As, and save the file to your Python3_Homework08/src folder.).

The file begins with a header:
Wireshark file header:

guint32 magic_number; /* magic number */
guint16 version_major; /* major version number */
guint16 version_minor; /* minor version number */
gint32 thiszone; /* GMT to local correction */
guint32 sigfigs; /* accuracy of timestamps */
guint32 snaplen; /* max length of captured packets, in octets */
guint32 network; /* data link type */
Each packet is then preceded by a four-entry header:
guint32 ts_sec; /* timestamp seconds */
guint32 ts_usec; /* timestamp microseconds */
guint32 incl_len; /* number of octets of packet saved in file */
guint32 orig_len; /* actual length of packet */
For more detailed information about the wireshark dump file format,
see http://wiki.wireshark.org/Development/LibpcapFileFormat.
Print the timestamp for each packet in seconds and microseconds.
Submit wiretimes.py when it is working to your satisfaction.
"""

file = open("wireshark.bin", "rb")
data = file.read()
file.close()

import struct


x, = struct.unpack("=c", data)
print(x)

