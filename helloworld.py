import subprocess

def run_docker_commands():
    try:
        # Build client and server images
        subprocess.run(["docker", "build", "-t", "client", "-f", "Dockerfile", "./client"], check=True)
        subprocess.run(["docker", "build", "-t", "server", "-f", "Dockerfile", "./server"], check=True)

        # Create Docker network
        subprocess.run(["docker", "network", "create", "my_network"], check=True)

        # Run server container
        subprocess.run(["docker", "run", "-d", "--name", "server", "--network", "my_network", "server"], check=True)

        # Run client container
        subprocess.run(["docker", "run", "--rm", "--name", "client", "--network", "my_network", "client"], check=True)

    finally:
        # Tear down: stop and remove containers, remove network
        subprocess.run(["docker", "stop", "server"], check=True)
        subprocess.run(["docker", "rm", "server"], check=True)
        subprocess.run(["docker", "network", "rm", "my_network"], check=True)

if __name__ == "__main__":
    run_docker_commands()