from fastapi import FastAPI
import dune

app = FastAPI()

@app.get("/")
def run_script():
    result = dune.run()
    return {"result": result}