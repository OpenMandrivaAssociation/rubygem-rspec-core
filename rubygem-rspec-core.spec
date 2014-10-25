%define rbname rspec-core

Summary:	RSpec runner and example groups
Name:		rubygem-%{rbname}
Version:	3.1.4
Release:	1
License:	GPLv2+ or Ruby
Group:		Development/Ruby
URL:		http://github.com/rspec/rspec-core
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems
BuildArch:	noarch

%description
BDD for Ruby. RSpec runner and example groups.

%files
%{_bindir}/rspec
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/exe
%{ruby_gemdir}/gems/%{rbname}-%{version}/exe/rspec
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

#----------------------------------------------------------------------------

%package doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{EVRD}

%description doc
Documents, RDoc & RI documentation for %{name}.

%files doc
%{ruby_gemdir}/doc/%{rbname}-%{version}

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%gem_build -f '(features|spec)'

%install
%gem_install

