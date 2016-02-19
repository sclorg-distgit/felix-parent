%global pkg_name felix-parent
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        1.2.1
Release:        15.11%{?dist}
Summary:        Parent POM file for Apache Felix Specs

License:        ASL 2.0
URL:            http://felix.apache.org/
#svn export http://svn.apache.org/repos/asf/felix/releases/felix-parent-1.2.1/
#tar -jcf felix-parent-1.2.1.tar.bz2 felix-parent-1.2.1/
Source0:        %{pkg_name}-%{version}.tar.bz2
#Remove mockito-all dependency which is not in koji
Patch0:        %{pkg_name}-%{version}-pom.patch

BuildArch: noarch

BuildRequires: %{?scl_prefix_java_common}javapackages-tools
BuildRequires: %{?scl_prefix_java_common}junit
BuildRequires: %{?scl_prefix_java_common}maven-local
BuildRequires: %{?scl_prefix_java_common}easymock2
BuildRequires: maven30-maven-plugin-plugin
BuildRequires: maven30-maven-compiler-plugin
BuildRequires: maven30-maven-install-plugin
BuildRequires: maven30-maven-jar-plugin
BuildRequires: maven30-maven-javadoc-plugin
BuildRequires: maven30-maven-resources-plugin
BuildRequires: maven30-maven-assembly-plugin
BuildRequires: maven30-maven-source-plugin
BuildRequires: maven30-maven-deploy-plugin
BuildRequires: maven30-maven-gpg-plugin
BuildRequires: maven30-maven-project-info-reports-plugin
BuildRequires: maven30-maven-release-plugin
BuildRequires: maven30-maven-surefire-plugin
BuildRequires: maven30-maven-surefire-report-plugin
BuildRequires: maven30-maven-plugin-build-helper
BuildRequires: maven30-maven-plugin-jxr

Requires: %{?scl_prefix_java_common}junit
Requires: %{?scl_prefix_java_common}easymock2
Requires: maven30-maven
Requires: maven30-maven-plugin-plugin
Requires: maven30-maven-compiler-plugin
Requires: maven30-maven-install-plugin
Requires: maven30-maven-jar-plugin
Requires: maven30-maven-javadoc-plugin
Requires: maven30-maven-resources-plugin
Requires: maven30-maven-assembly-plugin
Requires: maven30-maven-source-plugin
Requires: maven30-maven-deploy-plugin
Requires: maven30-maven-gpg-plugin
Requires: maven30-maven-project-info-reports-plugin
Requires: maven30-maven-release-plugin
Requires: maven30-maven-surefire-plugin
Requires: maven30-maven-surefire-report-plugin
Requires: maven30-maven-plugin-build-helper
Requires: maven30-maven-plugin-jxr


%description
Parent POM file for Apache Felix Specs.

%prep
%setup -q -n %{pkg_name}-%{version}
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%patch0 -p0 -b .sav
%pom_remove_plugin org.apache.maven.plugins:maven-site-plugin

# legacy depmap (some upstream packages haven't caught up with the
# "felix" -> "felix-parent" rename yet)
%mvn_alias : :felix
%{?scl:EOF}

%build
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%dir %{_mavenpomdir}/%{pkg_name}
%doc LICENSE NOTICE


%changelog
* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 1.2.1-15.11
- maven33 rebuild

* Thu Jan 15 2015 Michal Srb <msrb@redhat.com> - 1.2.1-15.10
- Fix directory ownership

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.2.1-15.9
- Mass rebuild 2015-01-13

* Mon Jan 12 2015 Michael Simacek <msimacek@redhat.com> - 1.2.1-15.8
- BR/R on packages from rh-java-common

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1.2.1-15.7
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.1-15.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.1-15.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.1-15.4
- Mass rebuild 2014-02-18

* Fri Feb 14 2014 Michael Simacek <msimacek@redhat.com> - 1.2.1-15.3
- SCL-ize BR

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.1-15.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.1-15.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.2.1-15
- Mass rebuild 2013-12-27

* Tue Jul 16 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.1-14
- Fix Maven alias

* Mon Jul 15 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.1-13
- Remove unneeded depmap file

* Mon Jul 15 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.1-12
- Update to current packaging guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.2.1-10
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Dec 18 2012 Michal Srb <msrb@redhat.com> - 1.2.1-9
- Removed dependency on maven-site-plugin

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Mar 30 2011 Alexander Kurtakov <akurtako@redhat.com> 1.2.1-6
- Fix faulty compiler plugin settings setting source but not target.

* Sun Mar 13 2011 Mat Booth <fedora@matbooth.co.uk> 1.2.1-5
- Add dep on maven-plugin-jxr.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 27 2010 Mat Booth <fedora@matbooth.co.uk> - 1.2.1-3
- Add legacy depmap from maven2-common-poms for felix packages that still
  specify "felix" instead of "felix-parent"

* Tue Jul 20 2010 Hui Wang <huwang@redhat.com> - 1.2.1-2
- Update summary and description
- Add comment in mvn-jpp

* Fri Jul 16 2010 Hui Wang <huwang@redhat.com> - 1.2.1-1
- Initial version of the package
