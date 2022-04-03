# ESDLang

ESDLang is a high-level language for viewing and editing ESD scripts, primarily to understand NPC quests and interactions,
make significant quest edits, and add convenience features to bonfires.
It decompiles ESD files into a subset of Python. These Python files cannot be executed as Python. They can only be recompiled.

DS1, DS2, Bloodborne, DS3, Sekiro, and Elden Ring are supported. See game dumps in the examples/ directory.

**For Sekiro and Elden Ring, copy oo2core_6_win64.dll from your game directory into the esdtool directory.**

## Running esdtool.exe

There are two officially supported ways to run esdtool.exe:

1. Drag and drop files into the esdtool.exe program. This tries to construct command line arguments automatically.

   See [Drag and Drop](#drag-and-drop).

2. Open a command line console, navigate to the esdtool directory, and run esdtool.exe as a command line program.

   See [Command Line Arguments](#command-line-arguments).

Double-clicking on esdtool.exe won't do anything. It needs arguments.

## ESD overview

An ESD is composed of a set of state machines. Each machine has states which explicitly transition to each other, including a unique entry state (id 0).
In Bloodborne and onwards, machines may call each other as subroutines.

In ESDLang, each machine is represented as a Python function.
Connected states are turned into if-else statements, loops, and straight-line code.
This is different from how FromSoft developers created it (using a graphical state machine editor).

```py
def t130800_x11(val5=12):
    call = t130800_x24()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5:
        assert t130800_x2()
    return 0
```

### Conditions

If-else statements always wait for one of the branches to become true. They always choose the first such branch.

For example, suppose you want to award an item only if an event flag was previously false, then continue executing the script.

```py
# If the flag is off
if EventFlag(9999) == 0:
    # Award the item and turn the flag on
    AwardItemLot(1100010)
    SetEventFlag(9999, 1)
else:
    pass
# Set a different flag after, say
SetEventFlag(7777, 1)
```

Note the `else pass`! Without this, the script might be stuck forever waiting for the condition to become true. This is because at least one of the branches must be true to continue. The `else` branch has no condition so it's always eligible for this (it's equivalent to `elif True`). `pass` just means "do nothing" in Python. Effectively, if statements are lists of possible transitions to other states, and the state machine will wait until one of the transition conditions is met.

On the other hand, suppose you always want to wait for a condition to become true. That could be implemented with a single-branch if statement. Alternatively, ESDLang uses the `assert [condition]` statement for this common use case. These two snippets are equivalent:

```py
assert CheckSpecificPersonTalkHasEnded(0) == 1
SetEventFlag(5119, 1)
# Other commands after this
```
```py
if CheckSpecificPersonTalkHasEnded(0) == 1:
    SetEventFlag(5119, 1)
    # Other commands after this
```

### Machine calls

Machines may also call other machines. This behavior is complicated.

In normal programming languages, when functions call other functions, the parent function is suspended while it waits for the child to return a result.
This is not so in ESDs. If there are a chain of 5 machine calls, all 5 of them can run and change states simultaneously.
Additionally, machines may only have one child machine active at a time.
If a parent calls a new machine during a preexisting call, the preexisting call is interrupted and abandoned.
This is used when NPCs die and it interrupts everything else so they can say a death line or otherwise cease interacting normally with the player.

However, most calls manually wait for the child to finish. They do this, of course, using conditions.
There is a special condition, represented as `call.Done()` in ESDLang, which only becomes true when the child has issued a `return [number]` statement.
`assert` is used as shorthand for this too. These two snippets are equivalent:

```py
assert t800006000_x80()
AddTalkListData(1, 20000010, -1)
# Other commands after this
```
```py
call = t800006000_x80()
if call.Done():
    AddTalkListData(1, 20000010, -1)
    # Other commands after this
```

One thing to watch out for is that `call.Done()` only becomes true if the child has an explicit `return [number]` statement.
Otherwise, the "I'm done" value is never set and the parent never notices.
The child can alternatively return a specific result with `return [number]` which the parent can access using `call.Get()`.

### Loops and gotos

Infinite loops are another form of control flow, with breaks and continues within the loop. These can be written as `while True`, or alternatively `while Loop('<loop name>')` to identify loops for multi-level breaks and continues. These basically behave the same way as while loops in most programming languages.

```py
def t150270_x31():
    c1_110()
    while True:
        ClearTalkListData()
        # action:15027000:Ask about the village
        AddTalkListData(1, 15027000, -1)
        # action:15027001:Ask about the villagers
        AddTalkListData(2, 15027001, -1)
        # action:15027002:Ask about the village priest
        AddTalkListDataIf(GetEventStatus(71500007) == 1, 3, 15027002, -1)
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        if GetTalkListEntryResult() == 1:
            # talk:27010200:What is wrong with this village?
            assert t150270_x4(text10=27010200, z6=71500007, flag19=0, mode13=1)
        elif GetTalkListEntryResult() == 2:
            # talk:27010300:What is wrong with the villagers?
            assert t150270_x5(text1=27010300, flag18=0, mode12=1)
        elif GetTalkListEntryResult() == 3:
            # talk:27010400:Tell me about the priest.
            assert t150270_x5(text1=27010400, flag18=0, mode12=1)
        else:
            return 0
```

Because ESDs come from proper state machines, they can't always be broken down into conditionals/loops, so Goto is also available. This is not needed in most machines but is prolific in others.

### States

You may notice many "State [number]" docstrings in compilation output. This is the internal representation of the different distinct states the
state machine can be in. It's used during compilation to avoid significantly restructuring existing machines.
If you're adding new commands, you can basically ignore this.

Some notable options to make decompilation output more or less readable:

* Disable state docstrings altogether with `-nostateinfo`
* Disable adding unused states with `-nodeadstates`. These appear under the "Unused" docstring. They are never accessed in-game but are part of the machine nonetheless. In theory, removing them should have no effect.
* For others, see "Compilation options" command line flags below

## Drag and drop

You can drag different types of files into esdtool.exe to compile/decompile ESDs.
In all cases, esdtool.exe needs to know which game you're modifying and where it's installed.
The first time you run esdtool.exe for files in a given directory, it will prompt you for these things.

**Make sure to unpack the game using UXM/USDFM before running anything. Avoid modifying unpacked game files if you can.**

You can drag these types of files (with or without the .dcx extension):

* ESD files: .esd files can be dragged into esdtool.exe to decompile them and write .py files with the same name(s).
* Python files: .py files can be dragged into esdtool.exe to compile them and write .esd files with the ESD name(s).
* talkesdbnd files: these can be dragged into esdtool.exe to produce a directory with .py files decompiled from all ESDs in the archive(s).

  You will be given a choice of whether to use a single directory or multiple directories per bnd (suffixed with -only).
  I would recommend a single directory because it allows you to update all bnds simultaneously.
* Directories with Python files: these can be dragged into esdtool.exe to create bnds in the parent directory.
  These bnds do not need to exist beforehand. They are based on bnds from the game directory.
* Directories with an -only suffix with Python files: this is a special case where only *one* specific bnd in the parent
  directory will be modified. For example, the m10_00_00_00-only\ directory will only update m10_00_00_00.talkesdbnd.dcx.
  The bnd file *does* need to already exist.
  
Note that by default, **compiled bnd files are copied from bnds in the unpacked game directory!**
When esdtool.exe updates a bnd file, it starts with the game bnds, modifies only the ESDs requested for compilation, and passes the rest of them through.
This means you should be very careful about modifying the unpacked game files, or else those modifications
will propagate to all instances of esdtool for that game. (You can set esddir to get around this. See below.)

After running esdtool.exe for the first time, you can edit options in a file called `esdtoolconfig.json`.
It supports these fields:

* `game`: The lowercase game abbreviation like `"ds1"` or `"sdt"`.
* `basedir`: The game directory which includes the exe and all unpacked files.
* `backup`: Whether to create backups when writing a file that already exists. You're explicitly asked this before esdtool writes any files.
* `extra`: A key-value dictionary from ESD names to BND names indicating extra ESDs to add to those BNDs which do not exist in the vanilla versions. This is used for adding brand new ESDs rather than just modifying existing ones.
* `other_options`: Regular command line options which are automatically added to the command line string.

Finally, here are some recommended workflows:

### Decompiling the entire game

1. Copy all game talkesdbnds into a different directory where you can safely browse and modify files
2. Select all of the talkesdbnds and drag them into esdtool.exe together
3. When prompted, enter a directory name like `py` or `all` or `esds` to place all decompiled files

### Recompiling the entire game

1. Drag your main Python file directory into esdtool.exe
2. This will update all the talkesdbnds

This isn't recommended if you can avoid it. Instead...

### Recompiling only specific files

1. After decompiling the entire game, create a completely different directory which doesn't contain any talkesdbnds, and create another directory nested inside of it
2. Copy the Python files you wish to modify into the inner directory
3. Make edits
4. Drag the inner directory into esdtool.exe
5. This will create talkesdbnds in the outer directory. You can then place these in `script\talk` in a Mod Engine directory, or just do it within a Mod Engine directory to begin with.

### Making UXM/UDSFM patching work

This requires overriding where esdtool looks for the vanilla files.

1. Before doing anything else, make a subdirectory of `script\talk` called `bak`, and copy all vanilla talkesdbnds into it
2. Unpack the files as above
3. In `script\talk\esdtoolconfig.json`, modify `extra_options` to add `-esddir script/talk/bak`. Do this before modifying any bnds.

## Command line flags

```
Usage: esdtool.exe <args>

esdtool decompiles ESDs to a high-level Python representation, which can be compiled back to ESD.
Similar to ffmpeg or ImageMagick, the order of command line arguments determines the order of
operations. For instance, -ds1 -esddir chr will default everything to DS1, but then change
the subdirectory used for ESD inputs. The other way around will not work.

> Game flag
-ds1, -ds1r, -ds2, -ds2s, -bb, -ds3, -sdt, -er
    Sets all game data flags to default known values for Steam installations of the given game, or
    clears them if unknown. This overrides all values which were there before. These default values
    are kept in SoulsIds in GameSpec.cs

> Game data flags
(not necessary to set if set by the game flag)
-basedir DIR
    Sets the base directory for esddir, maps, msgs, and params. UXM or similar tool must be used.
-esddir DIR
    Sets the relative dir for all ESDs, meaning all .esd, .esd.dcx, and esdbnd.dcx files in
    that directory. Overrides -i for a list of ESDs and clears -f.
-maps DIR
    Sets the relative dir for all MSB files. Used to look up chr info on ESDs, currently for
    DS1, DS1R, DS3, and Sekiro.
-msgs DIR
    Sets the relative dir where FMG bnds can be found. Used to annotate ESDs with game info.
-params FILE
    Sets the relative file with game params. Used to annotate ESDs with game info.
    Requires -layouts or -defs.
-names DIR
    A directory with names for game ids. Currently ModelName.txt is used alongside chr info.
-layouts DIR
    A directory with layout xml files, required to use -params in most games.
-defs DIR
    A directory with paramdef xml files, required to use -params in Elden Ring.
-outdcx [None | Zlib | DCP_EDGE | DCP_DFLT | DCX_EDGE | DCX_DFLT_10000_24_9 | DCX_DFLT_10000_44_9 | DCX_DFLT_11000_44_8 | DCX_DFLT_11000_44_9 | DCX_DFLT_11000_44_9_15 | DCX_KRAK]
    Sets the DCX type to use when writing ESDs (writebnd/writeloose).

> Input/output flags
-i FILE1 FILE2 etc
    Can be used in two ways, for a list of one or more files. If all files end in .py, sets
    the list of Python files to compile. If all files end in .esd, .esd.dcx, and esdbnd.dcx,
    sets the list of ESD files to decompile; also overrides -esddir and clears -f. These are
    relative to the current directory if relative paths.
-f ESD MAP CHR etc
    A list of one or more filters for -esddir or -i inputs, replacing previous list of filters
    (if any). ESD is an ESD name or prefix (like t300330 or event), MAP is a prefix for a BND
    name (like m40_00), and CHR is a character model with an ESD (like c1400, if -maps is
    supported). The ESDs output/replaced are a union of all filters. Filters do nothing if no
    input ESD matches them.
-edddir DIR
    The directory to use to find .edd or .edd.txt files, default dist\<game>\edd when it exists
    for English translations. This can be set to the same as -esddir to use the original EDD files.
-[no]backup
    When enabled (default false), backs up files with a .bak suffix before writing them. If the
    .bak file already exists, this does nothing. This is usually not needed if you're using a
    separate mod directory.
-writepy TEMPLATE
    Given ESD inputs (with -esddir or -i), decompile all ESDs, with filters if those exist. The
    template is a file name, with %e, %m, and %c replaced with ESD, map name prefix, and chr name
    respectively (if -maps is supported). First chr is used if there are multiple, and 'unk' if
    there are none. All ESDs matching the pattern while be combined in the respective file. If
    the template has no format args, all ESDs will go into one py file. Use - to output to stdout.
-writebnd DIR
    Given Python inputs (with -i), and also ESD inputs (with -esddir or -i), write copies of those
    ESD/bnd files to the given directory if they have compiled ESDs. If the given directory is a
    relative path and gamedir is also provided, it will be relative to the game directory. Can be
    used to write out final files for a mod.
-writebndfile FILE
    Same as -writebnd, but it will only write to the given BND file. It will still compile all
    inputs. If the given directory is a relative path and gamedir is also provided, it will be
    relative to the game directory.
-extra ESD1=BND2 ESD2=BND2 etc
    Used with -writebnd to add extra ESD files not present in the original game ESDs. For example,
    if the -writebnd directory contains m10_00_00_00.talkesdbnd.dcx, you can add a new ESD t100630
    to it by specifying t100630=m10_00_00_00
-[no]copysame
    When enabled (default false), writebnd not only writes copied of the compiled ESDs, but also
    copies of all ESDs which are identical to it. This can be used to decompile only one bonfire
    and change all other bonfires at once. Equivalence is determined an ESD's hash, which is shown
    by -info.
-writeloose TEMPLATE
    Writes out individual .esd files. If there are Python inputs (with -i), there also must be
    ESD inputs (with -esddir or -i) to use as a template; then writes out individual .esd files
    contained in those Python files. If there is more than one .esd, the template must include
    %e, which is the ESD id. If not given any Python files, just writes out the given ESD
    bnds/dcxs as individual .esd files.
-writeedd TEMPLATE
    Writes out .edd.txt files for EDD files alongside input ESD files, which can be used to
    annotate Python files with developer documentation. %e is the ESD id. Translated EDD dumps are
    already included with esdtool so this is not usually necessary.
-info
    Print basic info on the given input files - some parsing but no compilation/decompilation.
    If -maps is supported, also prints where the ESDs are used.

> EDD writing options
-eddformat Flat | Chunk | Join
    How to write .edd.txt files. This can be done flat (basically a direct dump), chunked with
    all strings in shared files at most 500 lines long, or joining chunked inputs from -edddir.

> Compilation options
-[no]cfg
    When enabled (default true), writes state machines as functions with nesting and loops. When
    disabled uses many gotos instead. CFG representation currently excludes unreachable states.
    Until supported, use nocfg to help with cut content recovery.
-[no]stateinfo
    When enabled (default true), writes state ids as docstrings. This is more cluttered but allows
    writing back commands/conditions to the same states.
-[no]deadstates
    When enabled (default true), adds unreachable states at the end of machines. This has no effect
    on execution, and it can be noisy, but it can also be helpful for restoring cut content.
-[no]newstates
    When enabled (default true), allows creating states with fresh ids, rather than requiring tha
    all all ids are specified in docstrings (with -stateinfo).
-[no]regsubstitute
    When enabled (default true), decompilation substitutes GetREG expressions with the contents of
    equivalent SetREG expressions from within the same state. The reverse optimization is not
    currently done during compilation.
-[no]cmdedd
    When enabled (default false) and EDD is available, output text for each individual command
    where given a description. This appears to be automatically inserted based on the command id,
    rather than custom text like state or machine descriptions.
-cmdtype [None | Talk | TalkER | Chr | Event | AI]
    The source to use for command and function names, for both reading and writing. If not
    provided, this is inferred from .esd/.py name and provided game where possible. Otherwise, None
    is used.

> Some examples
Show all known ESDs for a game:
    $ esdtool.exe -ds2s
Decompile all ESDs for a game to one Python file:
    $ esdtool.exe -ds3 -writepy ds3.py
Decompile all ESDs for a game to different Python files:
    $ esdtool.exe -ds1r -writepy %e.py
Decompile a specific ESD from a game by name:
    $ esdtool.exe -sdt -f t000001 -writepy %e.py
Decompile and recompile a lone ESD file (cmd type inferred from name):
    $ esdtool.exe -ds2s -i work\event_m10_04_00_00.esd -writepy work\%e.py
    $ esdtool.exe -ds2s -i work\event_m10_04_00_00.py -writeloose work\%e_recompiled.esd
Recompile the given Python files into a subdirectory of the game, copying relevant bnds:
    $ esdtool.exe -sdt -i *.py -writebnd mymod\script\talk
    $ esdtool.exe -ds2s -i mymod\event_m10_04_00_00.py -writebnd mymod\ezstate

```