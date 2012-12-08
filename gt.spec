Name:		gt
Version:	0.4
Release:	3
Summary:	Modified Timidity which supportes enhanced gus format patches
Group:		Sound
License:	GPLv2+
URL:		http://alsa.opensrc.org/index.php/GusSoundfont
# This is ftp://ling.lll.hawaii.edu/pub/greg/gt-0.4.tar.gz
# with the examples/patch and sfz directories removed as the license of the
# samples in these dirs is unclear. Also the src/ac3* files have been removed
# as these contain patented code.
Source0:	%{name}-%{version}-clean.tar.gz
Patch0:		gt-0.4-noac3.patch
Patch1:		gt-0.4-compile-fix.patch
Patch2:		gt-0.4-optflags.patch
Patch3:		gt-0.4-config-default-velocity-layer.patch
Patch4:		gt-0.4-ppc-compile-fix.patch
Patch5:		gt-0.4-unsf-bigendian-fix.patch
Patch6:		gt-0.4-unsf-tremolo.patch
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	flex

%description
Modified timidity midi player which supportes enhanced gus format patches and
surround audio output.


%package -n soundfont-utils
Summary:        Utilities for converting from / to various soundfont formats
Group:          Sound

%description -n soundfont-utils
Utilities for converting from / to various soundfont formats and a midi file
disassembler.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
cp -p src/README README.timidity


%build
export CFLAGS="%{optflags} -fsigned-char"
%configure
%make

%install
%makeinstall_std
# rename somewhat genericly named dim to midi-disasm
mv %{buildroot}%{_bindir}/dim %{buildroot}%{_bindir}/midi-disasm
mv %{buildroot}%{_mandir}/man1/dim.1 \
   %{buildroot}%{_mandir}/man1/midi-disasm.1
sed -i 's/dim/midi-disasm/g' %{buildroot}%{_mandir}/man1/midi-disasm.1
touch -r utils/midifile.c %{buildroot}%{_mandir}/man1/midi-disasm.1
 
%files
%doc AUTHORS COPYING ChangeLog FEATURES NEWS README*
%{_bindir}/gt
%{_mandir}/man1/gt.1*

%files -n soundfont-utils
%doc utils/README* utils/GUSSF2-SPEC
%{_bindir}/*
%exclude %{_bindir}/gt
%{_mandir}/man1/*
%exclude %{_mandir}/man1/gt.1*

%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4-2mdv2011.0
+ Revision: 610989
- rebuild

* Thu Jan 28 2010 Emmanuel Andry <eandry@mandriva.org> 0.4-1mdv2010.1
+ Revision: 497773
- import gt


