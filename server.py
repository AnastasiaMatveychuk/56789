import socket
import random

def power(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

def diffie_hellman_server():
    p = 14
    g = 7

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)

    print("Сервер ожидает подключения...")

    conn, addr = server_socket.accept()

    a = random.randint(1, p - 1)
    A = power(g, a, p)
    conn.send(str(A).encode())

    B = int(conn.recv(1024).decode())
    K = power(B, a, p)

    print("Секретное число:", K)

    conn.close()
    server_socket.close()

diffie_hellman_server()
