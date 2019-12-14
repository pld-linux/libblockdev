#
# Conditional build:
%bcond_without	apidocs		# gtk-doc based API documentation
#
Summary:	A library for low-level manipulation with block devices
Summary(pl.UTF-8):	Biblioteka do niskopoziomowych operacji na urządzeniach blokowych
Name:		libblockdev
Version:	2.23
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	https://github.com/storaged-project/libblockdev/releases/download/%{version}-1/%{name}-%{version}.tar.gz
# Source0-md5:	b956653be98a677cf004c07b302941b9
URL:		https://github.com/storaged-project/libblockdev
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	cryptsetup-devel >= 1.6.7
BuildRequires:	device-mapper-devel >= 1.02.93
BuildRequires:	dmraid-devel
BuildRequires:	glib2-devel >= 1:2.42.2
BuildRequires:	gobject-introspection-devel >= 1.3.0
BuildRequires:	gtk-doc
BuildRequires:	kmod-devel >= 19
BuildRequires:	libblkid-devel >= 2.23.0
BuildRequires:	libbytesize-devel >= 0.1
BuildRequires:	libmount-devel >= 2.23.0
BuildRequires:	libtool >= 2:2
BuildRequires:	libuuid-devel
BuildRequires:	ndctl-devel >= 58.4
BuildRequires:	nss-devel >= 3.18.0
BuildRequires:	parted-devel >= 3.1
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 2
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	udev-devel >= 1:216
BuildRequires:	volume_key-devel
BuildRequires:	yaml-devel >= 0.1
Requires:	glib2 >= 1:2.42.2
Requires:	kmod-libs >= 19
Requires:	udev-libs >= 1:216
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
Requires:	%{name}-btrfs = %{version}-%{release}
Requires:	%{name}-crypto = %{version}-%{release}
Requires:	%{name}-dm = %{version}-%{release}
Requires:	%{name}-fs = %{version}-%{release}
Requires:	%{name}-kbd = %{version}-%{release}
Requires:	%{name}-loop = %{version}-%{release}
Requires:	%{name}-lvm = %{version}-%{release}
Requires:	%{name}-lvm-dbus = %{version}-%{release}
Requires:	%{name}-mdraid = %{version}-%{release}
Requires:	%{name}-mpath = %{version}-%{release}
Requires:	%{name}-part = %{version}-%{release}
Requires:	%{name}-swap = %{version}-%{release}
Requires:	glib2-devel >= 1:2.42.2

%description devel
Header files for libblockdev library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libblockdev.

%package apidocs
Summary:	libblockdev API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libblockdev
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
API documentation for libblockdev library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libblockdev.

%package btrfs
Summary:	The BTRFS plugin for the libblockdev library
Summary(pl.UTF-8):	Wtyczka BTRFS do biblioteki libblockdev
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	btrfs-progs
Requires:	libbytesize >= 0.1

%description btrfs
The libblockdev library plugin providing the BTRFS-related
functionality.

%description btrfs -l pl.UTF-8
Wtyczka biblioteki libblockdev zapewniająca funkcjonalność
związaną z BTRFS.

%package crypto
Summary:	The crypto plugin for the libblockdev library
Summary(pl.UTF-8):	Wtyczka crypto do biblioteki libblockdev
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cryptsetup >= 1.6.7
Requires:	libblkid >= 2.23.0
Requires:	nss >= 3.18.1

%description crypto
The libblockdev library plugin providing the functionality related to
encrypted devices (LUKS).

%description crypto -l pl.UTF-8
Wtyczka biblioteki libblockdev zapewniająca funkcjonalność
związaną z urządzeniami szyfrowanymi (LUKS).

%package dm
Summary:	The Device Mapper plugin for the libblockdev library
Summary(pl.UTF-8):	Wtyczka Device Mapper do biblioteki libblockdev
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	device-mapper >= 1.02.93
Requires:	dmraid

%description dm
The libblockdev library plugin providing the functionality related to
Device Mapper.

%description dm -l pl.UTF-8
Wtyczka biblioteki libblockdev zapewniająca funkcjonalność
związaną z Device Mapperem.

%package fs
Summary:	The FS plugin for the libblockdev library
Summary(pl.UTF-8):	Wtyczka FS do biblioteki libblockdev
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libblkid >= 2.23.0
Requires:	libmount >= 2.23.0
Requires:	parted-libs >= 3.1

%description fs
The libblockdev library plugin providing the functionality related to
operations with file systems.

%description fs -l pl.UTF-8
Wtyczka biblioteki libblockdev zapewniająca funkcjonalność
związaną z operacjami na systemie plików.

%package kbd
Summary:	The KBD plugin for the libblockdev library
Summary(pl.UTF-8):	Wtyczka KBD do biblioteki libblockdev
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	bcache-tools >= 1.0.8
Requires:	libbytesize >= 0.1

%description kbd
The libblockdev library plugin providing the functionality related to
kernel block devices (namely zRAM and Bcache).

%description kbd -l pl.UTF-8
Wtyczka biblioteki libblockdev zapewniająca funkcjonalność
związaną z urządzeniami blokowymi jądra (konkretnie zRAM i Bcache).

%package loop
Summary:	The loop plugin for the libblockdev library
Summary(pl.UTF-8):	Wtyczka loop do biblioteki libblockdev
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description loop
The libblockdev library plugin providing the functionality related to
loop devices.

%description loop -l pl.UTF-8
Wtyczka biblioteki libblockdev zapewniająca funkcjonalność
związaną z urządzeniami loopback.

%package lvm
Summary:	The LVM plugin for the libblockdev library
Summary(pl.UTF-8):	Wtyczka LVM do biblioteki libblockdev
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libbytesize >= 0.1
Requires:	lvm2 >= 1.02.93
Requires:	thin-provisioning-tools

%description lvm
The libblockdev library plugin providing the LVM-related
functionality.

%description lvm -l pl.UTF-8
Wtyczka biblioteki libblockdev zapewniająca funkcjonalność
związaną z LVM.

%package lvm-dbus
Summary:	The LVM-DBus plugin for the libblockdev library
Summary(pl.UTF-8):	Wtyczka LVM-DBus do biblioteki libblockdev
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	lvm2-dbusd >= 2.02.156
Requires:	thin-provisioning-tools

%description lvm-dbus
The libblockdev library plugin providing the LVM-related functionality
utilizing the LVM DBus API.

%description lvm-dbus -l pl.UTF-8
Wtyczka biblioteki libblockdev zapewniająca funkcjonalność
związaną z LVM, wykorzystująca API DBus LVM.

%package mdraid
Summary:	The MD RAID plugin for the libblockdev library
Summary(pl.UTF-8):	Wtyczka MD RAID do biblioteki libblockdev
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libbytesize >= 0.1
Requires:	mdadm

%description mdraid
The libblockdev library plugin providing the functionality related to
MD RAID.

%description mdraid -l pl.UTF-8
Wtyczka biblioteki libblockdev zapewniająca funkcjonalność
związaną z MD RAID.

%package mpath
Summary:	The multipath plugin for the libblockdev library
Summary(pl.UTF-8):	Wtyczka multipath do biblioteki libblockdev
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	multipath-tools

%description mpath
The libblockdev library plugin providing the functionality related to
multipath devices.

%description mpath -l pl.UTF-8
Wtyczka biblioteki libblockdev zapewniająca funkcjonalność
związaną z urządzeniami multipath.

%package nvdimm
Summary:	The nvdimm plugin for the libblockdev library
Summary(pl.UTF-8):	Wtyczka nvdimm do biblioteki libblockdev
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ndctl-libs >= 58.4

%description nvdimm
The libblockdev library plugin providing the functionality related to
nvdimm devices.

%description nvdimm -l pl.UTF-8
Wtyczka biblioteki libblockdev zapewniająca funkcjonalność
związaną z urządzeniami nvdimm.

%package part
Summary:	The partitioning plugin for the libblockdev library
Summary(pl.UTF-8):	Wtyczka partycjonująca do biblioteki libblockdev
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gdisk
Requires:	multipath-tools
Requires:	parted-libs >= 3.1
Requires:	util-linux

%description part
The libblockdev library plugin providing the functionality related to
partitioning.

%description part -l pl.UTF-8
Wtyczka biblioteki libblockdev zapewniająca funkcjonalność
związaną z partycjonowaniem.

%package swap
Summary:	The swap plugin for the libblockdev library
Summary(pl.UTF-8):	Wtyczka swap do biblioteki libblockdev
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libblkid >= 2.23.0
Requires:	util-linux >= 2.23.0

%description swap
The libblockdev library plugin providing the functionality related to
swap devices.

%description swap -l pl.UTF-8
Wtyczka biblioteki libblockdev zapewniająca funkcjonalność
związaną z urządzeniami wymiany.

%package vdo
Summary:	The vdo plugin for the libblockdev library
Summary(pl.UTF-8):	Wtyczka vdo do biblioteki libblockdev
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libbytesize >= 0.1

%description vdo
The libblockdev library plugin providing the functionality related to
vdo devices.

%description vdo -l pl.UTF-8
Wtyczka biblioteki libblockdev zapewniająca funkcjonalność
związaną z urządzeniami vdo.

%package plugins
Summary:	Meta-package that pulls all the libblockdev plugins as dependencies
Summary(pl.UTF-8):	Metapakiet instalujący przez zależności wszystkie wtyczki libblockdev
Group:		Libraries
Requires:	%{name}-btrfs = %{version}-%{release}
Requires:	%{name}-crypto = %{version}-%{release}
Requires:	%{name}-dm = %{version}-%{release}
Requires:	%{name}-fs = %{version}-%{release}
Requires:	%{name}-kbd = %{version}-%{release}
Requires:	%{name}-loop = %{version}-%{release}
Requires:	%{name}-lvm = %{version}-%{release}
Requires:	%{name}-lvm-dbus = %{version}-%{release}
Requires:	%{name}-mdraid = %{version}-%{release}
Requires:	%{name}-mpath = %{version}-%{release}
Requires:	%{name}-nvdimm = %{version}-%{release}
Requires:	%{name}-part = %{version}-%{release}
Requires:	%{name}-swap = %{version}-%{release}
Requires:	%{name}-vdo = %{version}-%{release}

%description plugins
A meta-package that pulls all the libblockdev plugins as dependencies.

%description plugins -l pl.UTF-8
Metapakiet instalujący przez zależności wszystkie wtyczki libblockdev.

%package -n python-blockdev
Summary:	Python 2 bindings for libblockdev
Summary(pl.UTF-8):	Wiązania Pythona 2 do libblockdev
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-pygobject3 >= 3

%description -n python-blockdev
This package contains Python 2 bindings for libblockdev.

%description -n python-blockdev -l pl.UTF-8
Ten pakiet zawiera wiązania Pythona 2 do libblockdev.

%package -n python3-blockdev
Summary:	Python 2 bindings for libblockdev
Summary(pl.UTF-8):	Wiązania Pythona 2 do libblockdev
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python3-pygobject3 >= 3

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
	%{__with_without apidocs gtk-doc}
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

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

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

%post	kbd -p /sbin/ldconfig
%postun	kbd -p /sbin/ldconfig

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

%post	part -p /sbin/ldconfig
%postun	part -p /sbin/ldconfig

%post	swap -p /sbin/ldconfig
%postun	swap -p /sbin/ldconfig

%post	vdo -p /sbin/ldconfig
%postun	vdo -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc features.rst specs.rst
%attr(755,root,root) %{_libdir}/libbd_part_err.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbd_part_err.so.2
%attr(755,root,root) %{_libdir}/libbd_utils.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbd_utils.so.2
%attr(755,root,root) %{_libdir}/libblockdev.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libblockdev.so.2
%dir %{_sysconfdir}/libblockdev
%dir %{_sysconfdir}/libblockdev/conf.d
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/libblockdev/conf.d/00-default.cfg
%{_libdir}/girepository-1.0/BlockDev-2.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_btrfs.so
%attr(755,root,root) %{_libdir}/libbd_crypto.so
%attr(755,root,root) %{_libdir}/libbd_dm.so
%attr(755,root,root) %{_libdir}/libbd_fs.so
%attr(755,root,root) %{_libdir}/libbd_kbd.so
%attr(755,root,root) %{_libdir}/libbd_loop.so
%attr(755,root,root) %{_libdir}/libbd_lvm.so
%attr(755,root,root) %{_libdir}/libbd_lvm-dbus.so
%attr(755,root,root) %{_libdir}/libbd_mdraid.so
%attr(755,root,root) %{_libdir}/libbd_mpath.so
%attr(755,root,root) %{_libdir}/libbd_nvdimm.so
%attr(755,root,root) %{_libdir}/libbd_part.so
%attr(755,root,root) %{_libdir}/libbd_part_err.so
%attr(755,root,root) %{_libdir}/libbd_swap.so
%attr(755,root,root) %{_libdir}/libbd_utils.so
%attr(755,root,root) %{_libdir}/libbd_vdo.so
%attr(755,root,root) %{_libdir}/libblockdev.so
%{_includedir}/blockdev
%{_datadir}/gir-1.0/BlockDev-2.0.gir
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
%attr(755,root,root) %ghost %{_libdir}/libbd_btrfs.so.2

%files crypto
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_crypto.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbd_crypto.so.2

%files dm
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_dm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbd_dm.so.2

%files fs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_fs.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbd_fs.so.2

%files kbd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_kbd.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbd_kbd.so.2

%files loop
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_loop.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbd_loop.so.2

%files lvm
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lvm-cache-stats
%attr(755,root,root) %{_libdir}/libbd_lvm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbd_lvm.so.2

%files lvm-dbus
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_lvm-dbus.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbd_lvm-dbus.so.2
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/libblockdev/conf.d/10-lvm-dbus.cfg

%files mdraid
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_mdraid.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbd_mdraid.so.2

%files mpath
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_mpath.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbd_mpath.so.2

%files nvdimm
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_nvdimm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbd_nvdimm.so.2

%files part
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_part.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbd_part.so.2

%files swap
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_swap.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbd_swap.so.2

%files vdo
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbd_vdo.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbd_vdo.so.2

%files plugins
%defattr(644,root,root,755)

%files -n python-blockdev
%defattr(644,root,root,755)
%{py_sitedir}/gi/overrides/BlockDev.py[co]

%files -n python3-blockdev
%defattr(644,root,root,755)
%{py3_sitedir}/gi/overrides/BlockDev.py
