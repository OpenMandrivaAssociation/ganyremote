%define name ganyremote
%define version 3.0
%define release %mkrel 1

Summary: GTK frontend for anyRemote
Name: %{name}
Version: %{version}
Release: %{release}
License: GPLv2+
Group: Graphical desktop/GNOME
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Buildarch: noarch
Source0: http://nchc.dl.sourceforge.net/sourceforge/anyremote/%name-%version.tar.gz
URL: http://anyremote.sourceforge.net/
Requires: pygtk2.0 python-pybluez anyremote bluez-utils

%description
gAnyRemote package is GTK GUI frontend for anyRemote
(http://anyremote.sourceforge.net/). The overall goal of this project is to
provide remote control service on Linux through Bluetooth, InfraRed, Wi-Fi
or TCP/IP connection.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# we'll cp our own doc files
rm -rf %buildroot%_datadir/doc

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus

%postun
%clean_menus

%files
%defattr(-,root,root)
%doc NEWS README AUTHORS
%{_bindir}/%name
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/*.desktop
