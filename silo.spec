Summary:	The SILO boot loader for SPARCs
Summary(fr):	Chargeur de boot Linux pour SPARCs
Name:		silo
Version:	0.9.9
Release:	3
License:	GPL
Group:		Base
Group(pl):	Podstawowe
Source0:	ftp://sunsite.mff.cuni.cz/OS/Linux/Sparc/local/%{name}%{name}-%{version}.tgz
ExclusiveArch:	sparc sparc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
The silo package installs the SILO (Sparc Improved LOader) boot
loader, which you'll need to boot Red Hat Linux on a SPARC. SILO
installs onto your system's boot block and can be configured to boot
Linux, Solaris and SunOS.

%description -l fr
Le paquetage silo installe le chargeur de boot SILO (Sparc Improved
LOader) dont vous avez besoin pour démarrer Linux-Mandrake sur une
SPARC. SILO s'installe sur le "boot block" de votre système et peut
être configuré pour démarrer Linux, Solaris et SunOS.

%prep 
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{boot,sbin,usr%{_sbindir},%{_mandir}/man{5,8}}

install boot/first.b $RPM_BUILD_ROOT/boot/first.b
install boot/ultra.b $RPM_BUILD_ROOT/boot/ultra.b
install boot/cd.b $RPM_BUILD_ROOT/boot/cd.b
install boot/fd.b $RPM_BUILD_ROOT/boot/fd.b
install boot/second.b $RPM_BUILD_ROOT/boot/second.b
install boot/silotftp.b $RPM_BUILD_ROOT/boot/silotftp.b

install sbin/silo $RPM_BUILD_ROOT%{_sbindir}/silo
install misc/silocheck $RPM_BUILD_ROOT%{_sbindir}/silocheck

install man/silo.conf.5 $RPM_BUILD_ROOT%{_mandir}/man5
install man/silo.8 $RPM_BUILD_ROOT%{_mandir}/man8

gzip -9nf docs/* ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /etc/silo.conf ]; then
	/sbin/silo >& /dev/null
fi

%files
%defattr(644,root,root,755)
%doc docs/*.gz *.gz
/boot/first.b
/boot/ultra.b
/boot/cd.b
/boot/fd.b
/boot/silotftp.b
/boot/second.b
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man[58]/*
