ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
$(eval $(ARGS):;@:)
EXEC = docker-compose exec -w /code siom
RUN = docker-compose exec siom sh
MANAGE_DIR = manage.py

# HELP COMMANDS
help: ## show this help
	@echo 'usage: make [target] [option]'
	@echo ''
	@echo 'Common sequence of commands:'
	@echo '- make build'
	@echo '- make run'
	@echo '- make migrate'
	@echo '- make migrations'
	@echo '- make collectstatic'
	@echo '- make sh'
	@echo '- make logs'
	@echo '- make stop'
	@echo '- make restart'
	@echo ''
	@echo 'targets:'
	@egrep '^(.+)\:\ .*##\ (.+)' ${MAKEFILE_LIST} | sed 's/:.*##/#/' | column -t -c 2 -s '#'

.PHONY : build
build: stop ## build application containers
ifeq ($(ARGS), nocache)
	@ docker-compose build --no-cache
else
	@ docker-compose build
endif

.PHONY : run
run: ## start the application
	@ docker-compose up -d

.PHONY: migrate
migrate: run ## run pending migrations
	@ $(EXEC) python ./manage.py migrate

.PHONY: migrations
migrations: run ## create new migrations
	@ $(EXEC) python ./manage.py makemigrations

.PHONY: collectstatic
collectstatic: run ## create admin static files
	@ $(EXEC) python ./manage.py collectstatic --no-input

.PHONY: shell
shell: run ## runs the application Django shell
	@ $(EXEC) python ./manage.py shell

.PHONY: sh
sh: run ## runs pure shell on application container
	@ $(EXEC) sh

.PHONY: bash
bash: run ## runs pure shell on application container
	@ $(EXEC) bash

.PHONY: logs
logs: ## show the logs on terminal
	@ docker logs -f siom

.PHONY: stop
stop: ## stop all docker compose services
	@ docker-compose down -v

.PHONY: restart
restart: ## stop and recreate the docker compose services
	@ make stop
	@ sleep 2
	@ make run

.PHONY: superuser
superuser: run ## create new superuser
	@ $(EXEC) python ./manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')"
