%global tl_name numberedblock
%global tl_revision 33109

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.10
Release:	%{tl_revision}.1
Summary:	Print a block of code, with unique index number
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/numberedblock
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/numberedblock.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/numberedblock.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package has been created for the convenience of the report writer;
it provides the means to number, and label, code-block snippets in your
document. In this way, you can (unambiguously) refer to each snippet
elsewhere in your document.

