Summary: The SILO boot loader for SPARCs.
Name: silo
Version: 0.8.6
Release: 2
Copyright: GPL
ExclusiveArch: sparc sparc64
Group: System Environment/Base
Source: ftp://sunsite.mff.cuni.cz/pub/silo/silo-0.8.6.tgz
Patch1: silo-0.7.2-bootfile.patch
Patch2: silo-0.7.3-noromfs.patch

BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The silo package installs the SILO (Sparc Improved LOader) boot loader,
which you'll need to boot Red Hat Linux on a SPARC.  SILO installs onto
your system's boot block and can be configured to boot Linux, Solaris
and SunOS.

%prep 
%setup -q -n silo-0.8.6
%patch1 -p1 -b .bootfile
#%patch2 -p1 -b .noromfs

%build
#make CC="gcc -DNO_ROMFS"

make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{boot,sbin,usr/sbin,usr/man/man8}

install -m755 sbin/silo		$RPM_BUILD_ROOT/sbin/silo
install -m644 boot/first.b	$RPM_BUILD_ROOT/boot/first.b
install -m644 boot/ultra.b	$RPM_BUILD_ROOT/boot/ultra.b
install -m644 boot/cd.b		$RPM_BUILD_ROOT/boot/cd.b
install -m644 boot/fd.b		$RPM_BUILD_ROOT/boot/fd.b
install -m644 boot/second.b	$RPM_BUILD_ROOT/boot/second.b
install -m644 boot/silotftp.b	$RPM_BUILD_ROOT/boot/silotftp.b
install -m755 misc/silocheck	$RPM_BUILD_ROOT/usr/sbin/silocheck
install -m644 man/silo.8	$RPM_BUILD_ROOT/usr/man/man8/silo.8

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /etc/silo.conf ]; then
	/sbin/silo >& /dev/null
fi

%files
%defattr(-,root,root)
%doc docs COPYING ChangeLog
/sbin/silo
/boot/first.b
/boot/ultra.b
/boot/cd.b
/boot/fd.b
/boot/silotftp.b
/boot/second.b
/usr/sbin/silocheck
/usr/man/man8
