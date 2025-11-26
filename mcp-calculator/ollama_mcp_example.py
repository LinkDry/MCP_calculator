"""ollama调用MCP计算器工具的示例脚本"""

import ollama
import requests
import json
from typing import Dict, Any

# MCP服务器配置
MCP_SERVER_URL = "http://localhost:8000/api/v1"

# 系统提示词，指导模型使用MCP工具
SYSTEM_PROMPT = """
你是一个智能助手，能够使用MCP（模型上下文协议）工具来完成各种任务。

你可以使用以下工具：

## 计算器工具

### add
- 描述：执行加法运算，返回两个数的和
- 参数：
  - a: float，第一个加数（必填）
  - b: float，第二个加数（必填）
- 返回：两个数的和，类型为float

### subtract
- 描述：执行减法运算，返回两个数的差
- 参数：
  - a: float，被减数（必填）
  - b: float，减数（必填）
- 返回：两个数的差，类型为float

### multiply
- 描述：执行乘法运算，返回两个数的积
- 参数：
  - a: float，第一个乘数（必填）
  - b: float，第二个乘数（必填）
- 返回：两个数的积，类型为float

### divide
- 描述：执行除法运算，返回两个数的商
- 参数：
  - a: float，被除数（必填）
  - b: float，除数，不能为0（必填）
- 返回：两个数的商，类型为float

### power
- 描述：执行幂运算，返回a的b次方
- 参数：
  - a: float，底数（必填）
  - b: float，指数（必填）
- 返回：a的b次方结果，类型为float

### square_root
- 描述：计算平方根，返回一个数的平方根
- 参数：
  - a: float，要计算平方根的数，必须大于等于0（必填）
- 返回：平方根结果，类型为float

### cube_root
- 描述：计算立方根，返回一个数的立方根
- 参数：
  - a: float，要计算立方根的数，可以是正数或负数（必填）
- 返回：立方根结果，类型为float

### sum_list
- 描述：计算列表中所有数字的和
- 参数：
  - numbers: list，包含数字的列表（必填）
- 返回：列表中所有数字的和，类型为float

### average
- 描述：计算列表中所有数字的平均值
- 参数：
  - numbers: list，包含数字的列表（必填）
- 返回：列表中所有数字的平均值，类型为float

### maximum
- 描述：找出列表中的最大值
- 参数：
  - numbers: list，包含数字的列表（必填）
- 返回：列表中的最大值，类型为float

### minimum
- 描述：找出列表中的最小值
- 参数：
  - numbers: list，包含数字的列表（必填）
- 返回：列表中的最小值，类型为float

### calculate_expression
- 描述：计算数学表达式，支持基本的加减乘除运算
- 参数：
  - expression: str，要计算的数学表达式，例如：1+2*3-4/2（必填）
- 返回：表达式计算结果，类型为float

## 使用工具的格式

当你需要使用工具时，请按照以下格式输出：

```json
{
  "tool_call": {
    "name": "工具名称",
    "params": {
      "参数1": 值1,
      "参数2": 值2
    }
  }
}
```

例如，如果你需要计算1+2，你应该输出：

```json
{
  "tool_call": {
    "name": "add",
    "params": {
      "a": 1,
      "b": 2
    }
  }
}
```

我会将工具调用的结果返回给你，然后你可以根据结果生成最终的回答。
"""


def call_mcp_tool(tool_name: str, params: Dict[str, Any]) -> Dict[str, Any]:
    """调用MCP工具"""
    url = f"{MCP_SERVER_URL}/tool/call"
    payload = {
        "tool_name": tool_name,
        "tool_params": params
    }
    response = requests.post(url, json=payload)
    return response.json()


def ollama_mcp_example():
    """ollama调用MCP的示例"""
    # 用户查询
    user_query = "计算123456的立方根"
    
    print(f"用户查询: {user_query}")
    
    # 第一步：向ollama发送查询，获取工具调用请求
    response = ollama.chat(
        model="qwen3:0.6b",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_query}
        ]
    )
    
    assistant_response = response["message"]["content"]
    print(f"ollama响应: {assistant_response}")
    
    # 第二步：解析ollama响应，提取工具调用请求
    try:
        # 处理Markdown代码块格式，提取纯JSON内容
        if assistant_response.startswith('```json'):
            # 去除Markdown代码块标记
            json_content = assistant_response[7:-3].strip()
        elif assistant_response.startswith('```'):
            # 处理没有指定语言的代码块
            json_content = assistant_response[3:-3].strip()
        else:
            # 直接使用响应内容
            json_content = assistant_response.strip()
        
        tool_call_data = json.loads(json_content)
        tool_call = tool_call_data.get("tool_call")
        
        if tool_call:
            tool_name = tool_call["name"]
            params = tool_call["params"]
            
            print(f"提取到工具调用: 工具名称={tool_name}, 参数={params}")
            
            # 第三步：调用MCP工具
            mcp_result = call_mcp_tool(tool_name, params)
            print(f"MCP工具调用结果: {mcp_result}")
            
            # 第四步：将MCP结果返回给ollama，获取最终响应
            final_response = ollama.chat(
                model="qwen3:0.6b",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_query},
                    {"role": "assistant", "content": assistant_response},
                    {"role": "user", "content": json.dumps(mcp_result)}
                ]
            )
            
            final_answer = final_response["message"]["content"]
            print(f"最终回答: {final_answer}")
        else:
            print("ollama没有返回工具调用请求")
    except json.JSONDecodeError:
        print("ollama返回的不是有效的JSON格式")
    except Exception as e:
        print(f"处理过程中发生错误: {str(e)}")


if __name__ == "__main__":
    ollama_mcp_example()
