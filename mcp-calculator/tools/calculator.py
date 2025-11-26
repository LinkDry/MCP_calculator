"""计算器工具模块，提供各种计算功能"""


def add(a: float, b: float) -> float:
    """加法运算"""
    return a + b


def subtract(a: float, b: float) -> float:
    """减法运算"""
    return a - b


def multiply(a: float, b: float) -> float:
    """乘法运算"""
    return a * b


def divide(a: float, b: float) -> float:
    """除法运算"""
    if b == 0:
        raise ValueError("除数不能为0")
    return a / b


def power(a: float, b: float) -> float:
    """幂运算，计算a的b次方"""
    return a ** b


def square_root(a: float) -> float:
    """平方根运算"""
    if a < 0:
        raise ValueError("不能计算负数的平方根")
    return a ** 0.5


def cube_root(a: float) -> float:
    """立方根运算"""
    return a ** (1/3)


def sum_list(numbers: list) -> float:
    """计算列表中所有数字的和"""
    return sum(numbers)


def average(numbers: list) -> float:
    """计算列表中所有数字的平均值"""
    if not numbers:
        raise ValueError("列表不能为空")
    return sum(numbers) / len(numbers)


def maximum(numbers: list) -> float:
    """找出列表中的最大值"""
    if not numbers:
        raise ValueError("列表不能为空")
    return max(numbers)


def minimum(numbers: list) -> float:
    """找出列表中的最小值"""
    if not numbers:
        raise ValueError("列表不能为空")
    return min(numbers)


def calculate_expression(expression: str) -> float:
    """计算数学表达式"""
    # 安全检查：只允许基本数学运算和数字
    allowed_chars = set("0123456789+-*/(). ")
    if not all(c in allowed_chars for c in expression):
        raise ValueError("表达式包含不允许的字符")
    try:
        return eval(expression)
    except Exception as e:
        raise ValueError(f"表达式计算错误: {str(e)}")


# 工具描述信息，用于注册到MCP服务器
CALCULATOR_TOOLS = [
    {
        "name": "add",
        "description": "执行加法运算，返回两个数的和",
        "parameters": [
            {
                "name": "a",
                "type": "float",
                "description": "第一个加数",
                "required": True
            },
            {
                "name": "b",
                "type": "float",
                "description": "第二个加数",
                "required": True
            }
        ],
        "return_description": "两个数的和，类型为float",
        "func": add
    },
    {
        "name": "subtract",
        "description": "执行减法运算，返回两个数的差",
        "parameters": [
            {
                "name": "a",
                "type": "float",
                "description": "被减数",
                "required": True
            },
            {
                "name": "b",
                "type": "float",
                "description": "减数",
                "required": True
            }
        ],
        "return_description": "两个数的差，类型为float",
        "func": subtract
    },
    {
        "name": "multiply",
        "description": "执行乘法运算，返回两个数的积",
        "parameters": [
            {
                "name": "a",
                "type": "float",
                "description": "第一个乘数",
                "required": True
            },
            {
                "name": "b",
                "type": "float",
                "description": "第二个乘数",
                "required": True
            }
        ],
        "return_description": "两个数的积，类型为float",
        "func": multiply
    },
    {
        "name": "divide",
        "description": "执行除法运算，返回两个数的商",
        "parameters": [
            {
                "name": "a",
                "type": "float",
                "description": "被除数",
                "required": True
            },
            {
                "name": "b",
                "type": "float",
                "description": "除数，不能为0",
                "required": True
            }
        ],
        "return_description": "两个数的商，类型为float",
        "func": divide
    },
    {
        "name": "power",
        "description": "执行幂运算，返回a的b次方",
        "parameters": [
            {
                "name": "a",
                "type": "float",
                "description": "底数",
                "required": True
            },
            {
                "name": "b",
                "type": "float",
                "description": "指数",
                "required": True
            }
        ],
        "return_description": "a的b次方结果，类型为float",
        "func": power
    },
    {
        "name": "square_root",
        "description": "计算平方根，返回一个数的平方根",
        "parameters": [
            {
                "name": "a",
                "type": "float",
                "description": "要计算平方根的数，必须大于等于0",
                "required": True
            }
        ],
        "return_description": "平方根结果，类型为float",
        "func": square_root
    },
    {
        "name": "cube_root",
        "description": "计算立方根，返回一个数的立方根",
        "parameters": [
            {
                "name": "a",
                "type": "float",
                "description": "要计算立方根的数，可以是正数或负数",
                "required": True
            }
        ],
        "return_description": "立方根结果，类型为float",
        "func": cube_root
    },
    {
        "name": "sum_list",
        "description": "计算列表中所有数字的和",
        "parameters": [
            {
                "name": "numbers",
                "type": "list",
                "description": "包含数字的列表",
                "required": True
            }
        ],
        "return_description": "列表中所有数字的和，类型为float",
        "func": sum_list
    },
    {
        "name": "average",
        "description": "计算列表中所有数字的平均值",
        "parameters": [
            {
                "name": "numbers",
                "type": "list",
                "description": "包含数字的列表",
                "required": True
            }
        ],
        "return_description": "列表中所有数字的平均值，类型为float",
        "func": average
    },
    {
        "name": "maximum",
        "description": "找出列表中的最大值",
        "parameters": [
            {
                "name": "numbers",
                "type": "list",
                "description": "包含数字的列表",
                "required": True
            }
        ],
        "return_description": "列表中的最大值，类型为float",
        "func": maximum
    },
    {
        "name": "minimum",
        "description": "找出列表中的最小值",
        "parameters": [
            {
                "name": "numbers",
                "type": "list",
                "description": "包含数字的列表",
                "required": True
            }
        ],
        "return_description": "列表中的最小值，类型为float",
        "func": minimum
    },
    {
        "name": "calculate_expression",
        "description": "计算数学表达式，支持基本的加减乘除运算",
        "parameters": [
            {
                "name": "expression",
                "type": "str",
                "description": "要计算的数学表达式，例如：1+2*3-4/2",
                "required": True
            }
        ],
        "return_description": "表达式计算结果，类型为float",
        "func": calculate_expression
    }
]
