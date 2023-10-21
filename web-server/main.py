import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [2, 4, 6, 8]

@app.get('/name')
def get_name():
    return {
        'name':'Chanel'
    }

@app.get('/home', response_class=HTMLResponse)
def get_html():
    return """
    <h1>Pagina principal</h1>
    <hr>
    <p> Lorem ipsum </p>
    <button> Presione aqui </button>
    """


def run():
    store.get_categories()

if __name__ == "__main__":
    run()