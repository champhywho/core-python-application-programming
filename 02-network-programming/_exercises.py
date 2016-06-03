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
"Done in full_duplex_chat_server.py and full_duplex_chat_client.py"


# 9. Multi-User Full Duplex Chat. Further update your solution so that your
# chat service is multi-user.



# 10. Multi-User, Multiroom, Full Duplex Chat. Now make your chat service
# multi-user and multiroom.



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


# 13. Name Server. Design and implement a name server. Such a server is
# responsible for maintaining a database of hostname-port number pairs,
# perhaps along with the string description of the service that the
# corresponding servers provide. Take one or more existing servers and have
# them register their service with our name server. (Note that these servers
# are, in this case, clients of the name server.)
# Every client that starts up has no idea where the server is that it is looking
# for. Also as clients of the name server, these clients should send a request
# to the name server indicating what type of service they are seeking. The name
# server, in reply, returns a hostname-posrt number pair to this client, which
# then connects to the appropriate server to process its rquest.
#
# Extra Credit:
# 1) Add caching to your name server for popular requests.
# 2) Add logging capability to your name server, keeping track of which servers
#    have registered and which services clients are requesting.
# 3) Your name server should periodically ping the registered hosts at their
#    respective port numbers to ensure that the server is indeed up. Repeated
#    failures will cause a server to be delisted from the list of services.
#
# You can implement real services for the servers that register for your name
# service, or just use dummy servers (which merely acknowledge a request).



# 14. Error Checking and Graceful Shutdown. All of the sample cliet/server code
# presented in this chapter is poor in terms of error-checking. We do not handle
# scenarios such as when users press Ctrl+C to exit out of a server or Ctrl+D to
# terminate client input, nor do we check other inproper input to input() or
# handle network errors. Because of this weakness, quite often we terminate an
# application without closing our sockets, potentially losing data. Choose a
# client/server pair of one of our examples, and add enough error-checking so
# that each application properly shuts down, that is, closes network
# connections.



# 15. Asynchronicity and SocketServer/socketserver. Take the example TCP server
# and use either mix-in class to support an asynchronous server. To test your
# server, create and run multiple clients simultaneously and show output that
# your server is serving requests from both, interleaved.



# 16. *Extending SocketServer Classes. In the SocketServer TCP server code, we
# had to change our client from the original base TCP client because the
# CoketServer class does not maintain the connection between requests.
# a) Subclass the TCPServer and StreamRequestHandler classes and re-design the
#    server so that it maintains and uses a single connection for each client
#    (not one per reqeust).
# b) Integrate your solution for the previous exercise with your solution to
#    part (a), such that multiple clients are being serviced in parallel.



# 17. *Asynchronous System. Research at least five different Python-based
# asynchronous systems - choose from Twisted, Greenlets, Tornado, Diesel,
# Concurrence, Eventlet, Gevent, etc. Describe what they are, categorize them,
# find similarities and differences, and then create some demonstration code
# samples.
