# Created by pyp2rpm-3.3.3
%global pypi_name ansible

Name:           python-%{pypi_name}
Version:        2.9.10
Release:        1%{?dist}
Summary:        Radically simple IT automation

License:        GPLv3+
URL:            https://ansible.com/
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-PyYAML
Requires:       python3-cryptography
Requires:       python3-jinja2
Requires:       python3-packaging
Requires:       python3-requests
Requires:       python3-xmltodict

%description -n python3-%{pypi_name}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license docs/docsite/rst/community/contributor_license_agreement.rst lib/ansible/modules/cloud/vmware/vcenter_license.py lib/ansible/modules/network/cumulus/_cl_license.py lib/ansible/modules/network/f5/bigip_device_license.py lib/ansible/modules/network/f5/bigiq_regkey_license.py lib/ansible/modules/network/f5/bigiq_regkey_license_assignment.py lib/ansible/modules/network/f5/bigiq_utility_license.py lib/ansible/modules/network/f5/bigiq_utility_license_assignment.py lib/ansible/modules/storage/netapp/_na_cdot_license.py lib/ansible/modules/storage/netapp/na_ontap_license.py licenses/Apache-License.txt licenses/MIT-license.txt licenses/PSF-license.txt test/units/modules/network/f5/fixtures/load_regkey_license_key.json test/units/modules/network/f5/fixtures/load_regkey_license_pool.json test/units/modules/network/f5/test_bigip_device_license.py test/units/modules/network/f5/test_bigiq_regkey_license.py test/units/modules/network/f5/test_bigiq_regkey_license_assignment.py test/units/modules/network/f5/test_bigiq_utility_license.py test/units/modules/network/f5/test_bigiq_utility_license_assignment.py
%doc contrib/README.md docs/docsite/README.md lib/ansible/galaxy/data/apb/README.md lib/ansible/galaxy/data/container/README.md lib/ansible/galaxy/data/default/collection/plugins/README.md.j2 lib/ansible/galaxy/data/default/collection/README.md.j2 lib/ansible/galaxy/data/default/role/README.md lib/ansible/galaxy/data/network/README.md packaging/arch/README.md packaging/debian/README.md packaging/gentoo/README.md packaging/macports/README.md test/integration/targets/cnos_backup/README.md test/integration/targets/cnos_bgp/README.md test/integration/targets/cnos_command/README.md test/integration/targets/cnos_conditional_command/README.md test/integration/targets/cnos_conditional_template/README.md test/integration/targets/cnos_config/README.md test/integration/targets/cnos_facts/README.md test/integration/targets/cnos_image/README.md test/integration/targets/cnos_rollback/README.md test/integration/targets/cnos_save/README.md test/integration/targets/cnos_showrun/README.md test/integration/targets/cnos_template/README.md test/integration/targets/cnos_vlag/README.md test/integration/targets/enos_command/README.md test/integration/targets/enos_config/README.md test/integration/targets/enos_facts/README.md test/integration/targets/k8s/README.md test/integration/targets/setup_flatpak_remote/README.md test/integration/targets/vault/invalid_format/README.md test/integration/targets/vault/roles/test_vault_file_encrypted_embedded/README.md test/integration/targets/win_copy/files-different/vault/readme.txt test/units/cli/test_data/collection_skeleton/README.md test/units/cli/test_data/role_skeleton/README.md README.rst docs/docsite/rst/dev_guide/shared_snippets/licensing.txt
%exclude %{_bindir}/ansible
%exclude %{_bindir}/ansible-config
%exclude %{_bindir}/ansible-connection
%exclude %{_bindir}/ansible-console
%exclude %{_bindir}/ansible-doc
%exclude %{_bindir}/ansible-galaxy
%exclude %{_bindir}/ansible-inventory
%exclude %{_bindir}/ansible-playbook
%exclude %{_bindir}/ansible-pull
%exclude %{_bindir}/ansible-test
%exclude %{_bindir}/ansible-vault
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/ansible_test
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Jun 23 2020 Evgeni Golov - 2.9.10-1
- Initial package.
