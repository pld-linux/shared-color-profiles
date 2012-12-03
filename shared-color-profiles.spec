# NOTE: building profiles takes a lot of time and RAM
#	requires system dbus running to build
Summary:	Shared color profiles to be used in color management aware applications
Summary(pl.UTF-8):	Współdzielone profile kolorów dla aplikacji obsługujących zarządzanie kolorami
Name:		shared-color-profiles
Version:	0.1.6
Release:	1
License:	Free (Public Domain, CC-BY-SA, CC-BY-ND, zlib, MIT - depending on profile)
Group:		Libraries
Source0:	http://people.freedesktop.org/~hughsient/releases/%{name}-%{version}.tar.xz
# Source0-md5:	f81b3316a3052a99784d01205425be88
URL:		http://github.com/hughsie/shared-color-profiles
BuildRequires:	argyllcms
BuildRequires:	colord
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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

%build
%configure
# colprof hogs so much memory during build we need to disable parallel build
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL="install -p" \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_datadir}/color/icc/AdobeGammaTest.icm
%{_datadir}/color/icc/AdobeRGB1998.icc
%{_datadir}/color/icc/AppleRGB.icc
%{_datadir}/color/icc/BestRGB.icc
%{_datadir}/color/icc/BetaRGB.icc
%{_datadir}/color/icc/BruceRGB.icc
%{_datadir}/color/icc/CIE-RGB.icc
%{_datadir}/color/icc/ColorMatchRGB.icc
%{_datadir}/color/icc/DonRGB4.icc
%{_datadir}/color/icc/ECI-RGBv2.icc
%{_datadir}/color/icc/EktaSpacePS5.icc
%{_datadir}/color/icc/FOGRA27L_coated.icc
%{_datadir}/color/icc/FOGRA28L_webcoated.icc
%{_datadir}/color/icc/FOGRA29L_uncoated.icc
%{_datadir}/color/icc/FOGRA30L_uncoated_yellowish.icc
%{_datadir}/color/icc/FOGRA39L_coated.icc
%{_datadir}/color/icc/FOGRA40L_SC_paper.icc
%{_datadir}/color/icc/FakeBRG.icc
%{_datadir}/color/icc/FakeRBG.icc
%{_datadir}/color/icc/GRACoL_TR006_coated.icc
%{_datadir}/color/icc/ISOnewspaper26.icc
%{_datadir}/color/icc/NTSC-RGB.icc
%{_datadir}/color/icc/PAL-RGB.icc
%{_datadir}/color/icc/ProPhotoRGB.icc
%{_datadir}/color/icc/SMPTE-C-RGB.icc
%{_datadir}/color/icc/SNAP_TR002_newsprint.icc
%{_datadir}/color/icc/SWOP_TR003_coated_3.icc
%{_datadir}/color/icc/SWOP_TR005_coated_5.icc
%{_datadir}/color/icc/WideGamutRGB.icc
%{_datadir}/color/icc/bluish.icc
%{_datadir}/color/icc/crayons.icc
%{_datadir}/color/icc/sRGB.icc
%{_datadir}/color/icc/x11-colors.icc
%{_datadir}/color/icc/Oysonar
%{_datadir}/color/icc/Yamma
%{_datadir}/shared-color-profiles
