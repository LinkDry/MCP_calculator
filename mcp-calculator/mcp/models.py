from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional


class ToolCallRequest(BaseModel):
    """工具调用请求模型"""
    tool_name: str = Field(..., description="要调用的工具名称")
    tool_params: Dict[str, Any] = Field(..., description="工具调用参数")
    call_id: Optional[str] = Field(None, description="调用ID，用于跟踪请求")


class ToolCallResponse(BaseModel):
    """工具调用响应模型"""
    call_id: Optional[str] = Field(None, description="调用ID，与请求对应")
    success: bool = Field(..., description="调用是否成功")
    result: Any = Field(..., description="工具调用结果")
    error: Optional[str] = Field(None, description="错误信息，仅在success为False时提供")


class ToolParameter(BaseModel):
    """工具参数描述模型"""
    name: str = Field(..., description="参数名称")
    type: str = Field(..., description="参数类型")
    description: str = Field(..., description="参数描述")
    required: bool = Field(..., description="是否为必填参数")


class ToolDescription(BaseModel):
    """工具描述模型"""
    name: str = Field(..., description="工具名称")
    description: str = Field(..., description="工具功能描述")
    parameters: List[ToolParameter] = Field(..., description="工具参数列表")
    return_description: str = Field(..., description="返回值描述")


class ToolListResponse(BaseModel):
    """工具列表响应模型"""
    tools: List[ToolDescription] = Field(..., description="可用工具列表")
