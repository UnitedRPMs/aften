Name:           aften
Version:	0.0.8
Release:	2%{?dist}
License:	GPLv2+ and LGPLv2+ and BSD
Summary:	Audio encoder which generates compressed audio streams based on ATSC A/52 specification
Url:		http://aften.sourceforge.net/
Group:		Applications/Multimedia
Source: 	http://downloads.sourceforge.net/aften/%{name}-%{version}.tar.bz2

BuildRequires:	cmake
BuildRequires:	gcc

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Aften is an audio encoder which generates compressed audio streams based 
on ATSC A/52 specification. This type of audio is also known as AC-3 or 
Dolby® Digital and is one of the audio codecs used in DVD-Video content. 

%package 	devel
Summary:	Development files for Aften
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}

%description 	devel
This package contains development files for aften.


%prep
%setup -q 
# fix for x86_64 build
sed -i -e "s|DESTINATION lib|DESTINATION %{_lib}|g" CMakeLists.txt

%build
mkdir build
cd build

cmake   -DCMAKE_INSTALL_PREFIX:STRING=%{_prefix} \
	-DSHARED:STRING="yes" ..

make %{?_smp_mflags}

%install
cd build
make install DESTDIR=%{buildroot}


%files
%defattr(755, root, root)
%{_bindir}/aften
%{_bindir}/wavfilter
%{_bindir}/wavinfo
%{_bindir}/wavrms
%{_libdir}/libaften.so.0
%{_libdir}/libaften.so.0.0.8

%files devel
%{_libdir}/libaften.so
%{_includedir}/%{name}/*.h


%changelog

* Wed Aug 31 2016 <davidjeremias82 AT gmail DOT com> 0.0.8-2
- Fixed libdir path

* Fri Aug 16 2013 <davidjeremias82 AT gmail DOT com> 0.0.8-1
- initial rpm for Fedora
