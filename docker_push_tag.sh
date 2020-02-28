#!/bin/bash

echo "$DOCKERHUB_TOKEN" | docker login -u "$DOCKERHUB_USERNAME" --password-stdin

VERSION=`cat version.txt`
echo "build eureka version ${VERSION}"

docker build . --build-arg EUREKA_VERSION="${VERSION}" -t dinutac/netflixoss-eureka:"${VERSION}"
docker push dinutac/netflixoss-eureka:"${VERSION}"
