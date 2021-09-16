Directory client_data : client data files are stored here for clarity. files can come from any where in the client system given the right path.

        --> singleline.txt : contains single line text
        --> multiline.txt  : coatains multi line text

Directory server_data : contains files recieved from the client

client.py : python code for client operations

server.py : python code for server operations. This file creates threads of clients which can interact concurrently with the server.

Makefile : 

        --> Command make : lists the make options available
        --> Command make server : runs the server.py code
        --> Command make client : runs the client.py code

Report.pdf : Report for the application. Contains information about client operations and some screenshots of those commands run on the terminal

** Compiling Instructions can be found in the Report.pdf along with the screenshots.

                    ***************************** Individual Contributions *****************************

                    Abhinay podugu : Coded the server side script. Used threading library for creating multiple
                                     instances of the client. Created the test text files for file transfer. 
                                     Documented the information in Report.pdf .
                    
                    Sai Thanoj : Coded the client side script. Used socket library for achieving connection 
                                 between server and client.

