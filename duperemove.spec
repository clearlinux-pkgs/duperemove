#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : duperemove
Version  : 0.11.2
Release  : 6
URL      : https://github.com/markfasheh/duperemove/archive/v0.11.2/duperemove-0.11.2.tar.gz
Source0  : https://github.com/markfasheh/duperemove/archive/v0.11.2/duperemove-0.11.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause GPL-2.0
Requires: duperemove-bin = %{version}-%{release}
Requires: duperemove-license = %{version}-%{release}
Requires: duperemove-man = %{version}-%{release}
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : sqlite-autoconf-dev

%description
# Duperemove
Duperemove is a simple tool for finding duplicated extents and
submitting them for deduplication. When given a list of files it will
hash their contents on a block by block basis and compare those hashes
to each other, finding and categorizing blocks that match each
other. When given the -d option, duperemove will submit those
extents for deduplication using the Linux kernel extent-same ioctl.

%package bin
Summary: bin components for the duperemove package.
Group: Binaries
Requires: duperemove-license = %{version}-%{release}

%description bin
bin components for the duperemove package.


%package license
Summary: license components for the duperemove package.
Group: Default

%description license
license components for the duperemove package.


%package man
Summary: man components for the duperemove package.
Group: Default

%description man
man components for the duperemove package.


%prep
%setup -q -n duperemove-0.11.2
cd %{_builddir}/duperemove-0.11.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1605731790
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1605731790
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/duperemove
cp %{_builddir}/duperemove-0.11.2/LICENSE %{buildroot}/usr/share/package-licenses/duperemove/cca1a98df1d42b70d0e705fe296bf45230196c14
cp %{_builddir}/duperemove-0.11.2/LICENSE.xxhash %{buildroot}/usr/share/package-licenses/duperemove/faa50d629c27ea217aba549a466c7082430e1528
%make_install PREFIX=/usr SBINDIR=/usr/bin

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/btrfs-extent-same
/usr/bin/duperemove
/usr/bin/hashstats
/usr/bin/show-shared-extents

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/duperemove/cca1a98df1d42b70d0e705fe296bf45230196c14
/usr/share/package-licenses/duperemove/faa50d629c27ea217aba549a466c7082430e1528

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/btrfs-extent-same.8
/usr/share/man/man8/duperemove.8
/usr/share/man/man8/hashstats.8
/usr/share/man/man8/show-shared-extents.8
