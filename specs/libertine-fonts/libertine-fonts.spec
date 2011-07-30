# $Id$
# Authority: shuff
# Upstream: <gillian$linuxlibertine,org>

%define real_name LinLibertine
%define release_minor 2
%define release_date 2011_06_21

%{?rh7:%define _without_fontconfig 1}
%{?el2:%define _without_fontconfig 1}

Summary: Free alternative to Times New Roman
Name: libertine-fonts
Version: 5.1.3
Release: 1%{?dist}
License: SIL Open Font License
Group: User Interface/X
URL: http://www.linuxlibertine.org/

Source: http://dl.sf.net/project/linuxlibertine/linuxlibertine/%{version}-%{release_minor}/LinLibertineTTF_%{version}_%{release_date}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
%{!?_without_fontconfig:Requires: fontconfig}

Provides: LinLibertine = %{version}
Provides: LinBiolinum = %{version}

%description
Linux Libertine is designed to give you an alternative for fonts like T*mes New
Roman. We're creating free software and publish our fonts under terms of the
GPL and OFL.

It is our aim to support the many western languages and provide many special
characters. Our fonts cover the codepages of Western Latin, Greek, Cyrillic
(with their specific enhancements), Hebrew, IPA and many more. Furthermore,
typographical features such as ligatures, small capitals, different number
styles, scientific symbols, etc. are implemented in this font. Linux Libertine
thus contains more than 2000 characters.

%prep
%setup -c %{name}-%{version}

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_datadir}/fonts/libertine/
%{__install} -p -m0644 *.ttf %{buildroot}%{_datadir}/fonts/libertine/

%post
%{_bindir}/fc-cache %{_datadir}/fonts/ 2>/dev/null || :

%postun
if [ $1 -eq 0 ]; then
    %{_bindir}/fc-cache %{_datadir}/fonts/ 2>/dev/null || :
fi

%files
%defattr(-, root, root, 0755)
%doc Bugs.txt ChangeLog.txt GPL.txt INSTALL.txt LICENCE.txt OFL.txt README
%{_datadir}/fonts/libertine/

%changelog
* Wed Jun 29 2011 Steve Huff <shuff@vecna.org> - 5.1.3-1
- Initial package.
