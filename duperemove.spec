#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : duperemove
Version  : 0.11
Release  : 1
URL      : https://github.com/markfasheh/duperemove/archive/v0.11.tar.gz
Source0  : https://github.com/markfasheh/duperemove/archive/v0.11.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause GPL-2.0
Requires: duperemove-bin
Requires: duperemove-license
Requires: duperemove-man
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
Requires: duperemove-license
Requires: duperemove-man

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
%setup -q -n duperemove-0.11

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536298897
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1536298897
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/duperemove
cp LICENSE %{buildroot}/usr/share/doc/duperemove/LICENSE
cp LICENSE.xxhash %{buildroot}/usr/share/doc/duperemove/LICENSE.xxhash
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
%defattr(-,root,root,-)
/usr/share/doc/duperemove/LICENSE
/usr/share/doc/duperemove/LICENSE.xxhash

%files man
%defattr(-,root,root,-)
/usr/share/man/man8/btrfs-extent-same.8
/usr/share/man/man8/duperemove.8
/usr/share/man/man8/hashstats.8
/usr/share/man/man8/show-shared-extents.8
