# esdtool.exe
This is a high-level language for viewing and editing ESD scripts, primarily to make significant edits/forks for custom quests.
It decompiles ESD files into a subset of Python, using Python constructs to represent various ESD features.
However, the Python cannot currently be executed or linked with other files.

Decompilation and compilation should work for vanilla ESDs from DS1, DS2, Bloodborne, DS3, and Sekiro.

See examples of this from games in the top-level examples/ directory.

## Language constructs
An ESD is composed of a set of machines, and each machine has states which explicitly transition to each other, including a unique entry state (id 0).
Likewise, there is an entry machine (id 1). In Bloodborne and onwards, machines may call each other as subroutines.

Each state machine is turned into a Python function. For instance:
```py
def t130800_x11(val5=12):
    call = t130800_x24()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5:
        assert t130800_x2()
    return 0
```

This is syntactically valid Python, but it doesn't have the same semantics as Python, and there is no direct evaluation or imports (yet).
Calling other functions is asynchronous, and in this language returns a future-like object.
Likewise, if/else statements are asynchronous, and only execute when one of the branches comes true, and always choose the first such branch.

As a convenience, asserts can be used in the place of single-branch if statements, as these effectively pause the machine until the condition becomes true.
If the condition is for a function call to complete, the function call can be used directly in the assert statement.

```py
def t200260_1():
    call = t200260_x8(flag9=1459, flag10=1455, flag11=1456, val1=12, val2=10, val3=12, val4=10, val5=12,
                      flag12=6001, val6=7002600, flag13=6000, flag14=6001, flag15=6000, flag16=6000,
                      mode1=1, val7=1000000, val8=1000000, val9=1000000, mode2=0, mode3=1, mode4=1, val10=1000000,
                      val11=1000000, mode5=0, flag17=6000, mode6=0)
    assert GetEventStatus(72009004) == 1
    assert t200260_x1()
    SetEventState(72009004, 0)
    # talk:26000900:Uwaaagghh!
    t200260_x5(text5=26000900, flag22=1, mode12=1)
```

Infinite loops are another form of control flow, with breaks and continues within the loop. These can be written as `while True`, or alternatively `while Loop('<loop name>')` to identify loops for multi-level breaks and continues.

```py
def t150270_x31():
    c1110()
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

Finally, it is not possible for some state machines to be turned into loops/conditionals, or difficult for the decompiler to determine, so Goto is also available.
This is usually only used in large state machines - this means most DS1 state machines, as usually all logic for one character is in one state machine.
This also happens with the `-nocfg` option, which must also be used on recompilation.

## State mapping
States can be explicitly assigned to Python code using doc strings in the middle of functions.
Otherwise, states are inferred by looking at a sequence of commands.
By default, docstrings are added during decompilation; use `-nostateinfo` to disable this behavior.
If you don't want states to be automatically created (generally shouldn't happen if recompiling vanilla ESDs), use the `-nonewstates` option.

## Command line flags
```
Usage: esdtool.exe <args>

esdtool decompiles ESDs to a high-level Python representation, which can be compiled back to ESD.
Similar to ffmpeg or ImageMagick, the order of command line arguments determines the order of
operations. For instance, -ds1 -esddir chr will default everything to DS1, but then change
the subdirectory used for ESD inputs. The other way around will not work.

> Game flag
-ds1, -ds1r, -ds2, -ds2s, -bb, -ds3, -sdt
    Sets all game data flags to default known values for Steam installations of the given game, or
    clears them if unknown. This overrides all values which were there before. These default values
    are kept in SoulsIds in GameSpec.cs

> Game data flags
(not necessary to set if set by the game flag)
-basedir DIR
    Sets the base directory for esddir, maps, msgs, and params. UXM or similar tool must be used.
-esddir DIR
    Sets the relative dir for all ESDs, meaning all .esd, .esd.dcx, and .esdbnd.dcx files in
    that directory. Overrides -i for a list of ESDs and clears -f.
-maps DIR
    Sets the relative dir for all MSB files. Used to look up chr info on ESDs, currently for
    DS1, DS1R, DS3, and Sekiro.
-msgs DIR
    Sets the relative dir where FMG bnds can be found. Used to annotate ESDs with game info.
-params FILE
    Sets the relative file with game params. Used to annotate ESDs with game info.
    Requires -layouts.
-names DIR
    A directory with names for game ids. Currently ModelName.txt is used alongside chr info.
-layouts DIR
    A directory with layout xml files, required to use -params.
-outdcx [None | ACEREDGE | DemonsSoulsDFLT | DemonsSoulsEDGE | DarkSouls1 | DarkSouls3 | DarkSouls3SL2 | SekiroDFLT | SekiroKRAK]
    Sets the DCX type to use when writing ESDs (writebnd/writeloose).

> Input/output flags
-i FILE1 FILE2 etc
    Can be used in two ways, for a list of one or more files. If all files end in .py, sets
    the list of Python files to compile. If all files end in .esd, .esd.dcx, and .esdbnd.dcx,
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
    used to write out final files for a mod. This does not create backups.
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
-[no]newstates
    When enabled (default true), allows creating states with fresh ids, rather than getting all ids
    from docstrings (with -stateinfo).
-[no]cmdedd
    When enabled (default false) and EDD is available, output text for each individual command
    where given a description. This appears to be automatically inserted based on the command id,
    rather than custom text like state or machine descriptions.
-cmdtype [None | Talk | Chr | Event | AI]
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