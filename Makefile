local_build:
	docker-compose build --parallel
	docker-compose up
	docker-compose logs -f web db

local_up:
	docker-compose up


local_down:
	docker-compose down

local_shell:
	docker-compose exec web bash

test:
	docker-compose run --rm web sh -c "pytest"


format:
	isort .
	black .
	flake8 . --count --show-source --statistics --max-line-length 120


lint:
	flake8 . --count --show-source --statistics --max-line-length 120
	isort --check .
	black --check .
	#mypy .