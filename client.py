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


def diffie_hellman_client():
    p = 14
    g = 7

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    B = int(client_socket.recv(1024).decode())

    b = random.randint(1, p - 1)
    B = power(g, b, p)
    client_socket.send(str(B).encode())

    K = power(B, b, p)

    print("Секретное число:", K)

    client_socket.close()


diffie_hellman_client()
