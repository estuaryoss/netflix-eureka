FROM tomcat:9.0.26-jdk8-openjdk
MAINTAINER Catalin Dinuta <constantin.dinuta@gmail.com>

ENV EUREKA_VERSION 1.9.14

RUN cd $CATALINA_HOME/webapps &&\
  mkdir eureka &&\
  cd eureka &&\
  wget -q http://repo1.maven.org/maven2/com/netflix/eureka/eureka-server/$EUREKA_VERSION/eureka-server-$EUREKA_VERSION.war &&\
  jar xf eureka-server-$EUREKA_VERSION.war &&\
  rm eureka-server-$EUREKA_VERSION.war

ADD config.properties $CATALINA_HOME/webapps/eureka/WEB-INF/classes/config.properties
ADD eureka-client.properties $CATALINA_HOME/webapps/eureka/WEB-INF/classes/eureka-client.properties
ADD eureka-server.properties $CATALINA_HOME/webapps/eureka/WEB-INF/classes/eureka-server.properties

EXPOSE 8080

CMD ["catalina.sh", "run"]
