from fastapi import FastAPI, HTTPException
from typing import Dict, Callable, Any
from .models import ToolCallRequest, ToolCallResponse, ToolDescription, ToolListResponse


class MCPServer:
    """MCP服务器类，用于管理工具注册和处理工具调用"""
    
    def __init__(self):
        self.tools: Dict[str, Dict[str, Any]] = {}
        self.app = FastAPI(
            title="MCP Calculator Server",
            description="模型上下文协议(MCP)计算器服务器，提供各种计算工具",
            version="1.0.0"
        )
        self._setup_routes()
    
    def _setup_routes(self):
        """设置API路由"""
        
        @self.app.post("/api/v1/tool/call", response_model=ToolCallResponse)
        async def call_tool(request: ToolCallRequest):
            """调用指定工具"""
            return self.handle_tool_call(request)
        
        @self.app.get("/api/v1/tools", response_model=ToolListResponse)
        async def list_tools():
            """获取可用工具列表"""
            return self.get_tools_list()
    
    def register_tool(self, name: str, description: str, parameters: list, return_description: str, func: Callable):
        """注册工具到MCP服务器"""
        self.tools[name] = {
            "description": description,
            "parameters": parameters,
            "return_description": return_description,
            "func": func
        }
    
    def handle_tool_call(self, request: ToolCallRequest) -> ToolCallResponse:
        """处理工具调用请求"""
        tool_name = request.tool_name
        
        if tool_name not in self.tools:
            return ToolCallResponse(
                call_id=request.call_id,
                success=False,
                result=None,
                error=f"Tool '{tool_name}' not found"
            )
        
        tool = self.tools[tool_name]
        tool_func = tool["func"]
        
        try:
            # 调用工具函数
            result = tool_func(**request.tool_params)
            return ToolCallResponse(
                call_id=request.call_id,
                success=True,
                result=result,
                error=None
            )
        except Exception as e:
            return ToolCallResponse(
                call_id=request.call_id,
                success=False,
                result=None,
                error=str(e)
            )
    
    def get_tools_list(self) -> ToolListResponse:
        """获取可用工具列表"""
        tools_list = []
        for tool_name, tool_info in self.tools.items():
            tools_list.append({
                "name": tool_name,
                "description": tool_info["description"],
                "parameters": tool_info["parameters"],
                "return_description": tool_info["return_description"]
            })
        return ToolListResponse(tools=tools_list)
    
    def get_app(self) -> FastAPI:
        """获取FastAPI应用实例"""
        return self.app
