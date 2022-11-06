from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def indnex():
    return 'db_test'