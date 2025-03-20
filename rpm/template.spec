%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/jazzy/.*$
%global __requires_exclude_from ^/opt/ros/jazzy/.*$

Name:           ros-jazzy-sensor-msgs-py
Version:        5.3.6
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS sensor_msgs_py package

License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       python%{python3_pkgversion}-numpy
Requires:       ros-jazzy-sensor-msgs
Requires:       ros-jazzy-std-msgs
Requires:       ros-jazzy-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-jazzy-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  ros-jazzy-ament-copyright
BuildRequires:  ros-jazzy-ament-flake8
BuildRequires:  ros-jazzy-ament-pep257
%endif

%description
A package for easy creation and reading of PointCloud2 messages in Python.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/jazzy"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/jazzy

%changelog
* Thu Mar 20 2025 Tully Foote <tfoote@openrobotics.org> - 5.3.6-1
- Autogenerated by Bloom

* Wed Apr 24 2024 Tully Foote <tfoote@openrobotics.org> - 5.3.5-1
- Autogenerated by Bloom

* Thu Apr 18 2024 Tully Foote <tfoote@openrobotics.org> - 5.3.4-2
- Autogenerated by Bloom

* Tue Apr 16 2024 Tully Foote <tfoote@openrobotics.org> - 5.3.4-1
- Autogenerated by Bloom

* Wed Apr 10 2024 Tully Foote <tfoote@openrobotics.org> - 5.3.3-1
- Autogenerated by Bloom

* Wed Apr 10 2024 Tully Foote <tfoote@openrobotics.org> - 5.3.2-1
- Autogenerated by Bloom

* Thu Mar 28 2024 Tully Foote <tfoote@openrobotics.org> - 5.3.1-1
- Autogenerated by Bloom

* Wed Mar 06 2024 Tully Foote <tfoote@openrobotics.org> - 5.3.0-2
- Autogenerated by Bloom

* Wed Jan 24 2024 Tully Foote <tfoote@openrobotics.org> - 5.3.0-1
- Autogenerated by Bloom

* Tue Dec 26 2023 Tully Foote <tfoote@openrobotics.org> - 5.2.2-1
- Autogenerated by Bloom

* Mon Nov 06 2023 Tully Foote <tfoote@openrobotics.org> - 5.2.1-1
- Autogenerated by Bloom

* Wed Jun 07 2023 Tully Foote <tfoote@openrobotics.org> - 5.2.0-1
- Autogenerated by Bloom

* Thu Apr 27 2023 Tully Foote <tfoote@openrobotics.org> - 5.1.0-1
- Autogenerated by Bloom

* Tue Apr 11 2023 Tully Foote <tfoote@openrobotics.org> - 5.0.0-1
- Autogenerated by Bloom

* Tue Mar 21 2023 Tully Foote <tfoote@openrobotics.org> - 4.7.0-3
- Autogenerated by Bloom

