from fastapi import FastAPI

from money_mastery.controllers.conta import router

app = FastAPI()

@app.get("/", status_code=200)
async def teste_run():
    return dict(msg="A API está no ar!")

app.include_router(router)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', port=3005, reload=True)
