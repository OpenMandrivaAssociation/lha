%define name lha
%define version	1.14i
%define release %mkrel 13
%define serial 1

Name: %{name}
Summary: An archiving and compression utility for LHarc format archives.
Version: %{version}
Release: %{release}
Source: http://www2m.biglobe.ne.jp/~dolphin/lha/prog/%{name}-114i.tar.bz2
Patch0: lha-1.14i-make.patch
Patch1: lha-1.14e-ext.patch
Patch2: lha-1.14i-fix-includes.patch
Patch3: lha-114i-sec.patch
Patch4: lha-114i-symlink.patch
Patch5: lha-dir_length_bounds_check.patch
Patch6: lha-114i-sec2.patch
Patch7: lha-1.14i-CVE-2007-2030.patch
License: Freeware-like
Group: Archiving/Compression 
URL: http://www2m.biglobe.ne.jp/~dolphin/lha/lha-unix.htm
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Epoch: %{serial}

%description
LhA is an archiving and compression utility for LHarc format archive.
LhA is mostly used in the Amiga and in the DOS world, but can be used 
under Linux to extract files from .lha and .lzh archives. 

Install the LhA package if you need to extract files from .lha or .lzh
Amiga or DOS archives, or if you have to build LhA archives to
be read on the Amiga or DOS.

%prep
%setup -q -n %{name}-114i
%patch0 -p0
%patch1
%patch2 -p0
%patch4 -p1 -b .symlink

# security fixes
%patch3 -p1 -b .sec
%patch5 -p1 -b .bounds
%patch6 -p1 -b .sec2
%patch7 -p1 -b .cve-2007-2030

%build
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -s -m 755 src/lha $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/ja/man1
install -m 644 man/lha.n $RPM_BUILD_ROOT%{_mandir}/ja/man1/lha.1

%clean
rm -r $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/lha
%lang(ja) %{_mandir}/ja/man1/lha.1.bz2


