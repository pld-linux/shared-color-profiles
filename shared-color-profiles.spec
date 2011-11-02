Summary:	Shared color profiles to be used in color management aware applications
Summary(pl.UTF-8):	Współdzielone profile kolorów dla aplikacji obsługujących zarządzanie kolorami
Name:		shared-color-profiles
Version:	0.1.5
Release:	1
License:	Free (Public Domain, CC-BY-SA, CC-BY-ND, zlib, MIT - depending on profile)
Group:		Libraries
Source0:	http://people.freedesktop.org/~hughsient/releases/%{name}-%{version}.tar.gz
# Source0-md5:	65501b1376825b350b3deca97bbbf652
URL:		http://github.com/hughsie/shared-color-profiles
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains various profiles which are useful for programs
that are color management aware.

%description -l pl.UTF-8
Ten pakiet zawiera różne profile, przydatne dla programów
obsługujących zarządzanie kolorami.

%prep
%setup -q

cp -p profiles/Argyll/LICENSE LICENSE.Argyll
cp -p profiles/Argyll/README README.Argyll
cp -p profiles/Oysonar/LICENSE LICENSE.Oysonar
cp -p profiles/Oysonar/README README.Oysonar
cp -p profiles/Yamma/LICENSE LICENSE.Yamma
cp -p profiles/Yamma/README README.Yamma

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
%doc AUTHORS LICENSE.* NEWS README*
%{_datadir}/color/icc/AdobeGammaTest.icm
%{_datadir}/color/icc/Argyll
%{_datadir}/color/icc/FakeBRG.icc
%{_datadir}/color/icc/FakeRBG.icc
%{_datadir}/color/icc/Fogra27L.icc
%{_datadir}/color/icc/Oysonar
%{_datadir}/color/icc/Yamma
%{_datadir}/color/icc/bluish.icc
%{_datadir}/shared-color-profiles
