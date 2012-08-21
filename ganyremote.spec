%define	name	ganyremote
%define version	6.0.1
%define	release	%mkrel 1

Summary:	GTK frontend for anyRemote
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Group:		Graphical desktop/GNOME
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
%makeinstall_std

%find_lang %name

# we'll cp our own doc files
rm -rf %buildroot%_datadir/doc

%files -f %name.lang
%doc NEWS README AUTHORS
%{_bindir}/%name
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/*.desktop
