#!/bin/bash

echo "$DOCKERHUB_TOKEN" | docker login -u "$DOCKERHUB_USERNAME" --password-stdin

VERSION=`cat version.txt`
echo "build eureka version ${VERSION}"

docker build . --build-arg EUREKA_VERSION="${VERSION}" -t estuaryoss/netflix-eureka:"${VERSION}"
docker push estuaryoss/netflix-eureka:"${VERSION}"
