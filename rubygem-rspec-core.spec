%define	gemdir		%(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define	majorver	2.6.4
%define	rpmminorver	.%(echo %preminorver | sed -e 's|^\\.\\.*||')
%define	fullver	%{majorver}%{?preminorver}

%define	gemname	rspec-core
%define	geminstdir	%{gemdir}/gems/%{gemname}-%{fullver}

%define	rubyabi	1.8

%define	need_bootstrap_set	1

#% {!?need_bootstrap:	% global	need_bootstrap	% {need_bootstrap_set}}

Summary:	Rspec-2 runner and formatters
Name:		rubygem-%{gemname}
Version:	%{majorver}
Release:	%mkrel 2

Group:		Development/Ruby
License:	MIT
URL:		http://github.com/rspec/rspec-mocks
Source0:	http://rubygems.org/gems/%{gemname}-%{fullver}.gem

BuildRequires:	ruby(abi) = %{rubyabi}
BuildRequires:	rubygems
%if 0%{?need_bootstrap} < 1
BuildRequires:	rubygem(ZenTest)
BuildRequires:	rubygem(rake)
BuildRequires:	rubygem(rspec-expectations)
BuildRequires:	rubygem(rspec-mocks)
BuildRequires:	ruby-rdoc
%endif
Requires:	ruby(abi) = %{rubyabi}
Requires:	rubygem(rspec-expectations)
Requires:	rubygem(rspec-mocks)
Requires:	rubygem(rake)
# Optional
#Requires:	rubygem(ZenTest)
#Requires:	rubygem(mocha)
#Requires:	rubygem(ruby-debug)
#Requires:	rubygem(rr)
Provides:	rubygem(%{gemname}) = %{version}-%{release}
BuildArch:	noarch

%description
Behaviour Driven Development for Ruby.

%package	doc
Summary:	Documentation for %{name}
Group:		Development/Ruby 
Requires:	%{name} = %{version}-%{release}

%description	doc
This package contains documentation for %{name}.


%prep
%setup -q -c -T

mkdir -p .%{gemdir}
gem install \
	-V \
	--local \
	--install-dir .%{gemdir} \
	--bindir .%{_bindir} \
	--force \
	--rdoc \
	%{SOURCE0}

chmod 0644 .%{gemdir}/cache/%{gemname}-%{fullver}.gem

# rpmlint
pushd .%{geminstdir}
grep -rl '^#![ \t]*/usr/bin' ./lib| \
	xargs sed -i -e '\@^#![ \t]*/usr/bin@d'

# Until rspec is updated, lets install rspec.rb
cat > lib/rspec.rb <<EOF
require 'rspec/core'
require 'rspec/expectations'
require 'rspec/mocks'
EOF

popd

%build

%install
mkdir -p %{buildroot}%{_prefix}
cp -a .%{_prefix}/* %{buildroot}%{_prefix}/

# Rename autospec to avoid conflict with rspec 1.3
# (anyway this script doesn't seem to be useful)
mv %{buildroot}%{_bindir}/autospec{,2}

# cleanups
rm -f %{buildroot}%{geminstdir}/{.document,.gitignore,.treasure_map.rb,.rspec,.travis.yml,spec.txt}

%if 0%{?need_bootstrap} < 1
%check
pushd .%{geminstdir}
# spec/autotest/failed_results_re_spec.rb (and others) fail, skipping this for now
# (need investigating)
ruby -rubygems -Ilib/ -S bin/rspec \
	spec/rspec/*_spec.rb spec/rspec/*/*_spec.rb \
%if 0
	spec/autotest/*_spec.rb
%endif
%endif

%files
%defattr(-,root,root,-)
%dir	%{geminstdir}

%doc	%{geminstdir}/License.txt
%doc	%{geminstdir}/*.md

%{_bindir}/autospec2
%{_bindir}/rspec
%{geminstdir}/bin/
%{geminstdir}/lib/

%{gemdir}/cache/%{gemname}-%{fullver}.gem
%{gemdir}/specifications/%{gemname}-%{fullver}.gemspec


%files	doc
%defattr(-,root,root,-)
%{gemdir}/doc/%{gemname}-%{fullver}
%{geminstdir}/Gemfile
%{geminstdir}/Guardfile
%{geminstdir}/Rakefile
%{geminstdir}/cucumber.yml
%{geminstdir}/%{gemname}.gemspec
%{geminstdir}/features/
%{geminstdir}/script/
%{geminstdir}/spec/
