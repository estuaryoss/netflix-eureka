FROM tomcat:9.0.26-jdk8-openjdk
MAINTAINER Catalin Dinuta <constantin.dinuta@gmail.com>

RUN cd $CATALINA_HOME/webapps &&\
  mkdir eureka &&\
  cd eureka &&\
  wget -q http://repo1.maven.org/maven2/com/netflix/eureka/eureka-server/1.9.13/eureka-server-1.9.13.war &&\
  jar xf eureka-server-1.9.13.war &&\
  rm eureka-server-1.9.13.war

ADD config.properties $CATALINA_HOME/webapps/eureka/WEB-INF/classes/config.properties
#ADD eureka-client.properties $CATALINA_HOME/webapps/eureka/WEB-INF/classes/eureka-client.properties
ADD eureka-server.properties $CATALINA_HOME/webapps/eureka/WEB-INF/classes/eureka-server.properties

EXPOSE 8080

CMD ["catalina.sh", "run"]
