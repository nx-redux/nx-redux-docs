# Emulator Settings

**Tools → Settings → Emulation → Default settings** opens **Emulator Settings**. It
sets each emulator's options for a whole console, without starting a game
first.

The **Emulation** section holds **Default emulators** (see
[below](#default-emulators)), **Default settings**, **GPU driver** (see
[GPU driver](emulators/index.md#gpu-driver)), and the
[Save on quit and A resumes](#save-on-quit-and-a-resumes) switches.

![Settings with Emulation open beside the sections: Default emulators (selected), Default settings, GPU driver at System driver, and the Save on quit and A resumes switches, both on](../assets/screenshots/mobile/settings-emulators.webp){ .nx-wide }

For one game, use **Game Settings** in the game's context menu instead. See
[Game Settings](#game-settings).

## The emulator list

The page lists each emulator that runs one of your consoles, with the tags it
covers, such as **Gambatte GB · GBC**. Press `A` on an emulator. When it
covers more than one tag, the app asks for the console first.

![mGBA — Game Boy Advance (MGBA) beside the Settings sections: Audio Buffer and Fill Audio Gaps, then the Emulator label in the accent with its System and Video groups](../assets/screenshots/mobile/emulator-settings.webp){ .nx-wide }

??? info "More detail"

    Emulators for consoles you have no games for are not listed.

## An emulator's settings

The page is titled with the emulator, the console and the tag, such as
**PicoDrive — Sega Genesis (MD)**. Its rows sit under a label per group:

| Group | What it holds |
| --- | --- |
| **Display** | The picture: the Nintendo DS and 3DS screen rows, **3D Resolution**, **Graphics API**, **GPU driver**, **Wii Screen** and **Bottom screen**. See [Display](in-game-menu.md#display). |
| **Controls** | **Button Mapping**, **Controller Type**, and the Nintendo 3DS and Wii controls. See [Controls](in-game-menu.md#controls). |
| **Gameplay** | Fast forward, rewind, **Frame Skip** and **PS2 BIOS**. See [Gameplay](in-game-menu.md#gameplay). |
| **Multiplayer** | **Local Wireless**, on Nintendo DS, 3DS and PSP. See [Local Wireless](local-wireless.md). |
| **Audio** | **Audio Resampling Quality**, **Audio Buffer** and **Fill Audio Gaps**. See [Audio](in-game-menu.md#audio). |
| **Emulator** | The emulator's own options. Rows with `›` open a group of options, such as **Video** or **Audio**. |

The first five are the app's own settings for the console: the same rows as
the in-game [Options](in-game-menu.md#options) pages, plus the ones read
only when a game starts. A group shows only when it has rows for the
console.

![mGBA's System group beside the Settings sections: Game Boy Model, Use BIOS File if Found and Skip BIOS Intro](../assets/screenshots/mobile/emulator-settings-core.webp){ .nx-wide }

- The rows work as on the [Settings](settings.md#buttons) pages: a switch,
  a row of choices, or a value with `›` that opens the list of its values.
- `A` flips a switch and opens the list on a value with `›`. `LEFT` /
  `RIGHT` change a value where the page shows alone. Beside the Settings
  sections, press `A` on a row of choices first, as on any
  [Settings](settings.md#buttons) page. By touch, tap the switch, the
  choice, or the row.
- The **?** icon, or `X` **Info**, shows an option's full description.
- Each change is saved straight away. There is no **Save** row.
- Some options only take effect when a game starts, such as the N64
  resolution. The new value is used the next time you start a game.

**Audio Buffer** (Auto, 50 ms, 75 ms, 100 ms; Auto by default) is how much
sound is kept ready ahead of the speaker. **Auto** keeps 50 ms on Wii,
GameCube and PlayStation 2, and about 33 ms elsewhere. More covers slow
moments without crackling, but the sound comes later against the picture.
It applies the next time the game starts.

What you set here is the console's setting, the same as the in-game menu's
**Save Changes → Save for console**. See the
[in-game menu](in-game-menu.md) for the options themselves.

??? info "More detail"

    - The rows read only when a game starts are **Graphics API**
      ([Graphics API](emulators/index.md#graphics-api)), **GPU driver**
      ([GPU driver](emulators/index.md#gpu-driver)), **Audio Buffer**,
      **Local Wireless**, **PS2 BIOS**, and the Wii's **Wii Screen** and
      **Pointer** rows
      ([Nintendo Wii & GameCube](emulators/wii-gamecube.md#console-settings)).
      The in-game menu leaves them out.
    - **Button Mapping**, the fast forward rows and the three **Audio**
      rows are there for every console. Button Mapping opens the console's
      mapping; see [Button Mapping](controls.md#button-mapping).
      **Controller Type** is for Sega
      Genesis, Sega CD and Sega 32X, the rewind rows for emulators that can
      rewind, and **Frame Skip** for Wii and GameCube.
    - While a second screen is connected, every console also has **Bottom
      screen**: **System default**, **Main screen** or **Second screen**. See
      [Dual Screens & External Displays](dual-screen.md#for-one-console).
    - **Screen Scaling**, **Screen Sharpness**, **Overlay**, the offsets,
      **Pad Opacity (landscape)** and **Debug HUD** are in the in-game menu
      only. Keep them for the console with **Save Changes → Save for
      console** there.
    - The in-game [Emulator](in-game-menu.md#emulator) page leaves out the
      options that only take effect when a game starts.
    - When the app cannot read an emulator's options outside a game,
      **Emulator** shows **This emulator's options aren't available outside
      a game.** Change them from the in-game menu instead.
    - The console's settings and **Save for console** write the same file.

## Cable Link

mGBA's page for Game Boy Advance ends with a **Cable Link** group, the
settings of [Cable Link over Wi-Fi](netplay.md#cable-link-over-wi-fi). They
are the app's own, not one console's or game's, so Game Settings doesn't
list them.

| Row | Values | Default | What it does |
| --- | --- | --- | --- |
| **Input delay** | Auto, 1 frame to 8 frames | 1 frame | How many frames a button press waits in a session, the same on both phones. **Auto** starts at 2 and rises when the network stalls. It applies from the next session. |
| **Delay overlay** | Off, On | Off | Shows the current input delay in a corner of the game. |
| **Clear link ROM cache** | | | Deletes the game files kept from Cable Link sessions; they are sent again next time. The row shows the cache's size. |

mGBA is listed for this whichever emulator is your default for Game Boy
Advance: a Cable Link session always runs mGBA.

![The end of mGBA's page: the last Emulator groups, then the Cable Link group with Input delay 1 frame, Delay overlay off and Clear link ROM cache](../assets/screenshots/mobile/emulator-settings-cable-link.webp){ .nx-wide }

## Game Settings

Open a game's context menu with `MENU` in a game list, or a long press on
the game, and choose **Game Settings**. The same page opens over the list, for that one game.

![Game Settings for Tetris, over the Game Boy list: the Controls label in the accent with Controller Layout, then Gameplay with Max FF Speed selected and Fast Forward Audio](../assets/screenshots/mobile/game-settings.webp)

- The first change gives the game its own settings, starting from the
  console's.
- **Controls → Button Mapping** sets that game's buttons. The game follows
  the console's mapping until you change one, and follows it again once
  every button matches the console's. See
  [Button Mapping](controls.md#button-mapping).
- To go back to the console's settings, press `A` on **Use emulator
  settings**, the last row.
- `B` goes back to the game list.
- There is no hint bar: the rows work as on the
  [emulator's page](#an-emulators-settings), by buttons or touch. `LEFT`
  and `RIGHT` change a value straight away.

??? info "More detail"

    - The game's settings are the same file **Save Changes → Save for game**
      writes.
    - **Use emulator settings** shows only while the game has its own
      settings. `A` on it deletes them, so the game follows the console's
      again.
    - `B` returns to the game list on the same game.

## Save on quit and A resumes

Two switches in **Tools → Settings → Emulation**, both **On** by default,
decide how games pick up where you left them.

| Row | On (the default) | Off |
| --- | --- | --- |
| **Save on quit** | Quitting or leaving a game saves a hidden save state, so it carries on where you left off. | Quit just quits: no hidden save state is written. Games start fresh from the shelves, **Continue** and the Game Switcher, unless you load a save slot. |
| **A resumes** | `A` on a game with a save state continues from it. | `A` starts games fresh. **MENU → Resume** still continues from the save. |

With **Save on quit** off, the in-game menu's **Save & Quit** and its
shortcut are named **Quit**, and the Game Switcher lists every recent
game, not only those it can resume. Your battery saves are kept either way.

??? info "More detail"
    - Turning **Save on quit** off doesn't delete the hidden save state: the
      file stays on disk, but games stop resuming from it, and Home stops
      showing its picture. A game that stops while it's off drops its link
      to the old state, so turning the switch back on never resumes a
      weeks-old state over newer in-game saves.
    - With **A resumes** off, the Game Switcher also starts games fresh on
      `A` (its hint reads **Start**). With it on, `A` resumes from the latest
      save state, or starts fresh when there is none.
    - A fresh start replaces a game still suspended in the background
      instead of bringing it back. A game whose emulator can't save states
      still comes back on `A` while **A resumes** is on, so its progress isn't
      lost.
    - If Android closes the app in the background while **Save on quit** is
      off, the game starts fresh when you come back.

## Pause when unfocused

Whether a game pauses while another app takes over is set in **Tools →
Settings → System → Pause when unfocused**. See
[System](about.md#pause-when-unfocused).

The second screen has its own section in Settings: see
[Dual Screens & External Displays](dual-screen.md#settings).

## Default emulators

Some consoles can run on more than one emulator. **Tools → Settings →
Emulation → Default emulators** picks the emulator for a game with
no emulator of its own.

![Default emulators beside the Settings sections: one row per console with its emulator and tag, such as Game Boy Advance with gpSP (GBA)](../assets/screenshots/mobile/default-emulators.webp){ .nx-wide }

The consoles with more than one emulator come first, then the consoles you
have games for that have only one, each group A to Z. Each row shows the
console's emulator and tag, such as **gpSP (GBA)**. On a console with more
than one emulator, pick another one as on any
[Settings](settings.md#buttons) row: `A`, `LEFT` / `RIGHT` where the page
shows alone, or a tap.

- Saves and BIOS are shared by the console's emulators, so switching emulator
  copies nothing.
- To switch one game to another emulator, use **Emulator** in its context
  menu. See [Emulators](emulators/index.md).

??? info "More detail"

    - The line under the page's title reads **A game's own Emulator choice
      still wins. Saves and settings follow the tag.**

    - The consoles with more than one emulator (listed in
      [Choosing an emulator](emulators/index.md#choosing-an-emulator)) always
      show. The other rows are dimmed and only show the emulator in use.
