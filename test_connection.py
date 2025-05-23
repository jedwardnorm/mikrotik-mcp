import paramiko
import sys

def test_connection():
    try:
        # Create a new SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Connection parameters
        hostname = "192.168.88.1"
        username = "admin"
        password = "Cignorj3nb1986!"
        port = 22
        
        print(f"Attempting to connect to {hostname}...")
        
        # Attempt to connect
        ssh.connect(hostname, port, username, password)
        
        print("Successfully connected!")
        
        # Get firewall filter rules
        stdin, stdout, stderr = ssh.exec_command("/ip firewall filter print")
        
        print("\nFirewall Filter Rules:")
        print(stdout.read().decode())
        
        # Close the connection
        ssh.close()
        print("Connection closed successfully")
        
    except Exception as e:
        print(f"Connection failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    test_connection()
