#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-EV
Version  : 4.33
Release  : 14
URL      : https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/EV-4.33.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/EV-4.33.tar.gz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0 BSD-2-Clause GPL-1.0
Requires: perl-EV-license = %{version}-%{release}
Requires: perl-EV-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Canary::Stability)
BuildRequires : perl(common::sense)

%description
NAME
EV - perl interface to libev, a high performance full-featured event
loop
SYNOPSIS
use EV;

# TIMERS

my $w = EV::timer 2, 0, sub {
warn "is called after 2s";
};

my $w = EV::timer 2, 2, sub {
warn "is called roughly every 2s (repeat = 2)";
};

undef $w; # destroy event watcher again

my $w = EV::periodic 0, 60, 0, sub {
warn "is called every minute, on the minute, exactly";
};

# IO

my $w = EV::io *STDIN, EV::READ, sub {
my ($w, $revents) = @_; # all callbacks receive the watcher and event mask
warn "stdin is readable, you entered: ", <STDIN>;
};

# SIGNALS

my $w = EV::signal 'QUIT', sub {
warn "sigquit received\n";
};

# CHILD/PID STATUS CHANGES

my $w = EV::child 666, 0, sub {
my ($w, $revents) = @_;
my $status = $w->rstatus;
};

# STAT CHANGES
my $w = EV::stat "/etc/passwd", 10, sub {
my ($w, $revents) = @_;
warn $w->path, " has changed somehow.\n";
};

# MAINLOOP
EV::run;                # loop until EV::break is called or all watchers stop
EV::run EV::RUN_ONCE;   # block until at least one event could be handled
EV::run EV::RUN_NOWAIT; # try to handle same events, but do not block

%package dev
Summary: dev components for the perl-EV package.
Group: Development
Provides: perl-EV-devel = %{version}-%{release}
Requires: perl-EV = %{version}-%{release}

%description dev
dev components for the perl-EV package.


%package license
Summary: license components for the perl-EV package.
Group: Default

%description license
license components for the perl-EV package.


%package perl
Summary: perl components for the perl-EV package.
Group: Default
Requires: perl-EV = %{version}-%{release}

%description perl
perl components for the perl-EV package.


%prep
%setup -q -n EV-4.33
cd %{_builddir}/EV-4.33

%build
## build_prepend content
# Avoid being prompted by ExtUtils::MakeMaker or Canary::Stability
export PERL_MM_USE_DEFAULT=1
export PERL_CANARY_STABILITY_NOPROMPT=1
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-EV
cp %{_builddir}/EV-4.33/COPYING %{buildroot}/usr/share/package-licenses/perl-EV/8ef1d59d0a0dbdae691da831bd9afb7cb7cdf5a1
cp %{_builddir}/EV-4.33/libev/LICENSE %{buildroot}/usr/share/package-licenses/perl-EV/10e633ee2e9f8a961554d0d579f03a1d0755ff3b
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/EV.3
/usr/share/man/man3/EV::MakeMaker.3
/usr/share/man/man3/EV::libev.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-EV/10e633ee2e9f8a961554d0d579f03a1d0755ff3b
/usr/share/package-licenses/perl-EV/8ef1d59d0a0dbdae691da831bd9afb7cb7cdf5a1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/EV.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/EV/EVAPI.h
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/EV/MakeMaker.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/EV/ev.h
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/EV/libev.pod
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/EV/EV.so
