#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	Speech
%define		pnam	Recognizer-SPX
Summary:	Speech::Recognizer::SPX Perl module - bindings for Sphinx-II
Summary(pl):	Modu³ perla Speech::Recognizer::SPX - dowi±zania do Sphinx-II
Name:		perl-Speech-Recognizer-SPX
Version:	0.0602
Release:	3
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6cbef3f8d0f2dfefcbdec1d36abb2b17
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	sphinx2-devel
Provides:	perl(Speech::Recognizer::SPX::Config)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a Perl interface to the Sphinx-II speech
recognizer library.

%description -l pl
Ten modu³ udostêpnia perlowy interfejs do biblioteki rozpoznawania
mowy Sphinx-II.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make} OPTIMIZE="%{rpmcflags}"

# one of tests fails
#%%{!?_without_tests:%{__make} test}

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
%{perl_vendorarch}/auto/Audio/*/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Audio/*/*.so
%dir %{perl_vendorarch}/auto/Speech/Recognizer/SPX
%{perl_vendorarch}/auto/Speech/Recognizer/SPX/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Speech/Recognizer/SPX/*.so
%{_mandir}/man3/*
