import socket

s = socket.socket()
s.bind(('localhost', 1234))
s.listen(1)

print("Server started, waiting for client...")
conn, addr = s.accept()
print("Connected with", addr)

while True:
    frame = conn.recv(1024).decode()
    if frame == "END":
        print("Transmission completed")
        break

    print("Frame received:", frame)
    conn.send("ACK".encode())

conn.close()
s.close()