# Generated from rspec-core-2.8.0.gem by gem2rpm5 0.6.7 -*- rpm-spec -*-
%define	rbname	rspec-core

Summary:	rspec-core-2.8.0
Name:		rubygem-%{rbname}

Version:	2.8.0
Release:	5
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://github.com/rspec/rspec-core
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
BDD for Ruby. RSpec runner and example groups.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build -f '(features|spec)'

%install
%gem_install

%files
%{_bindir}/autospec
%{_bindir}/rspec
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/exe
%{ruby_gemdir}/gems/%{rbname}-%{version}/exe/autospec
%{ruby_gemdir}/gems/%{rbname}-%{version}/exe/rspec
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%{ruby_gemdir}/doc/%{rbname}-%{version}
%{ruby_gemdir}/gems/%{rbname}-%{version}/*.md
%{ruby_gemdir}/gems/%{rbname}-%{version}/*.txt
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/features
%{ruby_gemdir}/gems/%{rbname}-%{version}/features/*
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/spec
%{ruby_gemdir}/gems/%{rbname}-%{version}/spec/*
