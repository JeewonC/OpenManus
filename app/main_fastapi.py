from mcp.server.fastmcp import FastMCP

# This creates the FastAPI app from your MCP server
server = FastMCP("openmanus")

# 👇 This is what Azure needs to find!
app = server.app
