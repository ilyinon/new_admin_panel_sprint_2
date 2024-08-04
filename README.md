# Проектное задание: Docker-compose

1. Нужно скопировать `.env_example` в `.env`. Отредактировать при необходимости.
2. Для того чтобы запустить проект нужно выполнить команду
`docker-compose up  -d --build`

после этого можно войти в админку `http://localhost/admin/`, для входа используйте логин `admin` и пароль `123123`

3. для запуска swagger используйте комманду в корне проекта
` docker run -d -p 8080:8080 --name swagger -v ./swagger/openapi.yaml/openapi.yaml:/swagger.yaml -e SWAGGER_JSON=/swagger.yaml swaggerapi/swagger-ui` после этого можно полкючиться `localhost:8000`


# Проектное задание: создать API

получить список фильмов по API через `http://localhost/api/v1/movies/`
получить фильм по его UUID через  `http://localhost/api/v1/movies/<UUID>`
