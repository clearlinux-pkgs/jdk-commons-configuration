Name     : jdk-commons-configuration
Version  : 1.6
Release  : 4
URL      : https://repo1.maven.org/maven2/commons-configuration/commons-configuration/1.6/commons-configuration-1.6.jar
Source0  : https://repo1.maven.org/maven2/commons-configuration/commons-configuration/1.6/commons-configuration-1.6.jar
Source1  : https://repo1.maven.org/maven2/commons-configuration/commons-configuration/1.6/commons-configuration-1.6.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: jdk-commons-configuration-data
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%package data
Summary: data components for the jdk-commons-configuration package.
Group: Data

%description data
data components for the jdk-commons-configuration package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/commons-configuration.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/commons-configuration.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/commons-configuration.xml \
%{buildroot}/usr/share/maven-poms/commons-configuration.pom \
%{buildroot}/usr/share/java/commons-configuration.jar \

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/commons-configuration.jar
/usr/share/maven-metadata/commons-configuration.xml
/usr/share/maven-poms/commons-configuration.pom
