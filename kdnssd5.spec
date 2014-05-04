%define major 5
%define libname %mklibname KF5DNSSD %{major}
%define devname %mklibname KF5DNSSD -d
%define debug_package %{nil}

Name: kdnssd5
Version: 4.98.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/unstable/frameworks/%{version}/kdnssd-%{version}.tar.xz
Summary: The KDE Frameworks 5 DNSSD library
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5

%description
The KDE Frameworks 5 DNSSD abstraction library.

%package -n %{libname}
Summary: The KDE Frameworks 5 DNSSD library
Group: System/Libraries

%description -n %{libname}
The KDE Frameworks 5 DNSSD abstraction library.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files for %{name}.

%{name} is the KDE Frameworks 5 DNSSD abstraction library.

%prep
%setup -q -n kdnssd-%{version}
%cmake

%build
%make -C build

%install
%makeinstall_std -C build
mkdir -p %{buildroot}%{_libdir}/qt5
mv %{buildroot}%{_prefix}/mkspecs %{buildroot}%{_libdir}/qt5/

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5DNSSD
%{_libdir}/qt5/mkspecs/modules/*
