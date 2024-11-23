# FastAPI Boilerplate

## Setup
### Install Python and PostgreSQL

```sh
asdf install
```

## Create env

```sh
python -m venv env
source ./env/bin/activate
```

## Install Dependencies

```sh
pip install -r requirements.txt
```

## Create Env File

```sh
cp .env.sample .env.local
```

## Generatie Keys

```python
from scripts.generate_key import generate_key


print(f'A256GCM_KEY="{generate_key(32)}"')
print(f'JWT_SECRET_KEY="{generate_key(64)}"')
print(f'SESSION_SECRET_KEY="{generate_key(88)}"')
print(f'SESSION_SALT="{generate_key(64)}"')
```

## Start Dev Server

```python
make d
```
