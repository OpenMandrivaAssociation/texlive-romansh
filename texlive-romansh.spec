# revision 25956
# category Package
# catalog-ctan /macros/latex/contrib/babel-contrib/romansh
# catalog-date 2012-04-13 15:00:06 +0200
# catalog-license lppl1.3
# catalog-version undef
Name:		texlive-romansh
Version:	20120413
Release:	11
Summary:	Babel/Polyglossia support for the Romansh language
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/romansh
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/romansh.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/romansh.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/romansh.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a language description file that enables
support of Romansh either with babel or with polyglossia.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/romansh/romansh.ldf
%doc %{_texmfdistdir}/doc/latex/romansh/romansh.pdf
#- source
%doc %{_texmfdistdir}/source/latex/romansh/romansh.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Fri Aug 10 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120413-2
+ Revision: 813744
- Update to latest release.
- Import texlive-romansh
- Import texlive-romansh

