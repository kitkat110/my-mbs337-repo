PORT ?= 8050
NAME ?= "kitkat110/demo-dashboard:0.1.0"

filter:
	docker ps --filter "expose=${PORT}" --format "table {{.Names}}\t{{.Image}}\t{{.Ports}}\t{{.Status}}"

build:
	docker build -t ${NAME} .

run: build
	docker run -p 8050:8050 -d ${NAME}

stop:
	docker stop $(shell docker ps -q)

all: stop build run

compose-down:
	docker compose down

compose-up:
	docker compose up --build -d

compose: compose-down compose-up


compose-down-staging:
	docker compose -f docker-compose-staging.yml down

compose-up-staging:
	docker compose -f docker-compose-staging.yml up --build -d

compose-staging: compose-down-staging compose-up-staging