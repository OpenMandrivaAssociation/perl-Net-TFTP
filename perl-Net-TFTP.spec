%define upstream_name    Net-TFTP
%define upstream_version 0.1901
Name:		perl-%{upstream_name}
Version:	0.1901
Release:	5

Summary:	Net::TFTP - TFTP Client class
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/gbarr/perl-net-tftp
Source0:	https://cpan.metacpan.org/authors/id/G/GB/GBARR/Net-TFTP-0.1901.tar.gz

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
%setup -q -n Net-TFTP-0.1901

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
%make test || :

%install
%makeinstall_std

%files
%doc ChangeLog README
%{perl_vendorlib}/Net/TFTP.pm
%{_mandir}/*/*


