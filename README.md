# twitter-api-fastapi
API based on Twitter API created with the framework FastAPI.


## Llamadas al mismo endpoint con diferentes métodos HTTP

Es posible llamar al mismo endpoint con los diferentes métodos HTTP, sin tener la necesidad de agregar un /update, /delete, etc. al final del path:


```py
@router.get(
    path="/{user_id}",
    response_model=User,
    summary="Show a user based on the id",
)
def show_user():
    pass


@router.delete(
    path="/{user_id}",
    response_model=User,
    summary="Delete a user based on the id",
)
def delete_user():
    pass


@router.put(
    path="/{user_id}",
    response_model=User,
    summary="Update a user based on the id",
)
def update_user():
    pass
```

Como puedes ver se puede usar @router en lugar de @app, para no tener todos los endpoint en un solo archivo. Se usa la clase APIRouter como en el siguiente tutorial: https://www.fastapitutorial.com/blog/fastapi-route/, En este caso, se podría implementar de la siguiente manera:

```py
# main.py

from fastapi import FastAPI

from routes import route_auth, route_users

app = FastAPI()


@app.get(path="/")
def home():
    return {"Twitter API": "Working!"}


app.include_router(route_auth.router, prefix="/auth", tags=["Auth"])
app.include_router(route_users.router, prefix="/users", tags=["Users"])
```

```py
# routes/route_auth.py

from fastapi import APIRouter, status

from models.user import User

router = APIRouter()


@router.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new User",
)
def signup():
    pass


@router.post(
    path="/login",
    response_model=User,
    summary="Login a User",
)
def login():
    pass
```


## Convenciones endpoints

Así como existen convenciones para la forma en la que escribimos el código, también existen convenciones para la forma en la que se nombran o se definen las rutas en los endpoints.

Aquí hay un link con algunas reglas de ejemplo: https://restfulapi.net/resource-naming/

**URLs**

Teniendo en cuenta lo anterior una forma de manejar los endpoints podría ser:

**Tweets**

- **GET/tweets/ ->** Shows all tweets
- **GET/tweets/{id} ->** Shows a specific tweet
- **POST/tweets/ ->** Creates a new tweet
- **PUT/tweets/{id} ->** Updates a specific tweet
- **DELETE/tweets/{id} ->** Deletes a specific tweet

**Authentication**

- **POST/auth/signup ->** Registers a new user
- **POST/auth/login ->** Login a user

**Users**

- **GET/users/ ->** Shows all users
- **GET/users/{id} ->** Gets a specific user
- **PUT/users/{id} ->** Updates a specific user
- **DELETE/users/{id} ->** Deletes a specific user


## Sobre las fechas

"A timestamp without a time zone attached gives no useful information,
because without the time zone, you cannot infer what point in time your

application is really referring to."

La frase de arriba es de un libro llamado *Serious Python* y es muy cierta, no nos sirve de nada tener una fecha y hora si no sabemos a qué zona horaria corresponde, para esto tenemos que crear un ‘time zone-aware timestamp’ para lo cual una opción sería hacer lo siguiente:

```py
from datetime import datetime

from dateutil import tz  # Esto se debe instalar en el entorno virtual con pip3 install python-dateutil

created_at = datetime.utcnow().replace(tzinfo=tz.tzutc())
```
