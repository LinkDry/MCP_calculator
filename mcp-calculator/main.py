"""MCP计算器服务器入口文件"""

from mcp import MCPServer
from tools import CALCULATOR_TOOLS

# 创建MCP服务器实例
mcp_server = MCPServer()

# 注册所有计算器工具
for tool in CALCULATOR_TOOLS:
    mcp_server.register_tool(
        name=tool["name"],
        description=tool["description"],
        parameters=tool["parameters"],
        return_description=tool["return_description"],
        func=tool["func"]
    )

# 获取FastAPI应用实例
app = mcp_server.app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
