%define	gemdir		%(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define	majorver	2.8.0
%define	rpmminorver	.%(echo %preminorver | sed -e 's|^\\.\\.*||')
%define	fullver	%{majorver}%{?preminorver}

%define	gemname	rspec-core
%define	geminstdir	%{gemdir}/gems/%{gemname}-%{fullver}

%define	rubyabi	1.8

%define	need_bootstrap_set	0

%{!?need_bootstrap:	%global need_bootstrap %{need_bootstrap_set}}

Summary:	Rspec-2 runner and formatters
Name:		rubygem-%{gemname}
Version:	%{majorver}
Release:	5

Group:		Development/Ruby
License:	MIT
URL:		http://github.com/rspec/rspec-mocks
Source0:	http://rubygems.org/gems/%{gemname}-%{fullver}.gem

BuildRequires:	ruby(abi) = %{rubyabi}
BuildRequires:	rubygems
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

%files
%dir	%{geminstdir}
%dir	%{geminstdir}/exe/autospec
%dir	%{geminstdir}/exe
%dir	%{geminstdir}/exe/rspec

%doc	%{geminstdir}/License.txt
%doc	%{geminstdir}/*.md

%{_bindir}/autospec2
%{_bindir}/rspec
%{geminstdir}/lib/

%{gemdir}/cache/%{gemname}-%{fullver}.gem
%{gemdir}/specifications/%{gemname}-%{fullver}.gemspec


%files	doc
%{gemdir}/doc/%{gemname}-%{fullver}
#%{geminstdir}/Gemfile
#%{geminstdir}/Rakefile
#%{geminstdir}/cucumber.yml
#%{geminstdir}/%{gemname}.gemspec
%{geminstdir}/features/
#%{geminstdir}/script/
%{geminstdir}/spec/
