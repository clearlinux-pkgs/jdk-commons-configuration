PKG_NAME := jdk-commons-configuration
URL := https://repo1.maven.org/maven2/commons-configuration/commons-configuration/1.6/commons-configuration-1.6.jar
ARCHIVES := https://repo1.maven.org/maven2/commons-configuration/commons-configuration/1.6/commons-configuration-1.6.pom %{buildroot}

include ../common/Makefile.common
