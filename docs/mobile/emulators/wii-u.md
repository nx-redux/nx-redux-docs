# Nintendo Wii U

Wii U games run on the bundled **Cemu** core. The app lays out the TV and
the GamePad as two screens, the way it lays out the
[Nintendo DS](nintendo-ds.md) and [3DS](nintendo-3ds.md) screens.

| | Cemu |
| --- | --- |
| Folder | `Roms/Nintendo Wii U (WIIU)/` |
| Saves | `Saves/WIIU/Cemu/mlc01/` (the Wii U's own storage) |
| BIOS | Not needed. Encrypted discs (`wud`, `wux`) need their [disc key](#disc-keys) |
| [File types](index.md) | `wua` (recommended), `wud` `wux`, `rpx` |

- **Vulkan only.** Wii U games need a phone whose GPU runs Vulkan. See
  [Graphics](#graphics).
- **No save states.** Cemu has none, so games save in-game, as on a Wii U.
  See [Saves](#saves).
- **Wii U games need a fast phone.** They were tested on the Retroid Pocket
  Nova and the Galaxy Z Fold. On a phone with less than 3.5 GB of RAM, the
  first Wii U game shows **Wii U games may not run well on this phone.**
  once; the game still starts.
- The first launch of a game builds its shader and pipeline cache, which can
  take a long time. Later launches are quicker.

## Adding games

| Type | What it is |
| --- | --- |
| `.wua` | One file with the game, and its update and DLC when they were packed in. **Recommended.** |
| `.wud`, `.wux` | A disc image, full (`.wud`) or compressed (`.wux`). Needs its [disc key](#disc-keys). |
| `.rpx` | An installed game unpacked into folders (`code`, `content`, `meta`): the `.rpx` file in its `code` folder. |

!!! note "Updates and DLC go inside the `.wua`"
    For now the app can't install a game's update or DLC on its own. To play
    a game with them, pack the base game, the update and the DLC into one
    `.wua`.

### Making a .wua

A `.wua` is made with Cemu on a computer:

1. Install the game, its update and its DLC in Cemu.
2. Open **Tools → Title Manager**, right-click the game and choose
   **Convert to compressed Wii U archive (.wua)**.
3. Tick the update and the DLC you want in the file, and save it.
4. Copy the `.wua` into `Roms/Nintendo Wii U (WIIU)/`.

??? info "More detail"
    - A `.wua` is compressed, and needs no disc key.
    - Games open in place, so a large `.wua` is never copied.

### Disc keys

An encrypted disc image (`.wud`, `.wux`) needs the disc's key. Either:

- add it to `keys.txt` in `Bios/WIIU/`, one key per line, or
- put a `.key` file with the same name beside the image: `Game.wux` and
  `Game.key`.

Without a key the game doesn't start, and the app says **… needs its disc
key: add it to keys.txt in Bios/WIIU/, or put a .key file with the same
name beside the image**.

## Controls

The [pad skin](../controls.md#pad-skins) has the GamePad's controls,
laid out like the New 3DS pad, with `A` on the right. **SWAP** sits in the middle of the row of touch
shortcuts and swaps the two screens. Touch the GamePad's screen with your
finger, as on a Wii U.

<!-- TODO: Wii U pad skin screenshot (phone and Fold), as on the 3DS page. -->

A controller maps to the GamePad:

| Control | Wii U GamePad |
| --- | --- |
| Face buttons | By letter: a controller's `A` is the GamePad's `A` |
| `L1`, `R1` | `L`, `R` |
| `L2`, `R2` | `ZL`, `ZR` |
| Left stick, right stick | The GamePad's sticks, analog |
| `L3`, `R3` | The GamePad's stick clicks |
| `SELECT`, `START` | `−`, `+` |
| `MENU` | The app's [in-game menu](../in-game-menu.md) |

To use the GamePad's positions on an Xbox pad (`A` on the right), set
**Controller Layout** to **Nintendo**; see
[Controls](../controls.md#controller-buttons).

These shortcuts are the app's:

| Buttons | What they do |
| --- | --- |
| **SWAP**, or `SELECT` + `L1` | Swap the screens: the other one becomes the big one. |
| `SELECT` + `LEFT` / `RIGHT` | Change the layout of the orientation you're in: **Large screen**, **Stacked**, **Single screen**, **Picture in picture**, **Side by side**, and round again. |

Unlike the 3DS, `L3` doesn't swap the screens: it is a GamePad button.
There is no stylus mode, so `SELECT` + `R1` isn't a shortcut.

!!! tip "The layout tip"
    When a game starts, a notice reads **SELECT + Left / Right changes the
    screen layout** and **SELECT + L swaps the screens**. Tap **Don't show
    again** to hide it for good. It shows where the layout shortcut works.

!!! note "`SELECT` waits"
    As on the [3DS](nintendo-3ds.md#controls), the game gets `SELECT` (the
    GamePad's `−`) when you let go of it, so a combo doesn't reach the game.

### Motion

Games that use the GamePad's gyroscope read your phone's: tilt and turn the
phone as you would the GamePad. In Mario Kart 8, for example, you can steer
by turning the phone.

**Motion Controls** (On by default) is in the in-game menu under **Options →
Controls**, and in [Emulator Settings](../emulator-settings.md). It isn't
listed on a phone without both an accelerometer and a gyroscope.

## Screen layouts

The layouts are the [Nintendo DS](nintendo-ds.md#screen-layouts) ones, with
the TV as the top screen and the GamePad as the bottom screen. Each screen
keeps its 16:9 shape and fills the room it has.

| Layout | What it shows |
| --- | --- |
| **Large screen** | The big screen, with the other at half its size under it, or beside it where that leaves the big one bigger. |
| **Stacked** | One above the other, the same size. |
| **Single screen** | The big screen only. |
| **Picture in picture** | The big screen, with the other small in its top-right corner. |
| **Side by side** | Next to each other, the same size. |

**Big Screen** picks which screen is the big one (the TV by default), and
**SWAP** changes it. The GamePad takes touches wherever it is drawn, except
as the small picture-in-picture screen.

Each orientation keeps its own layout, as on the DS: **Layout (portrait)**,
**Layout (portrait, controller)** (while a controller hides the pad) and
**Layout (landscape)**. Until you pick one, portrait is **Stacked** and
landscape **Large screen**. `SELECT` + `LEFT` / `RIGHT` changes the one
you're in and saves it for the game straight away.

??? info "More detail"
    - With [Pad skin](../appearance.md#pad-skin) on, the skin places the
      screens in portrait, on the Galaxy Z Fold and on tablets, and the
      **Layout** rows it doesn't use read **Unavailable**. On a regular
      phone in landscape the skin's screen follows **Layout (landscape)**:
      **Stacked** until you pick another.
    - Cemu's own screen layouts and GamePad position options aren't listed
      under **Emulator**: the app's layouts replace them.

### Foldables and second screens

- **Galaxy Z Fold:** the pad skin puts the TV in its top screen and the
  GamePad in its touch screen. See
  [Foldables & Large Screens](../foldables.md).
- **A second screen** (a handheld with two screens, or a display on USB-C):
  the game starts split, the TV on one screen and the GamePad on the other,
  which takes the touches. **SWAP** swaps them over. See
  [Dual Screens & External Displays](../dual-screen.md#nintendo-ds-and-3ds).

## Graphics

Cemu draws with Vulkan only, so a Wii U game needs a phone with a Vulkan GPU.
There is no OpenGL ES fallback and no **Graphics API** row. On a phone
without Vulkan the game doesn't start, and the app says **Wii U needs
Vulkan, which this phone's GPU driver doesn't offer.**

On a Qualcomm Adreno GPU a custom [GPU driver](index.md#gpu-driver) such as
Turnip may run Wii U games better than the phone's own driver. On the
Retroid Pocket Nova (Adreno 740), the Stable Turnip driver worked best.
Some newer Turnip builds crash while the shader cache is being built: if a
game crashes there, try another driver or the system driver. The **GPU
driver** row is always shown for Wii U games, under **Display** in
[Emulator Settings](../emulator-settings.md) and
[Game Settings](../emulator-settings.md#game-settings).

### 3D Resolution

**3D Resolution**, under **Display**, sets how sharply the game is drawn,
at a whole multiple of the Wii U's 1280 × 720:

| Mode | What it does |
| --- | --- |
| **Auto** (default) | Native, 1x, on every display. Above Native some games break: in Wind Waker HD, for example, shadows and foliage turn black at 2x. |
| **Quality** | As sharp as the display can show, up to 3x. |
| **Performance** | A fixed **Scale** you pick, from 1x up to what the display can show (up to 3x). 1x by default. |

Use Performance to draw a game you know works above Native at 2x or 3x,
where the display reaches it.

!!! note "Set at launch"
    Cemu reads the resolution only when a game starts. A change in the
    in-game menu, turning or folding the phone, or a second display applies
    the next time you start the game.

??? info "More detail"
    - Cemu's own **Internal Resolution** isn't listed under **Emulator**:
      **3D Resolution** sets it.
    - Heavy games are limited by the phone's CPU, not by the resolution.
      Breath of the Wild runs at full speed outdoors on the Retroid Pocket
      Nova, at the limit of its CPU, so a higher scale costs more there
      than in lighter games.
    - Mario Kart 8 and Super Mario 3D World ran at 60 fps on the Retroid
      Pocket Nova and the Galaxy Z Fold.

## Software keyboard

When a game asks for text, such as Wind Waker HD's file name, a
**Keyboard** box opens over the game:

- Type a name and tap **OK**, or press `A`. With nothing typed, the game
  gets the console account's name.
- **Cancel**, or `B`, closes the box. The game's keyboard stays open, and a
  notice with **Type** brings the box back. `START` on the pad answers with
  the account's name.

## Saves

Games save in-game, to the Wii U's own storage in `Saves/WIIU/Cemu/mlc01/`.
Cemu has no save states, so for Wii U games:

- the in-game menu has no **Save** or **Load**, and **Quit** just quits;
- a game doesn't resume where you left off: it starts again, and you load
  your in-game save;
- rewind isn't available.

## Cheats and achievements

- Cheats: not available for Wii U games.
- RetroAchievements: not available for Wii U games.

## Multiplayer

Wii U games are one player, on the GamePad. Netplay isn't available.
