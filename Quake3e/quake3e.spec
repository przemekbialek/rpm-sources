%global commitdate 20260326
%global commithash 229a054fcd6cd87300713ca18e161380bbaf097e
%global shortcommit %(c=%{commithash}; echo ${c:0:7})
%define debug_package %{nil}
Name:           Quake3e
Version:        0~git%{commitdate}.%{shortcommit}
Release:        %{autorelease}
Summary:        Modern Quake III Arena engine
License:        GPLv2
URL:            https://github.com/ec-/Quake3e
Source:         %{url}/archive/%{commithash}/%{name}-%{shortcommit}.tar.gz
Source1:        quake3e.desktop

BuildRequires:  libXxf86dga-devel
BuildRequires:  libXxf86vm-devel
BuildRequires:  libXrandr-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  sdl2-compat-devel
BuildRequires:  libcurl-devel
BuildRequires:  make
BuildRequires:  gcc

%description
This is a modern Quake III Arena engine aimed to be fast, secure and compatible with all existing Q3A mods. It is based on last non-SDL source dump of ioquake3 with latest upstream fixes applied.
This package does not contain any game content.

%prep
%setup -n %{name}-%{commithash}

%build
make RENDERER_DEFAULT=vulkan

%install
make DESTDIR=%{buildroot}%{_datadir}/games/quake3 install
mkdir -p %{buildroot}%{_datadir}/{applications,icons/hicolor/scalable/apps}
cp %{SOURCE1} %{buildroot}%{_datadir}/applications
cp code/unix/quake3.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps

%files
%defattr(0644, root, root, 0755)
%license COPYING.txt
%doc id-readme.txt README.md
%dir /usr/share/games/quake3
%{_datadir}/icons/hicolor/scalable/apps/quake3.svg
%attr(0755, root, root) /usr/share/games/quake3/*
/usr/share/applications/quake3e.desktop

%changelog
* Wed Mar 09 2026 Przemysław Białek
- update to latest version

* Wed Feb 28 2026 Przemysław Białek
- update to latest version

* Wed Feb 25 2026 Przemysław Białek
- update to latest version

* Wed Feb 18 2026 Przemysław Białek
- changed source release version to commithash

* Wed Feb 04 2026 Przemysław Białek
- first release
