# ESDLang

This is the library part of ESDLang. It's mainly used for AST-based expression manipulation.

See `Script` for esdtool.exe routines.

## Library usage

As a library, ESDLang merges in the
[ESD SoulsFormats fork](https://github.com/Meowmaritus/SoulsFormats/tree/ac189baa87099a5821d6af174495d27b635d8fa9/SoulsFormats/Formats/ESD)
to work with [SoulsFormats](https://github.com/JKAnderson/SoulsFormats) at head, with some extra features for more powerful
expression manipulation. The forked library was itself based on combining SoulsFormats with [EzSembler](https://github.com/JKAnderson/EzSembler).
The postfix format was originally reverse engineered in the
[ezstate](https://github.com/grimrhapsody/ezstate) python library, with a succint summary in
[this gist](https://gist.github.com/JKAnderson/e3fd38d4efd5f3350e13a613319b8bed).
Many folks have contributed to investigation since then for figuring out opcodes and function/command names.

There is an alternative to the SoulsFormats.ESD class called ESDLang.Adapter.ESDL which implements many of the same methods, but is not a SoulsFile.
If you were previously using the ESD from forked SoulsFormats, you should be able to just search and replace all references from one to the other, and it should work.
Newer applications should probably prefer to use SoulsFormats ESD with the EzSemble classes - since the EzSemble API has been migrated to work with SoulsFormats at head - but tbd on the best way to do that.

## Byte-perfect writes

Using the ESDLang.EzSemble.AST constructs, it is possible to dissemble an ESD expression/command and then write back the exact same bytes during assembly,
so long as you hold onto the original Expr objects or can fully reproduce them.

The bytes will *not* necessarily be the same if you serialize the AST classes using ToString and then try to parse the string back when assembling.
But even in that case, the only difference is that all continue-if-false instructions are discarded, because they are both very ubiquitous and very inconsistently used.
As far as I know, there is no in-game behavior difference from this bytecode change.
