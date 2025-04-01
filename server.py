import socket

#HOST = socket.gethostname()

HOST = ('127.0.0.1', 7771)

#print(HOST)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(HOST)
sock.listen()

print("----start----")
conn, addr = sock.accept()
print(conn)
print(addr)

print("end")