%define	pdir	Date
%define	pnam	ICal
%include	/usr/lib/rpm/macros.perl
Summary:	Perl extension for ICalendar date objects
Summary(pl):	Modu³ perla Date-ICal
Name:		perl-Date-ICal
Version:	1.67
Release:	3

License:	?
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl extension for ICalendar date objects.

%description -l pl
Rozszerzenie perla do obiektów danych ICalendar.

%prep
%setup -q -n Date-ICal-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README Changes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Date/ICal.pm
%{perl_sitelib}/Date/ICal
%{_mandir}/man3/*
