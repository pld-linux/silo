Summary:	The SILO boot loader for SPARCs.
Name:		silo
Version:	0.8.6
Release:	2
License:	GPL
ExclusiveArch:	sparc sparc64
Group:		Base
Group(pl):	Podstawowe
Source0:	ftp://sunsite.mff.cuni.cz/pub/silo/%{name}-%{version}.tgz
Patch1:		%{name}-0.7.2-bootfile.patch
Patch2:		%{name}-0.7.3-noromfs.patch

BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The silo package installs the SILO (Sparc Improved LOader) boot
loader, which you'll need to boot Red Hat Linux on a SPARC. SILO
installs onto your system's boot block and can be configured to boot
Linux, Solaris and SunOS.

%prep 
%setup -q -n silo-0.8.6
%patch1 -p1 -b .bootfile
#%patch2 -p1 -b .noromfs

%build
#make CC="gcc -DNO_ROMFS"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{boot,sbin,usr/sbin,usr/man/man8}

install -m755 sbin/silo		$RPM_BUILD_ROOT/sbin/silo
install boot/first.b	$RPM_BUILD_ROOT/boot/first.b
install boot/ultra.b	$RPM_BUILD_ROOT/boot/ultra.b
install boot/cd.b		$RPM_BUILD_ROOT/boot/cd.b
install boot/fd.b		$RPM_BUILD_ROOT/boot/fd.b
install boot/second.b	$RPM_BUILD_ROOT/boot/second.b
install boot/silotftp.b	$RPM_BUILD_ROOT/boot/silotftp.b
install -m755 misc/silocheck $RPM_BUILD_ROOT%{_sbindir}/silocheck
install man/silo.8 $RPM_BUILD_ROOT%{_mandir}/man8/silo.8

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /etc/silo.conf ]; then
	/sbin/silo >& /dev/null
fi

%files
%defattr(644,root,root,755)
%doc docs COPYING ChangeLog
/sbin/silo
/boot/first.b
/boot/ultra.b
/boot/cd.b
/boot/fd.b
/boot/silotftp.b
/boot/second.b
%attr(755,root,root) %{_sbindir}/silocheck
%{_mandir}/man8
