# revision 29447
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-numberedblock
Version:	20131010
Release:	4
Summary:	TeXLive numberedblock package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/numberedblock.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/numberedblock.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive numberedblock package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/numberedblock/numberedblock.sty
%doc %{_texmfdistdir}/doc/latex/numberedblock/README
%doc %{_texmfdistdir}/doc/latex/numberedblock/testnumberedblock.pdf
%doc %{_texmfdistdir}/doc/latex/numberedblock/testnumberedblock.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
