# Generated from hammer_cli_foreman_kubevirt-0.1.0.gem by gem2rpm -*- rpm-spec -*-
# template: hammer_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name hammer_cli_foreman_kubevirt
%global plugin_name foreman_kubevirt

%{!?_root_sysconfdir:%global _root_sysconfdir %{_sysconfdir}}
%global hammer_confdir %{_root_sysconfdir}/hammer

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.1.4
Release: 2%{?foremandist}%{?dist}
Summary: Foreman kubevirt commands for Hammer CLI
Group: Development/Languages
License: GPLv3
URL: https://github.com/theforeman/hammer-cli-foreman-kubevirt
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(gettext) >= 3.1.3
Requires: %{?scl_prefix}rubygem(gettext) < 4.0.0
Requires: %{?scl_prefix}rubygem(hammer_cli_foreman) >= 0.17.0
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

%description
Foreman kubevirt commands for Hammer CLI.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{hammer_confdir}/cli.modules.d
install -m 0644 .%{gem_instdir}/config/%{plugin_name}.yml \
                %{buildroot}%{hammer_confdir}/cli.modules.d/%{plugin_name}.yml

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%config %{hammer_confdir}/cli.modules.d/%{plugin_name}.yml
%license %{gem_instdir}/LICENSE
%{gem_instdir}/config

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md


%changelog
* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.1.4-2
- Rebuild plugins for Ruby 2.7

* Thu Mar 19 2020 Shira Maximov <shiramaximov@gmail.com> 0.1.4-1
- Update to 0.1.4

* Wed May 22 2019 Shira Maximov <shiramaximov@gmail.com> 0.1.3-1
- Update to 0.1.3

* Sun May 19 2019 Shira Maximov <shiramaximov@gmail.com> 0.1.2-1
- Update to 0.1.2

* Sun May 19 2019 Shira Maximov <shiramaximov@gmail.com> 0.1.1-1
- Update to 0.1.1

* Wed May 15 2019 Shira Maximov <shiramaximov@gmail.com> 0.1.0-1
- Add rubygem-hammer_cli_foreman_kubevirt generated by gem2rpm using the hammer_plugin template

