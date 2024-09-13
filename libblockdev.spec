#
# Conditional build:
%bcond_without	apidocs		# gtk-doc based API documentation
%bcond_without	python3		# CPython 3.x support
#
Summary:	A library for low-level manipulation with block devices
Summary(pl.UTF-8):	Biblioteka do niskopoziomowych operacji na urządzeniach blokowych
Name:		libblockdev
Version:	3.2.0
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	https://github.com/storaged-project/libblockdev/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	60a52413f14303147c79a6f368aced92
URL:		https://github.com/storaged-project/libblockdev
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	cryptsetup-devel >= 2.7.0
BuildRequires:	device-mapper-devel >= 1.02.93
BuildRequires:	e2fsprogs-devel
BuildRequires:	glib2-devel >= 1:2.42.2
BuildRequires:	gobject-introspection-devel >= 1.3.0
BuildRequires:	gtk-doc
BuildRequires:	json-glib-devel >= 1.0
BuildRequires:	kmod-devel >= 19
BuildRequires:	keyutils-devel
BuildRequires:	libatasmart-devel >= 0.17
BuildRequires:	libblkid-devel >= 2.27.0
BuildRequires:	libbytesize-devel >= 0.1
BuildRequires:	libfdisk-devel >= 2.31.0
BuildRequires:	libmount-devel >= 2.23.0
BuildRequires:	libnvme-devel >= 1.4
BuildRequires:	libtool >= 2:2
BuildRequires:	libuuid-devel
BuildRequires:	ndctl-devel >= 60
BuildRequires:	nss-devel >= 3.18.1
BuildRequires:	parted-devel >= 3.1
BuildRequires:	pkgconfig
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-modules >= 1:3.2
%endif
BuildRequires:	rpm-build >= 4.6
# for <drivedb.h>
BuildRequires:	smartmontools
BuildRequires:	udev-devel >= 1:216
BuildRequires:	volume_key-devel
BuildRequires:	yaml-devel >= 0.1
Requires:	glib2 >= 1:2.42.2
Requires:	kmod-libs >= 19
Requires:	udev-libs >= 1:216
Obsoletes:	libblockdev-kbd < 3.0
Obsoletes:	libblockdev-part-err < 3.0
Obsoletes:	libblockdev-vdo < 3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libblockdev is a C library with GObject introspection support that
can be used for doing low-level operations with block devices like
setting up LVM, BTRFS, LUKS or MD RAID. The library uses plugins (LVM,
BTRFS,...) and serves as a thin wrapper around its plugins'
functionality. All the plugins, however, can be used as standalone
libraries. One of the core principles of libblockdev is that it is
stateless from the storage configuration's perspective (e.g. it has no
information about VGs when creating an LV).

%description -l pl.UTF-8
libblockdev to biblioteka C z obsługą GObject introspection. Można ją
wykorzystywać do wykonywania niskopoziomowych operacji na urządzeniach
blokowaych, w tym konfigurowania LVM, BTRFS, LUKS czy MD RAID.
Biblioteka wykorzystuje wtyczki (LVM, BTRFS...) oraz służy jako cienka
warstwa pośrednia do funkcjonalności tych wtyczek. Wszystkie wtyczki
mogą być także wykorzystywane jako samodzielne biblioteki. Jedną z
głównych zasad libblockdev jest to, że jest bezstanowa z punktu
widzenia konfiguracji urządzenia (np. nie ma informacji o VG podczas
tworzenia LV).

%package devel
Summary:	Header files for libblockdev library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libblockdec
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.42.2
Obsoletes:	libblockdev-kbd-devel < 3.0
Obsoletes:	libblockdev-part-err-devel < 3.0
Obsoletes:	libblockdev-vdo-devel < 3.0

%description devel
Header files for libblockdev library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libblockdev.

%package apidocs
Summary:	libblockdev API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libblockdev
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description apidocs
API documentation for libblockdev library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libblockdev.

%package btrfs
Summary:	The BTRFS plugin for the libblockdev library
Summary(pl.UTF-8):	Wtyczka BTRFS do biblioteki libblockdev
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
# btrfs command
Requires:	btrfs-progs >= 3.18.2
Requires:	libbytesize >= 0.1

%description btrfs
The libblockdev library plugin providing the BTRFS-related
functionality.

%description btrfs -l pl.UTF-8
Wtyczka biblioteki libblockdev zapewniająca funkcjonalność
związaną z BTRFS.

%package btrfs-devel
Summary:	Header file for libblockdev BTRFS plugin
Summary(pl.UTF-8):	Plik nagłówkowy wtyczki BTRFS do biblioteki libblockdev
Group:		Development/Libraries
Requires:	%{name}-btrfs = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description btrfs-devel
Header file for libblockdev BTRFS plugin.

%description btrfs-devel -l pl.UTF-8
Plik nagłówkowy wtyczki BTRFS do biblioteki libblockdev.

%package crypto
Summary:	The crypto plugin for the libblockdev library
Summary(pl.UTF-8):	Wtyczka crypto do biblioteki libblockdev
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cryptsetup-libs >= 2.7.0
Requires:	libblkid >= 2.27.0
Requires:	nss >= 3.18.1

%description crypto
The libblockdev library plugin providing the functionality related to
encrypted devices (LUKS).

%description crypto -l pl.UTF-8
Wtyczka biblioteki libblockdev zapewniająca funkcjonalność
związaną z urządzeniami szyfrowanymi (LUKS).

%package crypto-devel
Summary:	Header file for libblockdev crypto plugin
Summary(pl.UTF-8):	Plik nagłówkowy wtyczki crypto do biblioteki libblockdev
Group:		Development/Libraries
Requires:	%{name}-crypto = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description crypto-devel
Header file for libblockdev crypto plugin.

%description crypto-devel -l pl.UTF-8
Plik nagłówkowy wtyczki crypto do biblioteki libblockdev.

%package dm
Summary:	The Device Mapper plugin for the libblockdev library
Summary(pl.UTF-8):	Wtyczka Device Mapper do biblioteki libblockdev
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
# dmsetup command
Requires:	device-mapper >= 1.02.93

%description dm
The libblockdev library plugin providing the functionality related to
Device Mapper.

%description dm -l pl.UTF-8
Wtyczka biblioteki libblockdev zapewniająca funkcjonalność
związaną z Device Mapperem.

%package dm-devel
Summary:	Header file for libblockdev Device Mapper plugin
Summary(pl.UTF-8):	Plik nagłówkowy wtyczki Device Mapper do biblioteki libblockdev
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-dm = %{version}-%{release}
Requires:	device-mapper-devel >= 1.02.93

%description dm-devel
Header file for libblockdev Device Mapper plugin.

%description dm-devel -l pl.UTF-8
Plik nagłówkowy wtyczki Device Mapper do biblioteki libblockdev.

%package fs
Summary:	The FS plugin for the libblockdev library
Summary(pl.UTF-8):	Wtyczka FS do biblioteki libblockdev
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libblkid >= 2.27.0
Requires:	libmount >= 2.23.0
# mkfs.vfat, fatlabel, fsck.vfat commands
Suggests:	dosfstools
# mke2fs, e2fsck, tune2fs, dumpe2fs, resize2fs commands
Suggests:	e2fsprogs
# mkntfs, ntfsfix, ntfsresize, ntfslabel, ntfscluster commands
Suggests:	ntfsprogs
# mkfs.xfs, xfs_db, xfs_repair, xfs_admin, xfs_growfs commands
Suggests:	xfsprogs

%description fs
The libblockdev library plugin providing the functionality related to
operations with file systems.

%description fs -l pl.UTF-8
Wtyczka biblioteki libblockdev zapewniająca funkcjonalność
związaną z operacjami na systemie plików.

%package fs-devel
Summary:	Header files for libblockdev FS plugin
Summary(pl.UTF-8):	Pliki nagłówkowe wtyczki FS do biblioteki libblockdev
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-fs = %{version}-%{release}

%description fs-devel
Header files for libblockdev FS plugin.

%description fs-devel -l pl.UTF-8
Pliki nagłówkowe wtyczki FS do biblioteki libblockdev.

%package loop
Summary:	The loop plugin for the libblockdev library
Summary(pl.UTF-8):	Wtyczka loop do biblioteki libblockdev
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	losetup >= 2.23.2

%description loop
The libblockdev library plugin providing the functionality related to
loop devices.

%description loop -l pl.UTF-8
Wtyczka biblioteki libblockdev zapewniająca funkcjonalność
związaną z urządzeniami loopback.

%package loop-devel
Summary:	Header file for libblockdev loop plugin
Summary(pl.UTF-8):	Plik nagłówkowy wtyczki loop do biblioteki libblockdev
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-loop = %{version}-%{release}

%description loop-devel
Header file for libblockdev loop plugin.

%description loop-devel -l pl.UTF-8
Plik nagłówkowy wtyczki loop do biblioteki libblockdev.

%package lvm
Summary:	The LVM plugin for the libblockdev library
Summary(pl.UTF-8):	Wtyczka LVM do biblioteki libblockdev
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	device-mapper-libs >= 1.02.93
# lvm command
Requires:	lvm2 >= 1.02.116
Requires:	thin-provisioning-tools

%description lvm
The libblockdev library plugin providing the LVM-related
functionality.

%description lvm -l pl.UTF-8
Wtyczka biblioteki libblockdev zapewniająca funkcjonalność
związaną z LVM.

%package lvm-devel
Summary:	Header file for libblockdev LVM plugin
Summary(pl.UTF-8):	Plik nagłówkowy wtyczki LVM do biblioteki libblockdev
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-lvm = %{version}-%{release}
Requires:	device-mapper-devel >= 1.02.93

%description lvm-devel
Header file for libblockdev LVM plugin.

%description lvm-devel -l pl.UTF-8
Plik nagłówkowy wtyczki LVM do biblioteki libblockdev.

%package lvm-dbus
Summary:	The LVM-DBus plugin for the libblockdev library
Summary(pl.UTF-8):	Wtyczka LVM-DBus do biblioteki libblockdev
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	device-mapper-libs >= 1.02.93
Requires:	lvm2-dbusd >= 2.02.156
Requires:	thin-provisioning-tools

%description lvm-dbus
The libblockdev library plugin providing the LVM-related functionality
utilizing the LVM DBus API.

%description lvm-dbus -l pl.UTF-8
Wtyczka biblioteki libblockdev zapewniająca funkcjonalność
związaną z LVM, wykorzystująca API DBus LVM.

%package lvm-dbus-devel
Summary:	Development file for libblockdev LVM-DBus plugin
Summary(pl.UTF-8):	Plik programistyczny wtyczki LVM-DBus do biblioteki libblockdev
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-lvm-dbus = %{version}-%{release}

%description lvm-dbus-devel
Development file for libblockdev LVM-DBus plugin.

%description lvm-dbus-devel -l pl.UTF-8
Plik programistyczny wtyczki LVM-DBus do biblioteki libblockdev.

%package mdraid
Summary:	The MD RAID plugin for the libblockdev library
Summary(pl.UTF-8):	Wtyczka MD RAID do biblioteki libblockdev
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libbytesize >= 0.1
Requires:	mdadm >= 3.3.2

%description mdraid
The libblockdev library plugin providing the functionality related to
MD RAID.

%description mdraid -l pl.UTF-8
Wtyczka biblioteki libblockdev zapewniająca funkcjonalność
związaną z MD RAID.

%package mdraid-devel
Summary:	Header file for libblockdev MD RAID plugin
Summary(pl.UTF-8):	Plik nagłówkowy wtyczki MD RAID do biblioteki libblockdev
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-mdraid = %{version}-%{release}

%description mdraid-devel
Header file for libblockdev MD RAID plugin.

%description mdraid-devel -l pl.UTF-8
Plik nagłówkowy wtyczki MD RAID do biblioteki libblockdev.

%package mpath
Summary:	The multipath plugin for the libblockdev library
Summary(pl.UTF-8):	Wtyczka multipath do biblioteki libblockdev
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	device-mapper-libs >= 1.02.93
# multipath, mpathconf tools
Requires:	multipath-tools >= 0.4.9

%description mpath
The libblockdev library plugin providing the functionality related to
multipath devices.

%description mpath -l pl.UTF-8
Wtyczka biblioteki libblockdev zapewniająca funkcjonalność
związaną z urządzeniami multipath.

%package mpath-devel
Summary:	Header file for libblockdev multipath plugin
Summary(pl.UTF-8):	Plik nagłówkowy wtyczki multipath do biblioteki libblockdev
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-mpath = %{version}-%{release}

%description mpath-devel
Header file for libblockdev multipath plugin.

%description mpath-devel -l pl.UTF-8
Plik nagłówkowy wtyczki multipath do biblioteki libblockdev.

%package nvdimm
Summary:	The nvdimm plugin for the libblockdev library
Summary(pl.UTF-8):	Wtyczka nvdimm do biblioteki libblockdev
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
# ndctl command
Requires:	ndctl >= 60

%description nvdimm
The libblockdev library plugin providing the functionality related to
nvdimm devices.

%description nvdimm -l pl.UTF-8
Wtyczka biblioteki libblockdev zapewniająca funkcjonalność
związaną z urządzeniami nvdimm.

%package nvdimm-devel
Summary:	Header file for libblockdev nvdimm plugin
Summary(pl.UTF-8):	Plik nagłówkowy wtyczki nvdimm do biblioteki libblockdev
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-nvdimm = %{version}-%{release}

%description nvdimm-devel
Header file for libblockdev nvdimm plugin.

%description nvdimm-devel -l pl.UTF-8
Plik nagłówkowy wtyczki nvdimm do biblioteki libblockdev.

%package nvme
Summary:	The NVMe plugin for the libblockdev library
Summary(pl.UTF-8):	Wtyczka NVMe do biblioteki libblockdev
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libnvme >= 1.4

%description nvme
The libblockdev library plugin providing the functionality related to
NVMe devices.

%description nvme -l pl.UTF-8
Wtyczka biblioteki libblockdev zapewniająca funkcjonalność
związaną z urządzeniami NVMe.

%package nvme-devel
Summary:	Header file for libblockdev NVMe plugin
Summary(pl.UTF-8):	Plik nagłówkowy wtyczki NVMe do biblioteki libblockdev
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-nvme = %{version}-%{release}

%description nvme-devel
Header file for libblockdev NVMe plugin.

%description nvme-devel -l pl.UTF-8
Plik nagłówkowy wtyczki NVMe do biblioteki libblockdev.

%package part
Summary:	The partitioning plugin for the libblockdev library
Summary(pl.UTF-8):	Wtyczka partycjonująca do biblioteki libblockdev
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
# sgdisk command
Requires:	gdisk >= 0.8.6
Requires:	libfdisk >= 2.31.0
# sfdisk command
Requires:	util-linux

%description part
The libblockdev library plugin providing the functionality related to
partitioning.

%description part -l pl.UTF-8
Wtyczka biblioteki libblockdev zapewniająca funkcjonalność
związaną z partycjonowaniem.

%package part-devel
Summary:	Header file for libblockdev part plugin
Summary(pl.UTF-8):	Plik nagłówkowy wtyczki part do biblioteki libblockdev
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-part = %{version}-%{release}

%description part-devel
Header file for libblockdev part plugin.

%description part-devel -l pl.UTF-8
Plik nagłówkowy wtyczki part do biblioteki libblockdev.

%package s390
Summary:	The s390 plugin for the libblockdev library
Summary(pl.UTF-8):	Wtyczka s390 do biblioteki libblockdev
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
# dasdfmt command (https://github.com/ibm-s390-linux/s390-tools)
#Requires:	s390-tools

%description s390
The libblockdev library plugin providing the functionality related to
s390 devices.

%description s390 -l pl.UTF-8
Wtyczka biblioteki libblockdev zapewniająca funkcjonalność
związaną z urządzeniami s390.

%package s390-devel
Summary:	Header file for libblockdev s390 plugin
Summary(pl.UTF-8):	Plik nagłówkowy wtyczki s390 do biblioteki libblockdev
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-s390 = %{version}-%{release}

%description s390-devel
Header file for libblockdev s390 plugin.

%description s390-devel -l pl.UTF-8
Plik nagłówkowy wtyczki s390 do biblioteki libblockdev.

%package smart
Summary:	The smart plugin for the libblockdev library
Summary(pl.UTF-8):	Wtyczka smart do biblioteki libblockdev
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libatasmart >= 0.17
Suggests:	smartmontools

%description smart
The libblockdev library plugin providing the functionality related to
ATA S.M.A.R.T. support through libatasmart.

%description smart -l pl.UTF-8
Wtyczka biblioteki libblockdev zapewniająca funkcjonalność
związaną ze wsparciem dla ATA S.M.A.R.T używająca libatasmart.

%package smart-devel
Summary:	Header file for libblockdev smart plugin
Summary(pl.UTF-8):	Plik nagłówkowy wtyczki smart do biblioteki libblockdev
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-smart = %{version}-%{release}

%description smart-devel
Header file for libblockdev smart plugin.

%description smart-devel -l pl.UTF-8
Plik nagłówkowy wtyczki smart do biblioteki libblockdev.

%package smartmontools
Summary:	The smartmontools plugin for the libblockdev library
Summary(pl.UTF-8):	Wtyczka smartmontools do biblioteki libblockdev
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	smartmontools

%description smartmontools
The libblockdev library plugin providing the functionality related to
ATA S.M.A.R.T. support through smartmontools.

%description smartmontools -l pl.UTF-8
Wtyczka biblioteki libblockdev zapewniająca funkcjonalność
związaną ze wsparciem dla ATA S.M.A.R.T używająca smartmontools.

%package smartmontools-devel
Summary:	Header file for libblockdev smartmontools plugin
Summary(pl.UTF-8):	Plik nagłówkowy wtyczki smartmontools do biblioteki libblockdev
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-smart-devel = %{version}-%{release}
Requires:	%{name}-smartmontools = %{version}-%{release}

%description smartmontools-devel
Header file for libblockdev smartmontools plugin.

%description smartmontools-devel -l pl.UTF-8
Plik nagłówkowy wtyczki smartmontools do biblioteki libblockdev.

%package swap
Summary:	The swap plugin for the libblockdev library
Summary(pl.UTF-8):	Wtyczka swap do biblioteki libblockdev
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libblkid >= 2.27.0
# mkswap, swaplabel commands
Requires:	util-linux >= 2.23.2

%description swap
The libblockdev library plugin providing the functionality related to
swap devices.

%description swap -l pl.UTF-8
Wtyczka biblioteki libblockdev zapewniająca funkcjonalność
związaną z urządzeniami wymiany.

%package swap-devel
Summary:	Header file for libblockdev swap plugin
Summary(pl.UTF-8):	Plik nagłówkowy wtyczki swap do biblioteki libblockdev
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-swap = %{version}-%{release}

%description swap-devel
Header file for libblockdev swap plugin.

%description swap-devel -l pl.UTF-8
Plik nagłówkowy wtyczki swap do biblioteki libblockdev.

%package plugins
Summary:	Meta-package that pulls all the libblockdev plugins as dependencies
Summary(pl.UTF-8):	Metapakiet instalujący przez zależności wszystkie wtyczki libblockdev
Group:		Libraries
Requires:	%{name}-btrfs = %{version}-%{release}
Requires:	%{name}-crypto = %{version}-%{release}
Requires:	%{name}-dm = %{version}-%{release}
Requires:	%{name}-fs = %{version}-%{release}
Requires:	%{name}-loop = %{version}-%{release}
Requires:	%{name}-lvm = %{version}-%{release}
Requires:	%{name}-lvm-dbus = %{version}-%{release}
Requires:	%{name}-mdraid = %{version}-%{release}
Requires:	%{name}-mpath = %{version}-%{release}
Requires:	%{name}-nvdimm = %{version}-%{release}
Requires:	%{name}-nvme = %{version}-%{release}
Requires:	%{name}-part = %{version}-%{release}
%ifarch s390 s390x
Requires:	%{name}-s390 = %{version}-%{release}
%endif
Requires:	%{name}-smart = %{version}-%{release}
Requires:	%{name}-smartmontools = %{version}-%{release}
Requires:	%{name}-swap = %{version}-%{release}

%description plugins
A meta-package that pulls all the libblockdev plugins as dependencies.

%description plugins -l pl.UTF-8
Metapakiet instalujący przez zależności wszystkie wtyczki libblockdev.

%package tools
Summary:	Various tools based on libblockdev
Summary(pl.UTF-8):	Różne narzędzia bazujące na libblockdev
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Requires:	parted-libs >= 3.1

%description tools
Various tools based on libblockdev.

%description tools -l pl.UTF-8
Różne narzędzia bazujące na libblockdev.

%package -n python3-blockdev
Summary:	Python 3 bindings for libblockdev
Summary(pl.UTF-8):	Wiązania Pythona 3 do libblockdev
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python3-pygobject3 >= 3
Obsoletes:	python-blockdev < 3.0

%description -n python3-blockdev
This package contains Python 3 bindings for libblockdev.

%description -n python3-blockdev -l pl.UTF-8
Ten pakiet zawiera wiązania Pythona 3 do libblockdev.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	%{__with_without apidocs gtk-doc} \
	%{!?with_python3:--without-python3} \
	--with-drivedb=/var/lib/smartmontools/drivedb

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_gtkdocdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with apidocs}
%{__mv} $RPM_BUILD_ROOT{%{_datadir}/gtk-doc/html/libblockdev,%{_gtkdocdir}}
%endif

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%if %{with python3}
%py3_comp $RPM_BUILD_ROOT%{py3_sitedir}
%py3_ocomp $RPM_BUILD_ROOT%{py3_sitedir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	btrfs -p /sbin/ldconfig
%postun	btrfs -p /sbin/ldconfig

%post	crypto -p /sbin/ldconfig
%postun	crypto -p /sbin/ldconfig

%post	dm -p /sbin/ldconfig
%postun	dm -p /sbin/ldconfig

%post	fs -p /sbin/ldconfig
%postun	fs -p /sbin/ldconfig

%post	loop -p /sbin/ldconfig
%postun	loop -p /sbin/ldconfig

%post	lvm -p /sbin/ldconfig
%postun	lvm -p /sbin/ldconfig

%post	lvm-dbus -p /sbin/ldconfig
%postun	lvm-dbus -p /sbin/ldconfig

%post	mdraid -p /sbin/ldconfig
%postun	mdraid -p /sbin/ldconfig

%post	mpath -p /sbin/ldconfig
%postun	mpath -p /sbin/ldconfig

%post	nvdimm -p /sbin/ldconfig
%postun	nvdimm -p /sbin/ldconfig

%post	nvme -p /sbin/ldconfig
%postun	nvme -p /sbin/ldconfig

%post	part -p /sbin/ldconfig
%postun	part -p /sbin/ldconfig

%post	s390 -p /sbin/ldconfig
%postun	s390 -p /sbin/ldconfig

%post	smart -p /sbin/ldconfig
%postun	smart -p /sbin/ldconfig

%post	smartmontools -p /sbin/ldconfig
%postun	smartmontools -p /sbin/ldconfig

%post	swap -p /sbin/ldconfig
%postun	swap -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_utils.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbd_utils.so.3
%attr(755,root,root) %{_libdir}/libblockdev.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libblockdev.so.3
%dir %{_sysconfdir}/libblockdev
%dir %{_sysconfdir}/libblockdev/3
%dir %{_sysconfdir}/libblockdev/3/conf.d
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/libblockdev/3/conf.d/00-default.cfg
%{_libdir}/girepository-1.0/BlockDev-3.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_utils.so
%attr(755,root,root) %{_libdir}/libblockdev.so
%dir %{_includedir}/blockdev
%{_includedir}/blockdev/blockdev.h
%{_includedir}/blockdev/dbus.h
%{_includedir}/blockdev/dev_utils.h
%{_includedir}/blockdev/exec.h
%{_includedir}/blockdev/extra_arg.h
%{_includedir}/blockdev/logging.h
%{_includedir}/blockdev/module.h
%{_includedir}/blockdev/plugins.h
%{_includedir}/blockdev/sizes.h
%{_includedir}/blockdev/utils.h
%{_datadir}/gir-1.0/BlockDev-3.0.gir
%{_pkgconfigdir}/blockdev.pc
%{_pkgconfigdir}/blockdev-utils.pc

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libblockdev
%endif

%files btrfs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_btrfs.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbd_btrfs.so.3

%files btrfs-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_btrfs.so
%{_includedir}/blockdev/btrfs.h

%files crypto
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_crypto.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbd_crypto.so.3

%files crypto-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_crypto.so
%{_includedir}/blockdev/crypto.h

%files dm
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_dm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbd_dm.so.3

%files dm-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_dm.so
%{_includedir}/blockdev/dm.h

%files fs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_fs.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbd_fs.so.3

%files fs-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_fs.so
%{_includedir}/blockdev/fs.h
%{_includedir}/blockdev/fs

%files loop
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_loop.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbd_loop.so.3

%files loop-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_loop.so
%{_includedir}/blockdev/loop.h

%files lvm
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_lvm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbd_lvm.so.3

%files lvm-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_lvm.so
%{_includedir}/blockdev/lvm.h

%files lvm-dbus
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_lvm-dbus.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbd_lvm-dbus.so.3
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/libblockdev/3/conf.d/10-lvm-dbus.cfg

%files lvm-dbus-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_lvm-dbus.so

%files mdraid
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_mdraid.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbd_mdraid.so.3

%files mdraid-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_mdraid.so
%{_includedir}/blockdev/mdraid.h

%files mpath
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_mpath.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbd_mpath.so.3

%files mpath-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_mpath.so
%{_includedir}/blockdev/mpath.h

%files nvdimm
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_nvdimm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbd_nvdimm.so.3

%files nvdimm-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_nvdimm.so
%{_includedir}/blockdev/nvdimm.h

%files nvme
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_nvme.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbd_nvme.so.3

%files nvme-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_nvme.so
%{_includedir}/blockdev/nvme.h

%files part
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_part.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbd_part.so.3

%files part-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_part.so
%{_includedir}/blockdev/part.h

%ifarch s390 s390x
%files s390
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_s390.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbd_s390.so.3

%files s390-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_s390.so
%{_includedir}/blockdev/s390.h
%endif

%files smart
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_smart.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbd_smart.so.3

%files smart-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_smart.so
%{_includedir}/blockdev/smart.h

%files smartmontools
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_smartmontools.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbd_smartmontools.so.3

%files smartmontools-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_smartmontools.so

%files swap
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_swap.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbd_swap.so.3

%files swap-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_swap.so
%{_includedir}/blockdev/swap.h

%files plugins
%defattr(644,root,root,755)

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lvm-cache-stats
%attr(755,root,root) %{_bindir}/vfat-resize

%if %{with python3}
%files -n python3-blockdev
%defattr(644,root,root,755)
%{py3_sitedir}/gi/overrides/BlockDev.py
%{py3_sitedir}/gi/overrides/__pycache__/BlockDev.cpython-*.py[co]
%endif
