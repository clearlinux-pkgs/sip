#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sip
Version  : 4.19.20
Release  : 23
URL      : https://www.riverbankcomputing.com/static/Downloads/sip/4.19.20/sip-4.19.20.tar.gz
Source0  : https://www.riverbankcomputing.com/static/Downloads/sip/4.19.20/sip-4.19.20.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: sip-bin = %{version}-%{release}
Requires: sip-license = %{version}-%{release}
Requires: sip-python = %{version}-%{release}
Requires: sip-python3 = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : qscintilla
BuildRequires : qscintilla-dev
Patch1: 0001-Add-configure-to-generate-Makefile.patch

%description
SIP - C/C++ Bindings Generator for Python v2 and v3
===================================================

%package bin
Summary: bin components for the sip package.
Group: Binaries
Requires: sip-license = %{version}-%{release}

%description bin
bin components for the sip package.


%package dev
Summary: dev components for the sip package.
Group: Development
Requires: sip-bin = %{version}-%{release}
Provides: sip-devel = %{version}-%{release}
Requires: sip = %{version}-%{release}

%description dev
dev components for the sip package.


%package license
Summary: license components for the sip package.
Group: Default

%description license
license components for the sip package.


%package python
Summary: python components for the sip package.
Group: Default
Requires: sip-python3 = %{version}-%{release}

%description python
python components for the sip package.


%package python3
Summary: python3 components for the sip package.
Group: Default
Requires: python3-core

%description python3
python3 components for the sip package.


%prep
%setup -q -n sip-4.19.20
cd %{_builddir}/sip-4.19.20
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1608007982
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1608007982
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sip
cp %{_builddir}/sip-4.19.20/LICENSE-GPL2 %{buildroot}/usr/share/package-licenses/sip/2136dbc93e95a70deae070e44ff6b2702ec1599c
cp %{_builddir}/sip-4.19.20/LICENSE-GPL3 %{buildroot}/usr/share/package-licenses/sip/34e9b06e7f12eaed676f57481de931ec91c6ce0a
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sip

%files dev
%defattr(-,root,root,-)
/usr/include/python3.9/sip.h

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sip/2136dbc93e95a70deae070e44ff6b2702ec1599c
/usr/share/package-licenses/sip/34e9b06e7f12eaed676f57481de931ec91c6ce0a

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
