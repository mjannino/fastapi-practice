DOC_TYPE=html
CMD=bash

build:
	docker-compose build fastapi-app

start:
	docker-compose up -d

stop:
	docker-compose down

app.logs:
	docker logs -f fastapi-app

app.shell:
	docker exec -it fastapi-app /bin/bash

rebuild-all:
	docker-compose down && docker-compose build && docker-compose up -d

clean:
	docker container prune -f && docker image prune -f