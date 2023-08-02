from fastapi import FastAPI

app= FastAPI()

app.title=" Mi aplicacion con fastapi"
app.version="1.0.0"

@app.get('/',tags=['Home'])
def message():
    return 'Hola Mundo'