# Automatically generated by Net-Server.spec.PL
%define perlmod Net-Server
%define version 0.84
%define release 1
%define defperlver 5.6.1

# Derived values
%define name perl-%{perlmod}
%define perlver %(rpm -q perl --queryformat '%%{version}' 2> /dev/null || echo %{defperlver})

# Provide perl-specific find-{provides,requires}.
%define __find_provides %( echo -n /usr/lib/rpm/find-provides && [ -x /usr/lib/rpm/find-provides.perl ] && echo .perl )
%define __find_requires %( echo -n /usr/lib/rpm/find-requires && [ -x /usr/lib/rpm/find-requires.perl ] && echo .perl )

Summary:        Perl module %{class}::%{subclass}
Name:           %{name}
Version:        %{version}
Release:        %{release}
Group:          Development/Perl
License:	Artistic
Source0:	http://seamons.com/net_server/%{perlmod}-%{version}.tar.gz
URL:		http://seamons.com/net_server.html
Vendor:		Paul Seamons <paul@seamons.com>
Packager:	Rob Brown <bbb@cpan.org>
BuildRequires:  perl
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-buildroot-%(id -u -n)
Requires:       perl = %{perlver}
Provides:       %{perlmod} = %{version}

%description
Net::Server is an extensible, class oriented module written in perl
and intended to be the back end layer of internet protocol servers.

%prep
%setup -q -n %{perlmod}-%{version}

%build
%{__perl} Makefile.PL
%{__make} OPTIMIZE="$RPM_OPT_FLAGS"
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall} PREFIX=$RPM_BUILD_ROOT%{_prefix}
[ -x /usr/lib/rpm/brp-compress ] && /usr/lib/rpm/brp-compress
# Clean up some files we don't want/need
rm -rf `find $RPM_BUILD_ROOT -name "perllocal.pod" -o -name ".packlist" -o -name "*.bs"`
find $RPM_BUILD_ROOT%{_prefix} -type d | tac | xargs rmdir --ign

%clean
rm -rf $RPM_BUILD_ROOT
HERE=`pwd`
cd ..
rm -rf $HERE

%files
%defattr(-,root,root)
%doc README Changes examples
%{_prefix}

%changelog
* Wed May 22 2002 Rob Brown <bbb@cpan.org>
- RedHat style spec.
- It is noarch because it is implemented in pure perl
  (even including safe signal handling code).
- Include upper directories too for cleaner and
  safer rpm uninstall.
- Perl module provides and requires dependencies.
* Sat Apr 17 2002 Rob Brown <bbb@cpan.org>
- initial creation
