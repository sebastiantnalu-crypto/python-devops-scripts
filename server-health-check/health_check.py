import subprocess

servers = ["google.com", "github.com", "cloudflare.com"]

for server in servers:
    result = subprocess.run(
        ["ping", "-c", "1", server],
        stdout=subprocess.DEVNULL
    )

    if result.returncode == 0:
        print(f"[OK] {server} is reachable")
    else:
        print(f"[ERROR] {server} is unreachable")
