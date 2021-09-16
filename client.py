import socket
import os

IP = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 10000
CLIENT_DATA_PATH = "client_data"


def main():
    FIRST = True
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    while True:
        data = client.recv(SIZE).decode(FORMAT)
        # print(data, "client_data")

        if(data.split("@"))[0] == "FDOWN":
            cmd = data.split("@")[0]
        else:
            cmd, msg = data.split("@")

        if cmd == "DISCONNECTED":
            print(f"[SERVER]: {msg}")
            break

        elif cmd == "OK":
            print(f"{msg}")
            if FIRST:
                helper = ""
                helper += "---------- Commands are not case sensitive ----------.\n"
                helper += "LIST                 : List all the files from the server.\n"
                helper += "UPLOAD <path>        : Upload a file to the server. Give the path of the file to be uploaded to the server.\n"
                helper += "DELETE <filename>    : Delete a file from the server.\n"
                helper += "DOWNLOAD <filename>  : Download a file from the server.\n"
                helper += "LOGOUT               : Disconnect from the server.\n"
                helper += "HELP                 : List all the commands.\n"
                print(helper)
                FIRST = False

        elif cmd == "FDOWN":
            procData = data.split("@")
            name, text = procData[1], procData[2]
            filepath = os.path.join(CLIENT_DATA_PATH, name)
            with open(filepath, "w") as f:
                f.write(text)

            print("File downloaded successfully.")

        data = input("> ")
        data = data.split(" ")
        cmd = data[0]
        cmd = cmd.upper()

        if cmd == "HELP":
            client.send(cmd.encode(FORMAT))

        elif cmd == "LOGOUT":
            client.send(cmd.encode(FORMAT))
            break
        
        elif cmd == "DOWNLOAD":
            filename = data[1]
            send_data = f"{cmd}@{filename}"
            # print("iam here", send_data)
            client.send(send_data.encode(FORMAT))


        elif cmd == "LIST":
            client.send(cmd.encode(FORMAT))

        elif cmd == "DELETE":
            client.send(f"{cmd}@{data[1]}".encode(FORMAT))

        elif cmd == "UPLOAD":
            path = data[1]

            with open(f"{path}", "r") as f:
                text = f.read()

            filename = path.split("/")[-1]
            send_data = f"{cmd}@{filename}@{text}"
            client.send(send_data.encode(FORMAT))
        
        else:
            print("Not a valid command")
            client.send("LOGOUT".encode(FORMAT))
            break
    
    print("Disconnected from the server.")
    client.close()


if __name__ == "__main__":
    main()
