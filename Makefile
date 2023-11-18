up:
	docker-compose --profile prod up

down:
	docker-compose --profile prod down

shell:
	docker-compose exec tts-backend bash



local_build:
	docker-compose --profile development build

local_up:
	docker-compose --profile development up

local_down:
	docker-compose --profile development down

local_shell:
	docker-compose exec tts-backend-dev bash

test:
	docker-compose run --rm tts-backend-dev sh -c "pytest"


format:
	isort .
	black .
	flake8 . --count --show-source --statistics --max-line-length 120


lint:
	flake8 . --count --show-source --statistics --max-line-length 120
	isort --check .
	black --check .
	#mypy .
