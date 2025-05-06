from core.config import conf


from create_app import create_app

app = create_app()


@app.get("/")
async def root():

    return {"message": "Hello World"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=conf.server.host, port=conf.server.port)
