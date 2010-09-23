%define	name	ganyremote
%define version	5.11.7
%define	release	%mkrel 1

Summary:	GTK frontend for anyRemote
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Group:		Graphical desktop/GNOME
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Buildarch:	noarch
Source0:	 http://download.sourceforge.net/anyremote/%name-%version.tar.gz
URL:		http://anyremote.sourceforge.net/
Requires:	pygtk2.0 python-pybluez anyremote bluez

%description
gAnyRemote package is GTK GUI frontend for anyRemote.  It provides remote
control service on Linux through Bluetooth, InfraRed, Wi-Fi or TCP/IP
connection.

%prep
%setup -q

%build
%configure2_5x --build=%{_host}
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %name

# we'll cp our own doc files
rm -rf %buildroot%_datadir/doc

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %name.lang
%defattr(-,root,root)
%doc NEWS README AUTHORS
%{_bindir}/%name
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/*.desktop
