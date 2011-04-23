Summary:	Shared color profiles to be used in color management aware applications
Name:		shared-color-profiles
Version:	0.1.4
Release:	1
License:	GPL v2+ and Public Domain and zlib and MIT
Group:		Libraries
Source0:	http://people.freedesktop.org/~hughsient/releases/%{name}-%{version}.tar.gz
# Source0-md5:	cec4038c757ac7d23c573888d8d2fa77
URL:		http://github.com/hughsie/shared-color-profiles
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains various profiles which are useful for programs
that are color management aware.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%{_datadir}/color/icc/AdobeGammaTest.icm
%{_datadir}/color/icc/Argyll
%{_datadir}/color/icc/Fogra27L.icc
%{_datadir}/color/icc/Oysonar
%{_datadir}/color/icc/Yamma
%{_datadir}/color/icc/bluish.icc
%{_datadir}/shared-color-profiles
