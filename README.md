# netflix-eureka
NetflixOSS Eureka server registry with updated tomcat and eureka version

## Build status
[![Build Status](https://travis-ci.com/estuaryoss/netflixoss-eureka.svg?token=UC9Z5nQSPmb5vK5QLpJh&branch=master)](https://travis-ci.com/estuaryoss/netflixoss-eureka)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/291184c490c442f6b803a6573483dc21)](https://www.codacy.com/gh/estuaryoss/netflixoss-eureka?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=estuaryoss/netflixoss-eureka&amp;utm_campaign=Badge_Grade)

## Docker Hub
[estuaryoss/netflix-eureka](https://hub.docker.com/r/estuaryoss/netflix-eureka)  ![](https://img.shields.io/docker/pulls/estuaryoss/netflix-eureka.svg)

## Docker run
```shell script
docker run -d -p 8080:8080 estuaryoss/netflix-eureka:1.9.26
```

## Docker run with replication
```shell script
docker run -d -p 8080:8080 \   
-e JAVA_OPTS="-Deureka.serviceUrl.default=http://<eureka_replica_ip>:<eureka_replica_port>/eureka/v2/" estuaryoss/netflix-eureka:1.9.26
```

Example:
```shell script
docker run -d -p 8080:8080 -e JAVA_OPTS="-Deureka.serviceUrl.default=http://10.10.10.2:8080/eureka/v2/" estuaryoss/netflix-eureka:1.9.26
```

For multiple eureka servers replication, separate them with comma.

## Browser access
```shell script
curl -i http://localhost:8080/eureka  
```

## Eureka register endpoint
```shell script
curl -i http://localhost:8080/eureka/v2 
``` 

## About versions
Tomcat: 9.0.26
