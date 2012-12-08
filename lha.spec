%define name lha
%define version	1.14i
%define release %mkrel 23
%define serial 1

Name: %{name}
Summary: An archiving and compression utility for LHarc format archives
Version: %{version}
Release: %{release}
Source: http://www2m.biglobe.ne.jp/~dolphin/lha/prog/%{name}-114i.tar.bz2
Source1: http://packages.debian.org/changelogs/pool/non-free/l/lha/current/copyright
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

cp %{SOURCE1} .

%build
make OPTIMIZE="%{optflags} -DSUPPORT_LH7 -DMKSTEMP" LDFLAGS="%ldflags"

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
%doc copyright
%{_bindir}/lha
%lang(ja) %{_mandir}/ja/man1/lha.1*




%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1:1.14i-22mdv2011.0
+ Revision: 666075
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1:1.14i-21mdv2011.0
+ Revision: 606404
- rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 1:1.14i-20mdv2010.1
+ Revision: 520139
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1:1.14i-19mdv2010.0
+ Revision: 425509
- rebuild

* Sat Dec 20 2008 Oden Eriksson <oeriksson@mandriva.com> 1:1.14i-18mdv2009.1
+ Revision: 316439
- use the %%ldflags macro

* Fri Dec 19 2008 Oden Eriksson <oeriksson@mandriva.com> 1:1.14i-17mdv2009.1
+ Revision: 316241
- make it respect old OPTIMIZE CFLAGS (use mkstemp)
- use LDFLAGS from the %%configure macro

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1:1.14i-16mdv2009.0
+ Revision: 222427
- rebuild

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 1:1.14i-15mdv2008.1
+ Revision: 150445
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- fix summary-ended-with-dot
- do not hardcode bz2 extension

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Jul 06 2007 Olivier Blin <oblin@mandriva.com> 1:1.14i-14mdv2008.0
+ Revision: 48938
- add copyright file from Debian

* Wed Jul 04 2007 Olivier Blin <oblin@mandriva.com> 1:1.14i-13mdv2008.0
+ Revision: 48033
- apply security fix for CVE-2007-2030 (#31213)


* Sat Jan 13 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.14i-12mdv2007.0
+ Revision: 108282
- drop packager tag
- Import lha

* Sat Jan 13 2007 Götz Waschk <waschk@mandriva.org> 1.14i-12mdv2007.1
- unpack patches

* Sat Dec 31 2005 Guillaume Cottenceau <gc@mandrakesoft.com> 1.14i-12mdk
- Rebuild

* Fri Sep 17 2004 Götz Waschk <waschk@linux-mandrake.com> 1.14i-11mdk
- add symlink patch from fedora
- security update (CAN-2004-0769, CAN-2004-0771, CAN-2004-0694, CAN-2004-0745)

* Wed May 05 2004 Götz Waschk <waschk@linux-mandrake.com> 1.14i-10mdk
- security update (buffer overflow, directory traversal)

* Fri Feb 27 2004 Götz Waschk <waschk@linux-mandrake.com> 1.14i-9mdk
- language tag japanese man page
- fix url

