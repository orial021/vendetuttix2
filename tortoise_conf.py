TORTOISE_ORM = {
    "connections": {
        "default": "postgres://postgres:2354@localhost:5432/fastAPI"
    },
    "apps": {
        "models": {
            "models": ["models", "aerich.models"], 
            "default_connection": "default",
        },
    },
}