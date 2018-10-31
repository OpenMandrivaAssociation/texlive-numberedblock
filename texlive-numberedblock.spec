# revision 33109
# category Package
# catalog-ctan /macros/latex/contrib/numberedblock
# catalog-date 2014-03-06 18:55:44 +0100
# catalog-license lppl1.3
# catalog-version 1.10
Name:		texlive-numberedblock
Epoch:		1
Version:	1.10
Release:	6
Summary:	Print a block of code, with unique index number
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/numberedblock
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/numberedblock.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/numberedblock.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package has been created for the convenience of the report
writer; it provides the means to number, and label, code-block
snippets in your document. In this way, you can (unambiguously)
refer to each snippet elsewhere in your document.

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
