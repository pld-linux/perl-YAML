# TODO
# - YAML::Types depends on B::Deparse therefore the perl-devel dep)
#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	YAML
Summary:	YAML - YAML Ain't Markup Language (tm)
Summary(pl.UTF-8):	YAML - YAML nie jest językiem znaczników
Name:		perl-YAML
Version:	1.11
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/YAML/%{pdir}-%{version}.tar.gz
# Source0-md5:	be1adf76064537fe4730f52aa9e02127
URL:		http://www.yaml.org/spec/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.59
BuildRequires:	perl-devel >= 1:5.8.1
%if %{with tests}
BuildRequires:	perl-Spiffy >= 0.29
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The YAML.pm module implements a YAML Loader and Dumper based on the
YAML 1.0 specification.

YAML is a generic data serialization language that is optimized for
human readability. It can be used to express the data structures of
most modern programming languages. (Including Perl!!!)

%description -l pl.UTF-8
Moduł YAML.pm jest implementacją klas YAML Loader i Dumper bazujących
na specyfikacji YAML 1.0. YAML to język do serializacji ogólnych
danych, zoptymalizowany pod względem czytelności dla człowieka. Może
być używany do wyrażania struktur danych większości współczesnych
języków programowania (włącznie z Perlem).

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# this pulls dozen of Test::* deps which we don't want
%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/Test/YAML.pm
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man3/Test::YAML.3pm*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/YAML.pm
%{perl_vendorlib}/YAML
%{_mandir}/man3/YAML.3pm*
%{_mandir}/man3/YAML::*.3pm*
