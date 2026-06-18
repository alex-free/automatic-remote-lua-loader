%global source_date_epoch_from_changelog 0

Name: arll
Version: v1.0
Summary: Send the remote lua loader exploit and latest payloads in one command from your computer.
Release: 1
License: BSD-3-Clause
URL: https://github.com/alex-free/automatic-remote-lua-loader
Packager: Alex Free
Requires: curl python3

%description
Send the remote lua loader exploit and latest payloads in one command from your computer.

%install
mkdir -p %{buildroot}/usr/bin
cp %{_sourcedir}/arll %{buildroot}/usr/bin/

%files
/usr/bin/arll
