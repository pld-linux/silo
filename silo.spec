Summary:	The SILO boot loader for SPARCs
Summary(fr):	Chargeur de boot Linux pour SPARCs
Summary(pl):	SILO - boot loader dla maszyn sparcowych
Name:		silo
Version:	1.4.13
Release:	2
License:	GPL
Group:		Base
Source0:	http://www.sparc-boot.org/pub/silo/%{name}-%{version}.tar.bz2
# Source0-md5:	7039aabf3c1b3858ae8d0ccdde21343e
Patch0:		%{name}-sh.patch
URL:		http://www.sparc-boot.org/
BuildRequires:	e2fsprogs-static
BuildRequires:	elftoaout
ExclusiveArch:	sparc sparc64 sparcv9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The silo package installs the SILO (Sparc Improved LOader) boot
loader, which you'll need to boot PLD Linux on a SPARC. SILO installs
onto your system's boot block and can be configured to boot Linux,
Solaris and SunOS.

%description -l fr
Le paquetage silo installe le chargeur de boot SILO (Sparc Improved
LOader) dont vous avez besoin pour démarrer Linux-Mandrake sur une
SPARC. SILO s'installe sur le "boot block" de votre système et peut
être configuré pour démarrer Linux, Solaris et SunOS.

%description -l pl
Pakiet zawiera SILO (Sparc Improved LOader), ktory jest niezbêdny do
uruchomienia PLD Linuksa na SPARCu. SILO instaluje siê w bloku
bootuj±cym systemu i mo¿e byæ skonfigurowany tak, aby ³adowa³ Linuksa,
Solarisa lub SunOSa.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc} -m32"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	 DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /etc/silo.conf ]; then
	/sbin/silo -f > /dev/null 2>&1
fi

%files
%defattr(644,root,root,755)
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf
%doc docs/* first-isofs/README.SILO_ISOFS
/boot/*.b
%attr(755,root,root) /sbin/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man[158]/*
