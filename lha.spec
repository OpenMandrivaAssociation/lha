%define gitversion 20201225

Summary:	An archiving and compression utility for LHarc format archives
Name:		lha
Epoch:		1
Version:	1.14i
Release:	1.%{gitversion}.0
License:	Freeware-like
Group:		Archiving/Compression 
Url:		https://github.com/jca02266/lha
# Upstream no longer provide releases, so we use git.
Source0:	https://github.com/jca02266/lha/archive/%{name}-master.zip
Source1:	http://packages.debian.org/changelogs/pool/non-free/l/lha/current/copyright

%description
LhA is an archiving and compression utility for LHarc format archive.
LhA is mostly used in the Amiga and in the DOS world, but can be used 
under Linux to extract files from .lha and .lzh archives. 

Install the LhA package if you need to extract files from .lha or .lzh
Amiga or DOS archives, or if you have to build LhA archives to
be read on the Amiga or DOS.

%prep
%setup -qn %{name}-master


cp %{SOURCE1} .
%build

autoreconf -is
%configure
%make_build

%install
%make_install

mkdir -p %{buildroot}%{_mandir}/ja/mann
install -m 644 man/lha.n %{buildroot}%{_mandir}/ja/mann/lha.n

%files
%doc copyright
%{_bindir}/lha
%{_mandir}/man1/lha.1*
%lang(ja) %{_mandir}/ja/mann/lha.n*
