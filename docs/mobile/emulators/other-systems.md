# Other Systems

The other bundled systems play as you would expect. This page lists where
each one's games go and what is special about it. `MENU`, or `SELECT` +
`START`, opens the [in-game menu](../in-game-menu.md) on every system.

| System | Folder | Emulator | BIOS |
| --- | --- | --- | --- |
| NES | `Roms/Nintendo ES (FC)/` | FCEUmm | Not needed |
| Famicom Disk System | `Roms/Famicom Disk System (FDS)/` | FCEUmm | Needed: `disksys.rom` in `Bios/FDS/` (or `Bios/FC/`) |
| Super Nintendo | `Roms/Super Nintendo ES (SFC)/` | Snes9x, or Supafaust (`SUPA`) | Not needed |
| Neo Geo Pocket / Color | `Roms/Neo Geo Pocket (NGP)/`, `Roms/Neo Geo Pocket Color (NGPC)/` | RACE | Not needed |
| TurboGrafx-16 | `Roms/TurboGrafx-16 (PCE)/` | Beetle PCE Fast | CD games only: `syscard3.pce` in `Bios/PCE/` |
| Virtual Boy | `Roms/Virtual Boy (VB)/` | Beetle VB | Not needed |
| WonderSwan Color | `Roms/Wonderswan Color (WSC)/` | Beetle WonderSwan | Not needed |
| Atari 2600 | `Roms/Atari 2600 (A2600)/` | Stella 2014 | Not needed |
| Atari 5200 | `Roms/Atari 5200 (A5200)/` | a5200 | Optional: one is built in. `5200.rom` in `Bios/A5200/` is used when present. |
| Atari 7800 | `Roms/Atari 7800 (A7800)/` | ProSystem | Optional: `7800 BIOS (U).rom` or `7800 BIOS (E).rom` in `Bios/A7800/` |
| Atari Lynx | `Roms/Atari Lynx (LYNX)/` | Handy | `lynxboot.img` in `Bios/LYNX/` |
| ColecoVision | `Roms/Colecovision (COLECO)/` | Gearcoleco | Needed: `colecovision.rom` or `coleco.rom` in `Bios/COLECO/` |
| Pokémon mini | `Roms/Pokémon mini (PKM)/` | PokeMini | Optional: one is built in. `bios.min` in `Bios/PKM/` is used when present. |
| PICO-8 | `Roms/Pico-8 (P8)/` | fake-08 | Not needed |
| Doom | `Roms/Doom (PRBOOM)/` | PrBoom | Not needed: `prboom.wad` is bundled. The game's IWAD can also sit in `Bios/PRBOOM/`. |

Saves go in `Saves/<tag>/`, such as `Saves/FC/`.

ColecoVision plays cartridges only: the ADAM computer's disks and data
packs aren't supported, and the emulator's ADAM options are hidden.
**Mapper (restart)** and **Video Chip (restart)** are **Auto** by default: change them in
[Game Settings](../emulator-settings.md#game-settings), under **Emulator →
System**, only for a game that doesn't run right.

??? info "More detail: face buttons"
    A controller's face buttons work **by the printed letter** on the NES,
    Super Nintendo, Virtual Boy, Pokémon mini, Atari Lynx, WonderSwan and
    Neo Geo Pocket, and **by position** on the TurboGrafx-16, PICO-8, Atari,
    ColecoVision and Doom; see
    [Controls](../controls.md#controller-buttons).

## Controls

### NES and Famicom Disk System

When a Famicom Disk System game asks for the other side, press `L1` once. On
the on-screen pad the **DISK** button does the same.

| Control | What it does |
| --- | --- |
| `L1` | Turn the disk over (Famicom Disk System). One press ejects the disk and puts the next side in about a second later; a message shows the side. With the drive empty, it puts the next side in. |
| `R1` | Insert or eject the disk by hand (Famicom Disk System) |
| `X`, `Y` | Turbo `A`, turbo `B` (`TA` and `TB` on the on-screen pad). On by default; turn them off with **Turbo Enable** under **Options → Emulator → Input**. |
| `R2` | Insert a coin (Vs. System games) |

### Neo Geo Pocket / Color

| Control | Neo Geo Pocket |
| --- | --- |
| `A`, `B` | `A`, `B` |
| `START` | `OPTION` |

A game with a clock counts its time from the game itself, and save states
keep the clock, so rewind and states stay in step. To follow the phone's
clock instead, set **Real-Time Clock** to **Real Time** under **Options →
Emulator**. **Audio Quality (Restart)** (**Fast**, or the band-limited **Accurate**)
applies when the game starts, so it is only in
[Emulator Settings](../emulator-settings.md).

### TurboGrafx-16

| Control | TurboGrafx-16 |
| --- | --- |
| Right, bottom, left, top face buttons | `I`, `II`, `III`, `IV` |
| `L1`, `R1` | `V`, `VI` |
| `START` | `RUN` |
| `L2` | `Mode` |

CD games have two more options under **Options → Emulator → PC Engine
CD**, both off by default: **ADPCM Low-pass Filter** softens harsh ADPCM
sound, and **CD Ignore EDC/L-EC Errors** is needed by some hacks.

### Virtual Boy

| Control | Virtual Boy |
| --- | --- |
| `L2`, `R2` | The right d-pad's up and left |
| Right stick | The right d-pad (controllers only) |
| `X` | Low-battery toggle |

Games show in anaglyph 3D out of the box. **Allow Opposite Directions**,
under **Options → Emulator**, lets a d-pad press left and right, or up and
down, at once; it is off by default.

### Pokémon mini

| Control | Pokémon mini |
| --- | --- |
| `R1` | `C` |
| `L1` | Shake |
| `SELECT` | `POWER` |
| `X` | Turbo `A` |

### Atari

- **Atari 2600:** the bottom face button is Fire. **Color Palette**, under
  **Options → Emulator**, picks the **Standard** colours or **Z26**'s.
- **Atari 5200:** the on-screen pad has the two fire buttons, `*`, `#` and
  **KEYPAD**, which shows the console's keypad on screen.
- **Atari 7800:** the bottom and right face buttons are `1` and `2`.
- **Atari Lynx:** `L1` and `R1` are `Option 1` and `Option 2`.

### Games held upright

WonderSwan and Atari Lynx games made to be held upright show a picture
taller than wide. To give one the whole screen in portrait, turn
[Pad skin](../appearance.md#pad-skin) off: the buttons are then drawn
see-through over the game. On a [second display](../dual-screen.md), the
picture is turned the right way up there.

### PICO-8

The bottom and right face buttons are `O` and `X`. PICO-8 games have no save
states, and don't resume where you left off.

### Doom

`SELECT` shows the automap and `START` opens Doom's own menu. Rumble is on
out of the box.

PrBoom also plays Heretic and Hexen from their own IWAD files.

## Multiplayer

- **Up to four players:** TurboGrafx-16.
- **Two players:** NES, Famicom Disk System, Super Nintendo, Atari 2600,
  5200 and 7800, and ColecoVision. See [Local Multiplayer](../multiplayer.md).
- [Netplay](../netplay.md): NES, Famicom Disk System and Super Nintendo.

## Cheats and achievements

- [Cheats](../cheats.md): the NES, Famicom Disk System, Super Nintendo,
  TurboGrafx-16, WonderSwan, Atari 7800, Atari Lynx, ColecoVision and Doom
  take cheats. The others have no **Cheats** page.
- [RetroAchievements](../retroachievements.md) works for every system here
  except PICO-8 and Doom.
