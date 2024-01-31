P2P-multi-user-chatting-application
==============
# Scope
The project involves the design and implementation of a robust Peer-to-Peer Multi-User Chatting
Application using Python and sockets. The application will focus on text-based communication and aim
to provide features similar to popular platforms like Clubhouse.
# Goals
Our objective is to develop a secure peer-to-peer (P2P) chatting application with the adept
implementation of TCP and UDP protocols that allows users to log in with their username and password.
Users can engage in private conversations by sending messages directly to another user or participate in
group discussions within chat rooms. The application will provide a streamlined interface where users
can easily view a list of online users who are available to receive messages and explore available chat
rooms for collaborative interactions. Our emphasis is on ensuring a seamless and secure user experience
for both private messaging and group communication.
# User Authentication and Message Encryption:
- Objective: Allow users to securely log in with a username and password and encrypt messages
for enhanced security.
- Implementation Detail: Utilize TLS (Transport Layer Security) for secure communication during the authentication process and encryption of messages, and use SHA-256 hashing algorithm to hash passwords, in order to guarantee security and integrity.
## Additional Information about SHA-256 Implementation:
- SHA-256 (Secure Hash Algorithm 256-bit) is a cryptographic hashing function utilized to secure
sensitive data, particularly passwords, within our chatting application. In the context of user password
management.
- Password Security: SHA-256 encrypts passwords as irreversible hashes, converting them into
unique strings of fixed length. This implementation ensures that even if the stored hashes are accessed,
the original passwords cannot be derived, enhancing overall security.
- Data Integrity: When users create or update their passwords, SHA-256 generates a hash unique
to that specific input. Any changes to the input will produce a completely different hash, ensuring data
integrity and preventing unauthorized modifications.
- Reduced Vulnerability: Employing SHA-256 mitigates the risk of password-related
vulnerabilities such as plaintext storage or exposure in case of a data breach. This algorithm significantly
increases the difficulty of brute-force attacks or reverse-engineering password hashes.
- Authentication Protection: Hashing passwords with SHA-256 adds an additional layer of
security to user authentication, safeguarding user credentials from unauthorized access or theft.
By integrating SHA-256 for password hashing within our chatting application, we prioritize robust user
authentication and data protection, bolstering the overall security measures to ensure a safer user
experience.
# Functionalities
## User authentication
- Implement a user registration system where users can provide a unique username and a secure
password.
- Validate that the chosen username is unique to prevent duplications.
- Implement password policies, such as minimum length and complexity requirements, to
enhance security.
- Store the user credentials securely, utilizing encryption techniques for password storage.
- Develop a login system that prompts users to enter their registered username and password.
- Verify the entered username exists in the system.
- Validate the entered password against the stored, securely hashed password.
- Grant access upon successful validation.
- Secure username and password exchange over TCP will be employed for user authentication.
- Using hashing algorithms for secure storage and verification of user credentials.
## Basic Client-Server Setup
- Develop a server application that listens for incoming client connections.
- Use sockets or a suitable networking library to establish a server socket.
- Implement a mechanism to accept multiple client connections concurrently.
- Maintain a database to keep track of registered clients.
- Implement a connection initiation process where the client connects to the server's IP address and port.
- Establish a communication protocol between the client and server for data exchange.
- Maintain an updated list of online users on the server.
- Implement a mechanism for clients to notify the server when they connect or disconnect.
- Provide a command or functionality for clients to request the list of online users from the server.
- Ensure the server responds to the client's request with an updated list of online users.
## Chat Room Functionality
- Implement a mechanism for users to create new chat rooms.
- Develop a command or interface for users to provide a unique id for the new chat room.
- Store information about created chat rooms on the server.
- Implement a mechanism for users to join existing chat rooms.
- Provide users with a command or interface to enter the name of the chat room they wish to join.
- Ensure that users can be members of multiple chat rooms simultaneously.
- Develop a command or interface for users to request a list of available chat rooms.
## One-to-One Chat Functionality
- Implement a mechanism that allows users to initiate one-to-one private messaging.
- Users will be able to send and receive messages in that private chat.
- Develop a functionality that notifies users upon the reception of messages.
## Message Formatting and Features
- Ensure that users are capable of taking advantage of basic text formatting like bold and italics.
- Users are allowed to send clickable hyperlinks.
## Error Handling and Resilience
- Handle potential connection errors gracefully, providing meaningful error messages to the user.
- Users must be able to easily understand the error and be able to troubleshoot it.
- Reconnection with the network must occur in case of a network failure.
## User Interface Enhancement
- Develop a command line interface for the chat application.
- Add color-coded messages for better visual distinction.
## Documentation
- Develop user documentation that encompasses installation, configuration, and usage guidelines.
- Documentation providing comprehensive information on system architecture, protocols, and
the structure of the codebase.
## Testing
- Conduct unit testing for each implemented feature.
- Perform integration testing to ensure seamless interactions between different components.
- Conduct stress testing to evaluate system performance under high loads.
## Scalability
- System can handle as many users as possible without any deficiencies.
