#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Date
%define	pnam	ICal
Summary:	Date::ICal - Perl extension for ICalendar date objects
Summary(pl):	Date::ICal - rozszerzenie Perla o obiekty czasu ICalendar
Name:		perl-Date-ICal
Version:	1.72
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	69e10541f5da09fc0f53474073da6744
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Date-Leapyear >= 1.03
BuildRequires:	perl-Storable
BuildRequires:	perl-Test-Simple >= 0.19
BuildRequires:	perl-Time-HiRes
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl module Date::ICal talks the ICal date format, and is intended to
be a base class for other date/calendar modules that know about ICal
time format also.

%description -l pl
Modu³ Perla Date::ICal komunikuje sie za pomoc± formatu daty ICal.
Jest on zaprojektowany jako klasa bazowa dla innych modu³ów
daty/kalendarza, rozumiej±cych ICal jako jeden z formatów czasu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%{perl_vendorlib}/Date/ICal.pm
%{perl_vendorlib}/Date/ICal
%{_mandir}/man3/*
