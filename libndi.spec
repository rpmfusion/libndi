%global commit0 c14b40caafb26a02249f062e7f907ceaa53c1b74
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           libndi
Version:        0.0.1
Release:        7.git%{?shortcommit0}%{?dist}
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
* Wed Mar 01 2023 Leigh Scott <leigh123linux@gmail.com> - 0.0.1-7.gitc14b40c
- Rebuild for new ffmpeg

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.0.1-6.gitc14b40c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.0.1-5.gitc14b40c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov 11 2021 Leigh Scott <leigh123linux@gmail.com> - 0.0.1-4.gitc14b40c
- Rebuilt for new ffmpeg snapshot

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.0.1-3.gitc14b40c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 24 2021 Nicolas Chauvet <kwizart@gmail.com> - 0.0.1-2.gitc14b40c
- Initial spec file
