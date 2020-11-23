.PHONY: build start stop healthcheck

build: Dockerfile copy/server.py
	docker build -t alefly/server:v1 . 
	
start: build
	docker volume create logs
	docker run --rm --name server --mount source=logs,target=/var/log -p 1488:8080 -d alefly/server:v1
	
stop: 
	docker stop server
	
clean: 
	docker rmi alefly/server:v1
	docker volume rm logs
	
healthcheck:
	docker --version
	python3 --version
