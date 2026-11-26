# Sega Saturn

Saturn games run on the bundled **YabaSanshiro** core.

| | YabaSanshiro |
| --- | --- |
| Folder | `Roms/Sega Saturn (SATURN)/` |
| Saves | `Saves/SATURN/`: one backup memory file per game (see [Saves](#saves)) |
| BIOS | `Bios/SATURN/`: `saturn_bios.bin` (recommended, see [BIOS](#bios)) |
| [File types](index.md) | `chd` `cue` `ccd` `iso` `m3u`, and a zip or 7z holding one `.chd` or `.iso` |

- **OpenGL ES only.** YabaSanshiro has no Vulkan renderer, so Saturn games
  have no **Graphics API** row.
- Save states are about 10 MB each. Rewind isn't available.
- Saturn games play at full speed on the Retroid Pocket Nova, the Galaxy Z
  Fold and the AYANEO Pocket Air Mini, at the default 3D Resolution.

## Controls

The Saturn pad is the Genesis 6-button pad with two shoulder buttons. A
controller plays it **by position**, as on the other
[Sega consoles](sega.md), and so do the buttons of the on-screen
[pad skin](../controls.md#pad-skins):

| Button | Saturn button |
| --- | --- |
| Left, top and right face buttons | `A`, `B`, `C` |
| Bottom face button | `X` |
| `L1`, `R1` | `Y`, `Z` |
| `L2`, `R2` | `L`, `R` |
| `START` | `START` |

- The Saturn pad has no `Mode` or `SELECT`. `MENU`, or `SELECT` + `START`
  on a controller, opens the [in-game menu](../in-game-menu.md).
- The pad skin draws the Saturn pad: `A` `B` `C` below `X` `Y` `Z`, `L` and
  `R` on the shoulders, and `START` beside `MENU`.

## BIOS

Put the BIOS in `Bios/SATURN/`, named `saturn_bios.bin`, `sega_101.bin` or
`mpr-17933.bin`. Any region's BIOS works under any of these names.

Without one, games start on YabaSanshiro's built-in BIOS. Most games play,
but some may not work. The first time, the app says: **Running without a
Sega Saturn BIOS: some games may not work. Put saturn_bios.bin in
Bios/SATURN/.** It says this once.

!!! tip "If a game doesn't work"
    Add a Saturn BIOS to `Bios/SATURN/`. The next launch uses it.

??? info "More detail"
    - With more than one file, YabaSanshiro loads `saturn_bios.bin`, then
      `sega_101.bin`, then `mpr-17933.bin`.
    - A BIOS the app doesn't know is used without a warning. A file that is
      another console's BIOS is refused, and the app names it.

## Adding games

Put Saturn discs in `Roms/Sega Saturn (SATURN)/`. A disc whose tracks are
separate files is a `.cue` (or `.ccd`) plus its track files. Give each one
its own folder, named like the sheet. The folder shows as one game:

```
Roms/Sega Saturn (SATURN)/
├── Mega Man X4 (USA).chd
└── Daytona USA (USA)/
    ├── Daytona USA (USA).cue
    ├── Daytona USA (USA) (Track 01).bin
    └── Daytona USA (USA) (Track 02).bin
```

A multi-disc game plays as one game from an `.m3u` that lists its discs;
see [Multi-disc games](index.md#multi-disc-games).

!!! warning "Don't zip a `.cue` with its tracks"
    The app unpacks only one file from a zip, so a zipped `.cue` and its
    `.bin` tracks can't play. The app says so: **‹Game›.zip holds ‹Game›.cue
    with its tracks, which can't be played zipped. Zip a single .chd or .iso
    instead, or keep the files unzipped.** A zip or 7z holding one `.chd` or
    `.iso` plays.

??? info "More detail"
    - A Saturn disc in an extra folder that names no console is recognised
      from the disc itself and listed under Sega Saturn.
    - A folder named `Sega Saturn (SS)` works too.

## Saves

Every game gets **its own backup memory**, the Saturn's internal save
memory:

```
Saves/SATURN/<game>.bkr
```

It is written to its file each time the game saves, so a save is kept even
if the app is closed straight after.

??? info "More detail"
    - For example `Saves/SATURN/Daytona USA (USA).bkr`. An `.m3u` game's
      file is named after the playlist and shared by its discs, and a zipped
      disc's after the zip.
    - The file carries to another phone with
      [Device Sync](../device-sync.md), like any battery save.
    - Games save the same way on the built-in BIOS.

## 3D Resolution

**3D Resolution**, under **Display** in the in-game
[Options](../in-game-menu.md#options), sets how sharply the game is drawn.
The screen's size doesn't change. YabaSanshiro draws the whole picture at
1x, 2x or 4x of the game's own size; there is no 3x.

| Mode | What it does |
| --- | --- |
| **Auto** (default) | Draws at the scale the picture is shown at, up to **Max Scale** (2x by default). |
| **Quality** | As sharp as the display can show, up to 4x. |
| **Performance** | Draws at **Scale**, 1x or 2x. |

**Max Scale** shows only in Auto, **Scale** only in Performance. A change
takes effect at once, without restarting the game.

??? info "More detail"
    - With no 3x, a picture shown at about 3x is drawn at 4x in Quality, and
      at 2x in Auto and Performance.
    - Some games switch to a high-resolution mode (704 × 480) for menus or
      whole games. There, each step draws twice as many pixels across, so
      4x costs much more.
    - The lists follow the display: a small screen doesn't offer 4x.
    - While a [shader](../in-game-menu.md#options) is on, Auto draws at 1x.

## Emulator options { #core-options }

Change YabaSanshiro's settings on the **Emulator** page of the in-game
menu's [Options](../in-game-menu.md#options), or outside a game under
**Emulator** in [Emulator Settings](../emulator-settings.md). The app starts
games with the SH-2 dynamic recompiler, the 4 MB RAM cartridge, frame skip
on and the console's language set to English.

??? info "More detail"
    - YabaSanshiro's own resolution and HLE BIOS options don't appear on the
      **Emulator** page: **3D Resolution** and the [BIOS](#bios) check set
      them.

## Multiplayer

Up to two players can play, each on their own controller; see
[Local Multiplayer](../multiplayer.md). Netplay isn't available for Saturn
games.

## Cheats and achievements

- [Cheats](../cheats.md): the cheat download has Action Replay codes for
  Saturn games, including codes made of several parts joined with `+`. A
  "Master Code" entry does nothing on its own and can be left off.
- [RetroAchievements](../retroachievements.md) works for Saturn discs in
  `.chd`, `.cue`, `.iso` and `.m3u`, and zipped discs once unpacked.
