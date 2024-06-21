"""
开发环境的配置文件

@File: dev.py
"""

from pydantic import BaseConfig


class AppConfig(BaseConfig):
    print("load config from dev")
    """app启动的相关配置"""
    HOST: str = "0.0.0.0"
    PORT: int = 8888
    ENVIRONMENT: str = "dev"
    RELEASE_VERSION: str = "1.0.0"
    PROJECT_TITLE: str = "Shannon Insights"
    PROJECT_DESCRIPTION: str = (
        "use machine learning in industry for prediction and evaluation and so on"
    )
    
    # NACOS: dict = {
    #     "host": "",
    #     "namespace": "",
    #     "port": "",
    #     "group_name": ""
    # }

