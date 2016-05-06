# 4. Update the TCP (tsTclnt.py) and/or UDP (tsUclnt.py) clients so that the
# server name is not hardcoded into the application. Allow the user to specify
# a hostname and port number, and only use the default values if either or both
# parameters are misiing.
print("Done in tsTclnt.py")


# 5. Implement the sample TCP client/server programs found in th Python
# Library Reference documentation on the socket module and get them to work.
# Set up the server and then the client. An online version of the source is
# also available here: http://docs.python.org/library/socket#example
print("Done in sample_tcp_server_ip4/6.py and sample_tcp_client_ip4/6.py")

# You decide the server is too boring. Update the server so that it can do
# much more, recognizing the following commands:
# date  Server will return its current date/timestamp, that is, time.ctime().
# os    Get OS information (os.name).
# ls    Give listing of current directory. (Hints: os.listdir() lists a
#       directory, os.curdir is the current directory.) Extra Credit: Accept
#       ls dir and return dir's file listing.
#
# You do not need a network to do this assignment - your computer can
# communicate with itself. Be aware that after the server exits, the binding
# must be cleared before you can run it again. You might experience 'port
# already bound' errors. The operating system usually clears the binding
# within 5 minutes, so be patient.
print("Done in local_server.py and local_client.py")
