Summary:	DNS-SD Service Discovery Monitor
Name:		kdnssd
Version:	4.11.4
Release:	1
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	ftp://ftp.kde.org/pub/kde/%{ftpdir}/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
Requires:	nss_mdns
Conflicts:	kdenetwork4-devel < 3:4.11.0

%description
DNS-SD Service Discovery Monitor.

%files
%dir %{_kde_appsdir}/remoteview
%{_kde_appsdir}/remoteview/zeroconf.desktop
%{_kde_libdir}/kde4/kded_dnssdwatcher.so
%{_kde_libdir}/kde4/kio_zeroconf.so
%{_kde_services}/kded/dnssdwatcher.desktop
%{_kde_services}/zeroconf.protocol
%{_datadir}/dbus-1/interfaces/org.kde.kdnssd.xml

#-------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.0-1
- New version 4.11.0
- Split from kdenetwork4 package as upstream did
