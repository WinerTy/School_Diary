from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI(
        title="SchoolDiary",
    )
    return app
