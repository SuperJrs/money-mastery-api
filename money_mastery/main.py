from fastapi import FastAPI

from money_mastery.controllers.conta import router
from money_mastery.core.database import database

app = FastAPI()

@app.get("/", status_code=200)
async def teste_run():
    return dict(msg="A API está no ar!")


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(router)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', port=3005, reload=True)
