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


## Estructura de carpetas sugerida

 Esta es la manera en que la documentación de FastAPI aconseja organizar los archivos y carpetas. No es obligatoria esta nomenclatura:

```commandline
- controllers
	- __init__.py
	- auth.py
	- tweet.py
	- user.py
- models
	- __init__.py
	- Tweet.py
	- User.py
- venv
.gitignore
main.py
README.md
requirements.py
```

En *models* tendremos todos los modelos que necesite nuestra aplicación, en *controllers* todos los endpoints.

Ejemplo de como se vería `models/Tweet.py`:

```py
from uuid import UUID
from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, Field

from models import User


class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(
        ...,
        min_length=1,
        max_length=280
    )
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=None)
    created_by: User = Field(...)
```

El archivo `models/__init__.py` sirve para concentrar todo lo que queremos mostrar a otros paquetes. Y sería tan simple como:

```py
from .User import User, UserLogin
from .Tweet import Tweet
```

Ahora veremos los controllers estos cambia un poco de como los usa el profesor porque ahora tendremos routers entre medias, para quien venga de JavaScript es igual que Express.

Ejemplo del archivo `controllers / tweet.py`:

```py
from typing import List

from fastapi import APIRouter, status

from models import Tweet

router = APIRouter(
    prefix="/tweets",
    tags=["Tweets"],
)


@router.get(
    path="/",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Show all tweets",
)
def home():
    pass


@router.get(
    path="/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Show a Tweet",
)
def show_tweet():
    pass


@router.post(
    path="/",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Post a Tweet",
)
def post():
    pass


@router.delete(
    path="/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Delete a Tweet",
)
def delete_tweet():
    pass


@router.put(
    path="/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Update a Tweet",
)
def update_tweet():
    pass
```

Como se puede observar, en lugar de inicializar FastApi() se inicializó ApiRouter() pero funciona de igual manera, Como parámetros a ApiRouter() se le pasó *prefix* y *tags*, todo lo que se aplique a un *Router* se aplica a todas sus rutas hijas por ello, si se ponen tags en el router todas las demás rutas tendrán ese tag y prefix, esto es para no tener que poner en cada path `tweets/resto_de_la_ruta`, porque si se pone en el router ya estará automáticamente en todas.

Esos parámetros no son obligatorios e igual se pueden poner en cada ruta.

Ahora en el archivo `controllers/__init__.py` se crea el router principal de la app y queda algo como esto:

```py
from fastapi import APIRouter

from .user import router as user_router
from .tweet import router as tweet_router
from .auth import router as auth_router

router = APIRouter(
    prefix="/api"
)

router.include_router(user_router)
router.include_router(tweet_router)
router.include_router(auth_router)
```

Simplemente, es la unión de todos los pequeños routers como puedes ver, se añade `prefix="/api"` esto es algo que se puede encontrar en la mayoría de API, que la ruta para acceder a ellas siempre empieza con `nuestro_dominio/api/ resto_de_la_ruta`. Como se ha dicho anteriormente, esto no es necesario y si no se desea que tenga `api` en la ruta simplemente no se pone el *prefix*.

Y por último este es el archivo `main.py` de la app aquí solo se inicializa el server con FastApi() y se le pasa el router
para que lo use:

```py
from fastapi import FastAPI

from controllers import router

app = FastAPI()

app.include_router(router)
```

El import del router es de nuestro paquete controllers, no hay que instalar ningún paquete externo ni nada para hacer esto.

En principio algunos verán esto y se asustarán un poco, pero hay que tener en cuenta que cuando empieces a trabajar nunca te dejaran crear todo en un solo archivo y cuando te acostumbras un poco a este tipo de orden es mucho más cómodo el trabajo.
