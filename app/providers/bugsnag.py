import bugsnag  # type: ignore

from app.config import config


if config.bugsnag_api_key:
    bugsnag.configure(
        api_key=config.bugsnag_api_key,
        project_root="./",
    )


def bugsnag_notify(exc: Exception) -> None:
    if config.bugsnag_api_key:
        bugsnag.notify(exc)
    else:
        raise exc
