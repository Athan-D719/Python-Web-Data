import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating a mysocket-object
mysocket.connect(('data.pr4e.org', 80)) #using the connect method: Host,Port
#NOT SENDING ANY DATA BUT "DAILING THE PHONE"
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode() #method to encode the data to be send to the server, in thi case a GET request
                                                       #headers
mysocket.send(cmd) #method to send data through the socket #first send.


while True: #retreiving data untill the server stops retrieving.
    data = mysocket.recv(512) #receiving up to 512 characters declared in the data variable(encoded)
    if (len(data) < 1):
        break #if theres nothing received it will break the while loop. WHEN ITS DONE
    print(data.decode(), end='') #decoding the data encoded variable.  UTF-8 decoded data.

mysocket.close() #closing the comminication after all is done
''' 
HTTP/1.1 200 OK
Date: Thu, 18 Jun 2020 23:30:36 GMT
Server: Apache/2.4.18 (Ubuntu)
Last-Modified: Sat, 13 May 2017 11:22:22 GMT
ETag: "1d3-54f6609240717"
Accept-Ranges: bytes
Content-Length: 467
Cache-Control: max-age=0, no-cache, no-store, must-revalidate
Pragma: no-cache
Expires: Wed, 11 Jan 1984 05:00:00 GMT
Connection: close
Content-Type: text/plain

Why should you learn to write programs?

Writing programs (or programming) is a very creative
and rewarding activity.  You can write programs
 for
many reasons, ranging from making your living to solving
a difficult data analysis problem to having fun to helping
someone else solve a problem.  This book assumes that
everyone needs to know how to program, and that once
you know how to program you will figure out what you want
to do with your newfound skills. '''

