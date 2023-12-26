#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
# autospec version: v3
# autospec commit: c1050fe
#
Name     : duperemove
Version  : 0.14.1
Release  : 10
URL      : https://github.com/markfasheh/duperemove/archive/v0.14.1/duperemove-0.14.1.tar.gz
Source0  : https://github.com/markfasheh/duperemove/archive/v0.14.1/duperemove-0.14.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause GPL-2.0
Requires: duperemove-bin = %{version}-%{release}
Requires: duperemove-license = %{version}-%{release}
Requires: duperemove-man = %{version}-%{release}
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : sqlite-autoconf-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Duperemove
Duperemove is a simple tool for finding duplicated extents and
submitting them for deduplication. When given a list of files it will
hash their contents on an extent by extent basis and compare those hashes
to each other, finding and categorizing extents that match each
other. Optionally, a per-block hash can be applied for further duplication lookup.
When given the -d option, duperemove will submit those
extents for deduplication using the Linux kernel FIDEDUPRANGE ioctl.

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
%setup -q -n duperemove-0.14.1
cd %{_builddir}/duperemove-0.14.1
pushd ..
cp -a duperemove-0.14.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1703620384
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
make  %{?_smp_mflags}

pushd ../buildavx2
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1703620384
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/duperemove
cp %{_builddir}/duperemove-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/duperemove/cca1a98df1d42b70d0e705fe296bf45230196c14 || :
cp %{_builddir}/duperemove-%{version}/LICENSE.xxhash %{buildroot}/usr/share/package-licenses/duperemove/faa50d629c27ea217aba549a466c7082430e1528 || :
pushd ../buildavx2/
%make_install_v3 PREFIX=/usr SBINDIR=/usr/bin
popd
%make_install PREFIX=/usr SBINDIR=/usr/bin
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/btrfs-extent-same
/V3/usr/bin/duperemove
/V3/usr/bin/hashstats
/usr/bin/btrfs-extent-same
/usr/bin/duperemove
/usr/bin/hashstats

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
