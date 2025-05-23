import sys
import asyncio
from .serve import serve

def main():
    """
    Main entry point for the MikroTik MCP server.
    """
    print("Starting MikroTik MCP server...")
    try:
        asyncio.run(serve())
    except Exception as e:
        print(f"Error starting MCP server: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
