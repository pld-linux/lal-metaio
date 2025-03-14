Summary:	LAL wrapping of the MetaIO LIGO_LW XML library
Summary(pl.UTF-8):	Obudowanie LAL do biblioteki MetaIO LILO_LW XML
Name:		lal-metaio
Version:	4.0.4
Release:	3
License:	GPL v2+
Group:		Libraries
Source0:	http://software.igwn.org/lscsoft/source/lalsuite/lalmetaio-%{version}.tar.xz
# Source0-md5:	ed22d14d02e7ed5b846a62826b44866b
Patch0:		%{name}-env.patch
URL:		https://wiki.ligo.org/Computing/LALSuite
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	help2man >= 1.37
BuildRequires:	lal-devel >= 7.5.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	metaio-devel >= 8.4.0
BuildRequires:	octave-devel >= 1:3.2.0
BuildRequires:	pkgconfig
BuildRequires:	python3-devel >= 1:3.5
BuildRequires:	python3-numpy-devel >= 1:1.7
BuildRequires:	swig >= 4.1.0
BuildRequires:	swig-python >= 3.0.11
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	lal >= 7.5.0
Requires:	metaio >= 8.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LAL wrapping of the MetaIO LIGO_LW XML library.

%description -l pl.UTF-8
Obudowanie LAL do biblioteki MetaIO LILO_LW XML.

%package devel
Summary:	Header files for lal-metaio library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki lal-metaio
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	lal-devel >= 7.2.2
Requires:	metaio-devel >= 8.4.0

%description devel
Header files for lal-metaio library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki lal-metaio.

%package static
Summary:	Static lal-metaio library
Summary(pl.UTF-8):	Statyczna biblioteka lal-metaio
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static lal-metaio library.

%description static -l pl.UTF-8
Statyczna biblioteka lal-metaio.

%package -n octave-lalmetaio
Summary:	Octave interface for LAL MetaIO
Summary(pl.UTF-8):	Interfejs Octave do biblioteki LAL MetaIO
Group:		Applications/Math
Requires:	%{name} = %{version}-%{release}
Requires:	octave-lal >= 7.5.0

%description -n octave-lalmetaio
Octave interface for LAL MetaIO.

%description -n octave-lalmetaio -l pl.UTF-8
Interfejs Octave do biblioteki LAL MetaIO.

%package -n python3-lalmetaio
Summary:	Python bindings for LAL MetaIO
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki LAL MetaIO
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python3-lal >= 7.5.0
Requires:	python3-modules >= 1:3.5
Obsoletes:	python-lalmetaio < 2

%description -n python3-lalmetaio
Python bindings for LAL MetaIO.

%description -n python3-lalmetaio -l pl.UTF-8
Wiązania Pythona do biblioteki LAL MetaIO.

%prep
%setup -q -n lalmetaio-%{version}
%patch -P 0 -p1

%build
%{__libtoolize}
%{__aclocal} -I gnuscripts
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-swig
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/liblalmetaio.la

install -d $RPM_BUILD_ROOT/etc/shrc.d
%{__mv} $RPM_BUILD_ROOT%{_sysconfdir}/*sh $RPM_BUILD_ROOT/etc/shrc.d

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README.md
%attr(755,root,root) %{_bindir}/lalmetaio_version
%attr(755,root,root) %{_libdir}/liblalmetaio.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblalmetaio.so.11
/etc/shrc.d/lalmetaio-user-env.csh
/etc/shrc.d/lalmetaio-user-env.fish
/etc/shrc.d/lalmetaio-user-env.sh
%{_mandir}/man1/lalmetaio_version.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblalmetaio.so
%{_includedir}/lal/LALMetaIO*.h
%{_includedir}/lal/LIGOLwXML*.h*
%{_includedir}/lal/LIGOMetadata*.h
%{_includedir}/lal/SWIGLALMetaIO*.h
%{_includedir}/lal/SWIGLALMetaIO*.i
%{_includedir}/lal/swiglalmetaio.i
%{_pkgconfigdir}/lalmetaio.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/liblalmetaio.a

%files -n octave-lalmetaio
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/octave/*/site/oct/*/lalmetaio.oct

%files -n python3-lalmetaio
%defattr(644,root,root,755)
%dir %{py3_sitedir}/lalmetaio
%attr(755,root,root) %{py3_sitedir}/lalmetaio/_lalmetaio.so
%{py3_sitedir}/lalmetaio/*.py
%{py3_sitedir}/lalmetaio/__pycache__
