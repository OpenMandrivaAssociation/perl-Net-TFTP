%define upstream_name    Net-TFTP
Name:		perl-%{upstream_name}
Version:	0.1901
Release:	2

Summary:	Net::TFTP - TFTP Client class
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/gbarr/perl-net-tftp
Source0:	https://cpan.metacpan.org/authors/id/G/GB/GBARR/Net-TFTP-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Test::MockModule)
BuildRequires:	perl(Test::Warn)

BuildArch:	noarch

%description
Net::TFTP is a class implementing a simple Trivial File Transfer Protocol
client in Perl as described in RFC1350. Net::TFTP also supports the
TFTP Option Extension (as described in RFC2347), with the following options

RFC2348 Blocksize Option

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc ChangeLog README
%{perl_vendorlib}/Net/TFTP.pm
%{_mandir}/*/*


%changelog
* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.190.0-1mdv2011.0
+ Revision: 601939
- update to new version 0.19

* Wed Jul 14 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.180.0-1mdv2011.0
+ Revision: 553023
- adding missing buildrequires:
- adding missing buildrequires:
- update to 0.18

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.170.0-1mdv2010.0
+ Revision: 404249
- rebuild using %0.1901 Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.17-4mdv2009.0
+ Revision: 258135
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.17-3mdv2009.0
+ Revision: 246192
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.17-1mdv2008.1
+ Revision: 140694
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Jul 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.17-1mdv2008.0
+ Revision: 56124
- new version

* Wed May 09 2007 Oden Eriksson <oeriksson@mandriva.com> 0.16-4mdv2008.0
+ Revision: 25452
- rebuild

* Tue May 08 2007 Olivier Thauvin <nanardon@mandriva.org> 0.16-3mdv2008.0
+ Revision: 25195
- rebuild


* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.16-2mdk
- Fix SPEC according to Perl Policy
	- Source URL
- use mkrel

* Wed Jul 13 2005 Oden Eriksson <oeriksson@mandriva.com> 0.16-1mdk
- initial Mandriva package

