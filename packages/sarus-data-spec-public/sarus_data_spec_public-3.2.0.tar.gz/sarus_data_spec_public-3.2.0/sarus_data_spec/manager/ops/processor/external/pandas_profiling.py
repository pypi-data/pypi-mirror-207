from typing import Any

try:
    from pandas_profiling import ProfileReport
except ModuleNotFoundError:
    pass  # error message in typing.py


async def pd_profile_report(df: Any, *args: Any, **kwargs: Any) -> Any:
    return ProfileReport(df, *args, **kwargs)
