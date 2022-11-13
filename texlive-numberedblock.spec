Name:		texlive-numberedblock
Epoch:		1
Version:	33109
Release:	1
Summary:	Print a block of code, with unique index number
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/numberedblock
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/numberedblock.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/numberedblock.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
