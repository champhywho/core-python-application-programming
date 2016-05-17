# 4. Update the TCP (tsTclnt.py) and/or UDP (tsUclnt.py) clients so that the
# server name is not hardcoded into the application. Allow the user to specify
# a hostname and port number, and only use the default values if either or both
# parameters are misiing.
"Done in tsTclnt.py"


# 5. Implement the sample TCP client/server programs found in th Python
# Library Reference documentation on the socket module and get them to work.
# Set up the server and then the client. An online version of the source is
# also available here: https://docs.python.org/3/library/socket.html#example
"Done in sample_tcp_server_ip4/6.py and sample_tcp_client_ip4/6.py"

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
"Done in local_server.py and local_client.py"


# 6. Daytime Service. Use the socket.getservbyname() to determine the port
# number for the "daytime" service under the UDP protocol. Check the
# documentation for getservbyname() to get the exact usage syntax (i.e,
# socket.getservbyname.__doc__). Now write an application that sends a dummy
# message over and wait for the reply. Once you have received a reply from the
# server, display it to the screen.
"Done in daytime_server.py and daytime_client.py"


# 7. Half-Duplex Chat. Ceate a simple, half-duplex chat program. By half-duplex,
# we mean that when a connection is made and the service starts, only one
# person can type. The other participant must wait to get a message before
# being prompted to enter a message. Once a message is sent, the sender must
# wait for a reply before being allowed to send another message. One participant
# will be on the server side; the other will be on the client side.
"Done in half_duplex_chat_server.py and half_duplex_chat_client.py"


# 8. Full-Duplex Chat. Update your solution to the previous exercise so that
# your chat service is now full-duplex, meaning that both parties can send and
# receive, independent of each other.
"!!!Solution is postponed until 'threading'."


# 9. Multi-User Full Duplex Chat. Further update your solution so that your
# chat service is multi-user.
"!!!Solution is postponed until 'threading'."


# 10. Multi-User, Multiroom, Full Duplex Chat. Now make your chat service
# multi-user and multiroom.
"!!!Solution is postponed until 'threading'."


# 11. Web Client. Write a TCP client that connects to port 80 of your favorite
# Web site (remove the "http://" and any trailing information: use only the
# hostname). Once a connection has been established, send the HTTP command
# string GET /\n and write all the data that the server returns to a file.
# (The GET command retrieves a Web page, the / file indicates the file to get,
# and \n sends the command to the server.) Examine the contents of the retrieved
# file. What is it? How can your check to make sure the data you received is
# correct? (Note: You might have to insert one or two NEWLINEs after the
# command string. One usually works.)
"Done in web_client.py"


# 12. Sleep Server. Create a sleep server. A client will request to be "put
# to sleep" for a number of seconds. The server will issue the command on behalf
# of the client then return a message to the client indicating success. The
# client should have slept or should have been idle for the exact time
# requested. This is a simple implementation of remote procedure call, where a
# client's request invokes commands on another computer across the network.
"Done in sleep_server.py and sleep_client.py"
