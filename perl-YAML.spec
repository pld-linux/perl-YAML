#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	YAML
Summary:	YAML - YAML Ain't Markup Language (tm)
Summary(pl.UTF-8):   YAML - YAML nie jest językiem znaczników
Name:		perl-YAML
Version:	0.62
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/I/IN/INGY/%{pdir}-%{version}.tar.gz
# Source0-md5:	4be042a043ec520074b0ab6f7ca0bded
URL:		http://www.yaml.org/spec/
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-perldoc
BuildRequires:	perl-Spiffy >= 0.29
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The YAML.pm module implements a YAML Loader and Dumper based on the
YAML 1.0 specification.

YAML is a generic data serialization language that is optimized for
human readability. It can be used to express the data structures of
most modern programming languages.  (Including Perl!!!)

%description -l pl.UTF-8
Moduł YAML.pm jest implementacją klas YAML Loader i Dumper bazujących
na specyfikacji YAML 1.0. YAML to język do serializacji ogólnych
danych, zoptymalizowany pod względem czytelności dla człowieka. Może
być używany do wyrażania struktur danych większości współczesnych
języków programowania (włącznie z Perlem).

%prep
%setup -q -n %{pdir}-%{version}

%build
yes | perl Makefile.PL \
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
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/*.pm
%{perl_vendorlib}/%{pdir}
%{_mandir}/man[13]/*
