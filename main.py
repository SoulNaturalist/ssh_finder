import socket

def search_open_ports() -> None:
    """Method for check open ssh ports"""
    COUNT_PORT_ENUMERATION = 400
    START_IP = "192.168.1"

    for i in range(100, COUNT_PORT_ENUMERATION):
        ip_search = f'{START_IP}.{i}'
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((f'{ip_search}',22))
        if result == 10035:
            print(f'{ip_search} Resource not available')
        elif result == 0:
            print(f'{ip_search} Ssh port open')

if __name__ == '__main__':
    search_open_ports()