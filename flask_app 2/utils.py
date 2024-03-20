from datetime import datetime


def current_time() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
