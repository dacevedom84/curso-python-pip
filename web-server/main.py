import store
from fastapi import FastApi
from fastapi.responses import HTMLResponse

app = FastApi()

@app.get('/')
def get_list():
    return[1,2,3,]

@app.get('/contact', response_class=HTMLResponse)
def get_list():
    return """
        <h1> Hola soy una pñagina </h1>
        <p> Y yo soy un parrafo muy cortico </p>
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()