Summary:	The SILO boot loader for SPARCs
Summary(fr):	Chargeur de boot Linux pour SPARCs
Summary(pl):	SILO - boot loader dla maszyn sparcowych
Name:		silo
Version:	1.3
Release:	0.9
License:	GPL
Group:		Base
Source0:	http://www.sparc-boot.org/pub/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	8beb76021e952308550870c7f346f76e
URL:		http://www.sparc-boot.org/
ExclusiveArch:	sparc sparc64
BuildRequires:	e2fsprogs-static
BuildRequires:	glibc-static
BuildRequires:	elftoaout
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

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

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{boot,sbin,usr%{_sbindir},%{_mandir}/man{5,8}}

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /etc/silo.conf ]; then
	/sbin/silo > /dev/null 2>&1
fi

%files
%defattr(644,root,root,755)
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}.conf
%doc docs/* ChangeLog
/boot/*.b
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) /usr/bin/*
%attr(755,root,root) /usr/sbin/*
%{_mandir}/man[158]/*
