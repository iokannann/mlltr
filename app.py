from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Olá": "Mundo! Este é o meu site com FastAPI."}