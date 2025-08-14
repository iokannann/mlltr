from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "HELLO MI HERMANITO, SE TU LER ISSO TU É GAY."}