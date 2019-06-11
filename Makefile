DOCKER_IMAGE_NAME=shapesai/formatconv3d
TAG?=latest

.PHONY: docker-build
docker-build:
	docker build -t $(DOCKER_IMAGE_NAME):$(TAG) .

.PHONY: docker-run
docker-run:
	docker run --rm \
		--name formatconv3d \
		--mount src="$(PWD)",target=/app,type=bind \
		$(DOCKER_IMAGE_NAME):$(TAG)