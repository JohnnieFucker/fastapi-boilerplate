"""
Restful 风格的统一返回格式

@File: restful_model.py
"""
from pydantic import Field
from pydantic import BaseModel
from typing import Generic, TypeVar, Optional


T = TypeVar("T")  # 泛型类型 T


class RestfulModel(BaseModel, Generic[T]):
    """
    RESTful 风格的数据模型，所有 response 统一采用改模型
    """

    code: int = Field(default=0, title="错误码", description="正常状态下返回 0")
    message: str = Field(default="", title="状态消息", description="给出调用者本次接口运行的状态提示信息")
    total: Optional[int] = Field(default=0, title="列表总计", description="正常状态下返回列表总数")
    processing_time: Optional[float] = Field(
        default=0, title="耗时", description="正常状态下返回耗费时长"
    )
    data: Optional[T] = Field(default=None, title="响应的数据部分")
