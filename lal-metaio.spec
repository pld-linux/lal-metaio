Summary:	LAL wrapping of the MetaIO LIGO_LW XML library
Name:		lal-metaio
Version:	1.0.0
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	https://www.lsc-group.phys.uwm.edu/daswg/download/software/source/lalsuite/lalmetaio-%{version}.tar.gz
# Source0-md5:	554a8fcb9dbb75dc6e31d96ee00bf88f
URL:		https://www.lsc-group.phys.uwm.edu/daswg/projects/lalsuite.html
BuildRequires:	lal-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LAL wrapping of the MetaIO LIGO_LW XML library.

%package devel
Summary:	Header files for lal-metaio library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for lal-metaio library.

%package static
Summary:	Static lal-metaio library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static lal-metaio library.

%prep
%setup -q -n lalmetaio-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/shrc.d
mv $RPM_BUILD_ROOT%{_sysconfdir}/*sh $RPM_BUILD_ROOT/etc/shrc.d

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
/etc/shrc.d/lalmetaio-user-env*

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/lal/*
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
