# TODO
# - take french bitstring.3 from fcron?
Summary:	Utility functions from BSD systems
Summary(pl.UTF-8):	Funkcje narzędziowe z systemów BSD
Name:		libbsd
Version:	0.8.3
Release:	1
License:	BSD, MIT (depending on part)
Group:		Libraries
Source0:	https://libbsd.freedesktop.org/releases/%{name}-%{version}.tar.xz
# Source0-md5:	e935c1bb6cc98a4a43cb1da22795493a
URL:		https://libbsd.freedesktop.org/
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library provides useful functions commonly found on BSD systems,
and lacking on others like GNU systems, thus making it easier to port
projects with strong BSD origins, without needing to embed the same
code over and over again on each project.

%description -l pl.UTF-8
Ta biblioteka udostępnia funkcje zwykle spotykane w systemach BSD, a
nie występujące na innych, takich jak systemy GNU. Dzięki temu ułatwia
portowanie projektów mających silne korzenie BSD bez potrzeby
osadzania ciągle tego samego kodu w każdym projekcie.

%package devel
Summary:	Header files for BSD library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki BSD
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Conflicts:	glibc-devel < 6:2.19

%description devel
Header files for BSD library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki BSD.

%package static
Summary:	Static BSD library
Summary(pl.UTF-8):	Statyczna biblioteka BSD
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Conflicts:	glibc-devel < 6:2.19

%description static
Static BSD library.

%description static -l pl.UTF-8
Statyczna biblioteka BSD.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libbsd.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README TODO
%attr(755,root,root) %{_libdir}/libbsd.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbsd.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbsd.so
%{_libdir}/libbsd-ctor.a
%{_includedir}/bsd
%{_pkgconfigdir}/libbsd.pc
%{_pkgconfigdir}/libbsd-ctor.pc
%{_pkgconfigdir}/libbsd-overlay.pc
%{_mandir}/man3/arc4random*.3*
%{_mandir}/man3/bitstring.3*
%{_mandir}/man3/closefrom.3*
%{_mandir}/man3/dehumanize_number.3*
%{_mandir}/man3/expand_number.3*
%{_mandir}/man3/explicit_bzero.3*
%{_mandir}/man3/fgetln.3*
%{_mandir}/man3/fgetwln.3*
%{_mandir}/man3/flopen.3*
%{_mandir}/man3/fmtcheck.3*
%{_mandir}/man3/fparseln.3*
%{_mandir}/man3/funopen.3*
%{_mandir}/man3/getbsize.3*
%{_mandir}/man3/getmode.3*
%{_mandir}/man3/getpeereid.3*
%{_mandir}/man3/getprogname.3*
%{_mandir}/man3/heapsort.3*
%{_mandir}/man3/humanize_number.3*
%{_mandir}/man3/md5.3bsd*
%{_mandir}/man3/mergesort.3*
%{_mandir}/man3/nlist.3*
%{_mandir}/man3/pidfile.3*
%{_mandir}/man3/queue.3bsd*
%{_mandir}/man3/radixsort.3*
%{_mandir}/man3/readpassphrase.3*
%{_mandir}/man3/reallocarray.3*
%{_mandir}/man3/reallocf.3*
%{_mandir}/man3/setmode.3*
%{_mandir}/man3/setproctitle.3*
%{_mandir}/man3/setprogname.3*
%{_mandir}/man3/sradixsort.3*
%{_mandir}/man3/stringlist.3*
%{_mandir}/man3/strlcat.3*
%{_mandir}/man3/strlcpy.3*
%{_mandir}/man3/strmode.3*
%{_mandir}/man3/strnstr.3*
%{_mandir}/man3/strtonum.3*
%{_mandir}/man3/tree.3*
%{_mandir}/man3/unvis.3*
%{_mandir}/man3/vis.3*
%{_mandir}/man3/wcslcat.3*
%{_mandir}/man3/wcslcpy.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libbsd.a
