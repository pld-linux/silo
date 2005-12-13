Summary:	The SILO boot loader for SPARCs
Summary(fr):	Chargeur de boot Linux pour SPARCs
Summary(pl):	SILO - boot loader dla maszyn sparcowych
Name:		silo
Version:	1.4.9
Release:	1
License:	GPL
Group:		Base
Source0:	http://www.sparc-boot.org/pub/silo/%{name}-%{version}.tar.bz2
# Source0-md5:	843d75dd79a436b73e161c7ece5af26b
Patch0:		%{name}-llh.patch
URL:		http://www.sparc-boot.org/
BuildRequires:	/bin/bash
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
LOader) dont vous avez besoin pour d�marrer Linux-Mandrake sur une
SPARC. SILO s'installe sur le "boot block" de votre syst�me et peut
�tre configur� pour d�marrer Linux, Solaris et SunOS.

%description -l pl
Pakiet zawiera SILO (Sparc Improved LOader), ktory jest niezb�dny do
uruchomienia PLD Linuksa na SPARCu. SILO instaluje si� w bloku
bootuj�cym systemu i mo�e by� skonfigurowany tak, aby �adowa� Linuksa,
Solarisa lub SunOSa.

%prep
%setup -q
%patch0 -p1

%build
# ksh doesn't expand '\340' in echo, which is required to make working *.b
# (first stage silently hangs otherwise)
%{__make} \
	SHELL=/bin/bash

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
%doc ChangeLog docs/* first-isofs/README.SILO_ISOFS
/boot/*.b
%attr(755,root,root) /sbin/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man[158]/*
