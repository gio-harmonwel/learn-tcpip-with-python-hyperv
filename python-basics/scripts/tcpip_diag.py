import socket
import platform


def check_tcp_port(host: str, port: int, timeout: float = 2.0) -> bool:
    """Verify TCP 3-way handshake connectivity to a target host and port."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        return sock.connect_ex((host, port)) == 0


def get_dynamic_ip() -> str:
    """Retrieve the primary dynamically assigned IPv4 address of this node."""
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        try:
            sock.connect(("8.8.8.8", 80))
            return sock.getsockname()
        except OSError:
            return "127.0.0.1"


if __name__ == "__main__":
    print(f"Node Hostname : {socket.gethostname()}")
    print(f"Operating Sys : {platform.system()} {platform.release()}")
    print(f"Assigned IPv4 : {get_dynamic_ip()}")
    print("-" * 45)

    targets = [
        ("8.8.8.8", 53, "Public DNS (UDP/TCP 53)"),
        ("1.1.1.1", 443, "HTTPS / TLS (TCP 443)"),
        ("127.0.0.1", 22, "Local SSH Daemon (TCP 22)"),
    ]

    for host, port, label in targets:
        status = "OPEN" if check_tcp_port(host, port) else "CLOSED / FILTERED"
        print(f"[{label}] {host}:{port} -> {status}")
