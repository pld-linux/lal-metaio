Summary:	LAL wrapping of the MetaIO LIGO_LW XML library
Summary(pl.UTF-8):	Obudowanie LAL do biblioteki MetaIO LILO_LW XML
Name:		lal-metaio
Version:	1.3.1
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://software.ligo.org/lscsoft/source/lalsuite/lalmetaio-%{version}.tar.xz
# Source0-md5:	5222898eebfc05dbddeba2d63c64d336
Patch0:		%{name}-env.patch
URL:		https://wiki.ligo.org/DASWG/LALSuite
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	lal-devel >= 6.18.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	metaio-devel
BuildRequires:	octave-devel >= 1:3.2.0
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	python-numpy-devel >= 1:1.7
BuildRequires:	swig >= 3.0.12
BuildRequires:	swig-python >= 2.0.12
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	lal >= 6.18.0
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
Requires:	lal-devel >= 6.18.0
Requires:	metaio-devel

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
Requires:	octave-lal >= 6.18.0

%description -n octave-lalmetaio
Octave interface for LAL MetaIO.

%description -n octave-lalmetaio -l pl.UTF-8
Interfejs Octave do biblioteki LAL MetaIO.

%package -n python-lalmetaio
Summary:	Python bindings for LAL MetaIO
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki LAL MetaIO
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-lal >= 6.18.0
Requires:	python-modules >= 1:2.6

%description -n python-lalmetaio
Python bindings for LAL MetaIO.

%description -n python-lalmetaio -l pl.UTF-8
Wiązania Pythona do biblioteki LAL MetaIO.

%prep
%setup -q -n lalmetaio-%{version}
%patch0 -p1

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

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/lalmetaio_version
%attr(755,root,root) %{_libdir}/liblalmetaio.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblalmetaio.so.5
/etc/shrc.d/lalmetaio-user-env.csh
/etc/shrc.d/lalmetaio-user-env.fish
/etc/shrc.d/lalmetaio-user-env.sh

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

%files -n python-lalmetaio
%defattr(644,root,root,755)
%dir %{py_sitedir}/lalmetaio
%attr(755,root,root) %{py_sitedir}/lalmetaio/_lalmetaio.so
%{py_sitedir}/lalmetaio/*.py[co]
