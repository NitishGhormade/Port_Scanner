import socket

def port_scanner(host, start_port, end_port):
    print(f"Scanning {host} from port {start_port} to {end_port}")
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((host, port))
            if result == 0:
                print(f"Port {port} is open")

if __name__ == "__main__":
    target_host = input("Enter the host to scan (e.g., 127.0.0.1): ")
    port_scanner(target_host, 1, 1024)
