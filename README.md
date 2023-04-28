# CHAP-Project

The CHAP simulation application is a program that simulates the challenge-handshake authentication protocol (CHAP) using a graphical user interface (GUI). 
The application consists of two nodes: Node A, which represents the client seeking authentication, and Node B, which represents the server. 
To authenticate, Node A sends a code to Node B, which responds by sending a random number to Node A. 
Node A then performs a challenge on the random number and sends the result to Node B. 
Node B performs the same challenge on the random number it sent to Node A and compares the results. 
If the results match, authentication is successful; otherwise, access is denied.

The application is implemented using Python and the Tkinter library for the GUI. 
The user interface consists of several input fields for the code and secret, as well as labels that display the data exchanged between the two nodes during the authentication process. 
The application also includes error handling to handle invalid input from the user.

Overall, the CHAP simulation application provides a useful tool for understanding the challenge-handshake authentication protocol and how it works in practice. 
By simulating the protocol in real-time, users can gain a better understanding of how the protocol ensures secure authentication between two nodes.
