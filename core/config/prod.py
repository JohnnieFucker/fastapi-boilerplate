from pydantic import BaseConfig


class AppConfig(BaseConfig):
    print("load config from production")
    """app启动的相关配置"""
    HOST: str = "0.0.0.0"
    PORT: int = 8888
    ENVIRONMENT: str = "production"
    RELEASE_VERSION: str = "1.0.0"
    PROJECT_TITLE: str = "Shannon Insights"
    PROJECT_DESCRIPTION: str = (
        "use machine learning in industry for prediction and evaluation and so on"
    )