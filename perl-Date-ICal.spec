#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Date
%define	pnam	ICal
Summary:	Perl extension for ICalendar date objects
Summary(pl):	Modu³ perla Date::ICal
Name:		perl-Date-ICal
Version:	1.70
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-Date-Leapyear >= 1.03
BuildRequires:	perl-Storable
BuildRequires:	perl-Test-Simple >= 0.19
BuildRequires:	perl-Time-HiRes
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl extension for ICalendar date objects.

%description -l pl
Rozszerzenie perla do obiektów danych ICalendar.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%{perl_sitelib}/Date/ICal.pm
%{perl_sitelib}/Date/ICal
%{_mandir}/man3/*
