Summary:	An archiving and compression utility for LHarc format archives
Name:		lha
Epoch:		1
Version:	1.14i
Release:	29
License:	Freeware-like
Group:		Archiving/Compression 
Url:		http://www2m.biglobe.ne.jp/~dolphin/lha/lha-unix.htm
Source0:	http://www2m.biglobe.ne.jp/~dolphin/lha/prog/%{name}-114i.tar.bz2
Source1:	http://packages.debian.org/changelogs/pool/non-free/l/lha/current/copyright
Patch0:		lha-1.14i-make.patch
Patch1:		lha-1.14e-ext.patch
Patch2:		lha-1.14i-fix-includes.patch
Patch3:		lha-114i-sec.patch
Patch4:		lha-114i-symlink.patch
Patch5:		lha-dir_length_bounds_check.patch
Patch6:		lha-114i-sec2.patch
Patch7:		lha-1.14i-CVE-2007-2030.patch

%description
LhA is an archiving and compression utility for LHarc format archive.
LhA is mostly used in the Amiga and in the DOS world, but can be used 
under Linux to extract files from .lha and .lzh archives. 

Install the LhA package if you need to extract files from .lha or .lzh
Amiga or DOS archives, or if you have to build LhA archives to
be read on the Amiga or DOS.

%prep
%setup -qn %{name}-114i
%patch0 -p0
%patch1
%patch2 -p0
%patch4 -p1 -b .symlink

# security fixes
%patch3 -p1 -b .sec
%patch5 -p1 -b .bounds
%patch6 -p1 -b .sec2
%patch7 -p1 -b .cve-2007-2030

cp %{SOURCE1} .

%build
make OPTIMIZE="%{optflags} -DSUPPORT_LH7 -DMKSTEMP" LDFLAGS="%{ldflags}"

%install
install -m755 src/lha -D %{buildroot}%{_bindir}/lha
install -m644 man/lha.n -D %{buildroot}%{_mandir}/ja/man1/lha.1

%files
%doc copyright
%{_bindir}/lha
%lang(ja) %{_mandir}/ja/man1/lha.1*

