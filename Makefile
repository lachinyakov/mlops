CWD=/go/src/gitlab.com/yakovlachin/mlops
IMAGE=gitlab.com/yakovlachin/mlops

create-network:
	@-docker network create dev-network

up: create-network
	@ IMG=$(IMAGE) docker-compose up -d

down:
	@- IMG=$(IMAGE) docker-compose down --rmi local

clean:
	@-docker run --rm -v $(CURDIR):$(CWD) -w $(CWD) golang:1.13.3  sh -c "rm -rf ./tmp/*"

.dvc:
	bash ./scripts/dvc_init.sh

data/data.csv:
	bash ./scripts/lessons_get_test_data.sh

.DEFAULT_GOAL=image

.PHONY: acceptance docs
