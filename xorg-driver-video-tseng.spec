Summary:	X.org video driver for Tseng Labs video adapters
Summary(pl.UTF-8):	Sterownik obrazu X.org dla kart graficznych Tseng Labs
Name:		xorg-driver-video-tseng
Version:	1.1.1
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-tseng-%{version}.tar.bz2
# Source0-md5:	488aa9c3ec7a95e6589afa4b50bec8b4
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
BuildRequires:  rpmbuild(macros) >= 1.389
%requires_xorg_xserver_videodrv
Requires:	xorg-xserver-server >= 1.0.99.901
Obsoletes:	X11-driver-tseng < 1:7.0.0
Obsoletes:	XFree86-Tseng
Obsoletes:	XFree86-W32
Obsoletes:	XFree86-driver-tseng < 1:7.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for Tseng Labs video adapters.

%description -l pl.UTF-8
Sterownik obrazu X.org dla kart graficznych Tseng Labs.

%prep
%setup -q -n xf86-video-tseng-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/tseng_drv.so
%{_mandir}/man4/tseng.4*
