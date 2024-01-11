# Force out of source build
%undefine __cmake_in_source_build

%global archivename ldacBT
%global sonamebase 2

Name:           libldac
Version:        %{sonamebase}.0.2.3
Release:        10%{?dist}
Summary:        A lossy audio codec for Bluetooth connections

License:        ASL 2.0
URL:            https://github.com/EHfive/ldacBT
Source0:        %{url}/releases/download/v%{version}/%{archivename}-%{version}.tar.gz

# Upstream source throws error in a big-endian arch, see #1677491
ExcludeArch:    s390x

BuildRequires:  cmake3
BuildRequires:  gcc

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description
LDAC is an audio coding technology developed by Sony.
It enables the transmission of High-Resolution Audio content,
even over a Bluetooth connection.

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{archivename}

%build
%cmake3 \
    -DLDAC_SOFT_FLOAT=OFF \
    -DINSTALL_LIBDIR=%{_libdir}

%cmake3_build

%install
%cmake3_install

%ldconfig_scriptlets

%files
%license LICENSE
%{_libdir}/libldacBT_abr.so.%{sonamebase}
%{_libdir}/libldacBT_abr.so.%{sonamebase}.*
%{_libdir}/libldacBT_enc.so.%{sonamebase}
%{_libdir}/libldacBT_enc.so.%{sonamebase}.*
%{_libdir}/libldacBT_abr.so
%{_libdir}/libldacBT_enc.so

%files devel
%dir %{_includedir}/ldac
%{_includedir}/ldac/ldacBT_abr.h
%{_includedir}/ldac/ldacBT.h
%{_libdir}/pkgconfig/ldacBT-abr.pc
%{_libdir}/pkgconfig/ldacBT-enc.pc

%changelog
* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 2.0.2.3-10
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 2.0.2.3-9
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Gergely Gombos <gombosg@disroot.org> - 2.0.2.3-7
- Fix cmake out-of-source FTBFS for F33/rawhide

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 8 2019 Gergely Gombos <gombosg@gmail.com> - 2.0.2.3-3
- Move unversioned symlinks to the base package. Linked packages dynamically load (dlopen) this module with the name libldacBT_enc.so.

* Tue Feb 19 2019 Gergely Gombos <gombosg@gmail.com> - 2.0.2.3-2
- Fixed changelog

* Tue Feb 19 2019 Gergely Gombos <gombosg@gmail.com> - 2.0.2.3-1
- Bump to 2.0.2.3, upgrade .gitignore

* Fri Feb 15 2019 Gergely Gombos <gombosg@gmail.com> - 2.0.2.2-4
- Add s390x ExcludeArch

* Thu Feb 7 2019 Gergely Gombos <gombosg@gmail.com> - 2.0.2.2-3
- Minor fixes before Fedora submission

* Wed Jan 30 2019 Gergely Gombos <gombosg@gmail.com> - 2.0.2.2-2
- Fix package reviewer suggestions

* Tue Jan 29 2019 Gergely Gombos <gombosg@gmail.com> - 2.0.2.2-1
- Update to 2.0.2.2, fix file listing

* Sun Jan 27 2019 Gergely Gombos <gombosg@gmail.com>
- Rename to libldac, prepare for RPMFusion submission

* Sun Dec 16 2018 Gergely Gombos <gombosg@gmail.com>
- Packaged 1.1
