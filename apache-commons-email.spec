%{?_javapackages_macros:%_javapackages_macros}
%global short_name      commons-email

Name:             apache-%{short_name}
Version:          1.3.1
Release:          7%{?dist}
Summary:          Apache Commons Email Package
License:          ASL 2.0
URL:              http://commons.apache.org/proper/%{short_name}/
BuildArch:        noarch

Source0:          http://archive.apache.org/dist/commons/email/source/%{short_name}-%{version}-src.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(javax.mail:mail)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-release-plugin)
#BuildRequires:  mvn(org.apache.maven.plugins:maven-scm-publish-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-site-plugin)
BuildRequires:  mvn(org.easymock:easymock)
BuildRequires:  mvn(org.slf4j:slf4j-jdk14)

%description
Commons-Email aims to provide an API for sending email. It is built on top of 
the JavaMail API, which it aims to simplify.

%package javadoc
Summary:          Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{short_name}-%{version}-src

# Activation is now provided by the JRE
%pom_remove_dep "javax.activation:activation"

# Some test deps are not in fedora
%pom_remove_dep "org.subethamail:subethasmtp"
%pom_remove_dep "org.powermock:"

# Compatibility links
%mvn_alias "org.apache.commons:commons-email" "commons-email:commons-email"
%mvn_file :commons-email %{short_name} %{name}

%build
# Skip tests due to some missing deps
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt RELEASE-NOTES.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.1-6
- Regenerate build-requires

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.3.1-2
- Use Requires: java-headless rebuild (#1067528)
- Rely on automatic requires

* Wed Jul 31 2013 Mat Booth <fedora@matbooth.co.uk> - 1.3.1-1
- Update to latest upstream, rhbz #975516
- Remove activation dep from pom, rhbz #820963
- Adapt for current packaging guidelines

* Tue Feb 19 2013 Mat Booth <fedora@matbooth.co.uk> - 1.2-5
- Add missing BuildRequires on maven-local

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Apr 16 2011 Chris Spike <spike@fedoraproject.org> 1.2-1
- Initial version of the package
