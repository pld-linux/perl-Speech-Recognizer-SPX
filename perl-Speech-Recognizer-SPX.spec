#
# Conditional build:
%bcond_with	tests	# perform "make test"
			# need working audio device access
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Speech
%define		pnam	Recognizer-SPX
Summary:	Speech::Recognizer::SPX Perl module - bindings for Sphinx-II
Summary(pl.UTF-8):	Moduł Perla Speech::Recognizer::SPX - dowiązania do Sphinx-II
Name:		perl-Speech-Recognizer-SPX
Version:	0.0801
Release:	10
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Speech/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7562fb69c09447fecd6e3e3343f906f5
URL:		http://search.cpan.org/dist/Speech-Recognizer-SPX/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	sphinx2-devel
Provides:	perl(Speech::Recognizer::SPX::Config)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a Perl interface to the Sphinx-II speech
recognizer library.

%description -l pl.UTF-8
Ten moduł udostępnia perlowy interfejs do biblioteki rozpoznawania
mowy Sphinx-II.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	--sphinx-prefix=/usr
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Audio/*.pm
%{perl_vendorarch}/Speech/Recognizer/SPX.pm
%{perl_vendorarch}/Speech/Recognizer/SPX
%dir %{perl_vendorarch}/auto/Audio/*
%attr(755,root,root) %{perl_vendorarch}/auto/Audio/*/*.so
%dir %{perl_vendorarch}/auto/Speech/Recognizer/SPX
%attr(755,root,root) %{perl_vendorarch}/auto/Speech/Recognizer/SPX/*.so
%{_mandir}/man3/*
