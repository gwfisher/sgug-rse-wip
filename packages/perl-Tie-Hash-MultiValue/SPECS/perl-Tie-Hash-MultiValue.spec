Name:           perl-Tie-Hash-MultiValue
Version:        1.05
Release:        6%{?dist}
Summary:        Store multiple values per key
# LICENSE defines "Perl itself" as GPLv2+ or Artistic, CPAN RT#125581
License:        GPLv2+ or Artistic
URL:            https://metacpan.org/release/Tie-Hash-MultiValue
Source0:        https://cpan.metacpan.org/authors/id/M/MC/MCMAHON/Tie-Hash-MultiValue-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(strict)
BuildRequires:  perl(Tie::Hash) >= 1
BuildRequires:  perl(vars)
# Tests:
# Test::More version from Test::Simple in META
BuildRequires:  perl(Test::More) >= 0.44
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Tie::Hash) >= 1

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Tie::Hash\\)$

%description
Tie::Hash::MultiValue Perl module allows you to have hashes which store their
values in anonymous arrays, appending any new value to the already-existing
ones.

%prep
%setup -q -n Tie-Hash-MultiValue-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README Todo
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.05-5
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.05-2
- Perl 5.28 rebuild

* Fri Jun 15 2018 Petr Pisar <ppisar@redhat.com> - 1.05-1
- 1.05 bump
- License changed to "GPLv2+ or Artistic"

* Fri Jun 15 2018 Petr Pisar <ppisar@redhat.com> - 1.03-1
- 1.03 bump

* Thu Jun 14 2018 Petr Pisar <ppisar@redhat.com> 1.02-1
- Specfile autogenerated by cpanspec 1.78.
