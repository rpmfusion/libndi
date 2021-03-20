%global commit0 c14b40caafb26a02249f062e7f907ceaa53c1b74
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           libndi
Version:        0.0.1
Release:        2.git%{?shortcommit0}%{?dist}
Summary:        Open-source library done to interact with NDI streams

License:        LGPLv2+
URL:            https://code.videolan.org/jbk/libndi
Source0:        %{url}/-/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  cmake

BuildRequires:  ffmpeg-devel
BuildRequires:  pkgconfig(microdns)


%description
The goal of this project is to provide a way to interact with NDI streams,
without requiring to use a non-open-source SDK, and targetting numerous
platforms.  The library is now at an alpha level of quality, do not use
in production.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        utils
Summary:        Utility for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    utils
The %{name}-utils package contains utilities for %{name}.


%prep
%autosetup -p1 -n %{name}-%{commit0}


%build
%meson
%meson_build


%install
%meson_install


%{?ldconfig_scriptlets}


%files
%license COPYING
%doc NEWS README.md
%{_libdir}/libndi.so.0*

%files devel
%{_includedir}/libndi.h
%{_libdir}/libndi.so

%files utils
%{_bindir}/ndi


%changelog
* Wed Feb 24 2021 Nicolas Chauvet <kwizart@gmail.com> - 0.0.1-2.gitc14b40c
- Initial spec file
