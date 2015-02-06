%define rbname rspec-core

Summary:	RSpec runner and example groups
Name:		rubygem-%{rbname}
Version:	3.1.4
Release:	2
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
%dir %{gem_dir}/gems/%{rbname}-%{version}
%dir %{gem_dir}/gems/%{rbname}-%{version}/exe
%{gem_dir}/gems/%{rbname}-%{version}/exe/rspec
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/
%{gem_dir}/gems/%{rbname}-%{version}/lib/*
%{gem_dir}/specifications/%{rbname}-%{version}.gemspec

#----------------------------------------------------------------------------

%package doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{EVRD}

%description doc
Documents, RDoc & RI documentation for %{name}.

%files doc
%{gem_dir}/doc/%{rbname}-%{version}

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%gem_build -f '(features|spec)'

%install
%gem_install

