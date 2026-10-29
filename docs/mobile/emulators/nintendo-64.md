# Nintendo 64

Nintendo 64 games run on the bundled **Mupen64Plus-Next** core.

| | Mupen64Plus-Next |
| --- | --- |
| Folder | `Roms/Nintendo 64 (N64)/` |
| Saves | `Saves/N64/` |
| BIOS | Not needed |
| [File types](index.md) | `n64` `z64` `v64` (also inside a zip or 7z) |

- **Graphics API** can switch a game to Vulkan. See
  [Graphics API](index.md#graphics-api).

## Controls

<figure class="nx-phone" markdown>
![Super Mario 64 on the Fold's cover screen, with the Nintendo 64 pad: A, B, the yellow C buttons and Z](../../assets/screenshots/mobile/pad-n64.webp){ .nx-phone__screen }
![](../../assets/landing/mobile/zfold8.webp){ .nx-phone__frame }
</figure>

The Nintendo 64 maps a controller **by the printed letter**, like every
Nintendo console: the button printed `A` is the N64's `A`.

| Controller | Nintendo 64 |
| --- | --- |
| `A`, `B` | `A`, `B` |
| `X` | C-Left |
| `Y` | C-Down |
| `L1`, `R1` | `L`, `R` |
| `L2` | `Z` |
| `START` | `START` |
| Left stick | Analog stick |
| Right stick | The C buttons |
| `R2`, `SELECT` | Nothing |

- The on-screen pad draws `A`, `B` and a yellow C-button diamond, with `Z` on
  `L2`. It has no `SELECT`.
- `MENU`, or `SELECT` + `START`, still opens the
  [in-game menu](../in-game-menu.md).

??? info "More detail"
    **Controller Layout** in **Options → Console Settings** names your
    controller's letters if it is read wrongly. Set it to the layout that
    isn't your controller's to swap `A`/`B` and `X`/`Y`; see
    [Controls](../controls.md#controller-buttons).

## Rumble

Rumble is off out of the box: the controller holds the Controller Pak (for
saves) instead. To turn it on:

1. Open [Emulator Settings](../emulator-settings.md) for the console, or
   **Game Settings** for one game.
2. Under **Core settings → Pak/Controller Options**, set **Player 1 Pak** to
   **rumble**.
3. Start the game again.

Only games that support the Rumble Pak rumble, such as Super Smash Bros.
Mario Kart 64 doesn't. See [Vibration](../controls.md#game-rumble).

??? info "More detail"
    - The Rumble Pak takes the Controller Pak's place.
    - Each player has their own setting, from **Player 1 Pak** to **Player 4
      Pak**.

## Video

- Video uses the **GLideN64** plugin. With **Graphics API** set to
  **Vulkan**, it switches to the paraLLEl plugins: more accurate, and
  heavier.
- Many video options, such as the resolution, only take effect when a game
  starts. They are in [Emulator Settings](../emulator-settings.md), not in
  the in-game **Core Options**.

## High-resolution texture packs

Texture packs replace the Nintendo 64's blurry textures with high-resolution
ones. They load only with **Graphics API** set to **OpenGL ES** (the GLideN64
plugin).

**Getting a pack.** Sites such as evilgames.eu host packs like *Mario Kart 64
Reloaded*, *Super Mario 64 Reloaded* and *Ocarina of Time Reloaded*. Download
the **GLideN64 Cache**: a `.7z` holding one `<NAME>_HIRESTEXTURES.hts` file.
Extract the `.hts` and keep its name. When a pack offers HD and 4K, pick HD.

!!! note "Only the ready-made cache"
    PNG packs (the **GLideN64 / rt64 Source** download) don't work in the
    app. Packs made for other emulators don't either.

**Installing a pack:**

1. Put the `.hts` file in `Textures/N64/` in your home folder. Create the
   folders if they aren't there.
2. Open [Game Settings](../emulator-settings.md) for the game. Under
   **Core settings → GLideN64**, turn on **Use High-Res textures**.
3. Start the game.

`<NAME>` is the game's internal header name, such as `MARIOKART64` or
`SUPER MARIO 64`, not its file name. The pack's own file name already has it
right.

!!! tip "Keep packs on internal storage"
    The game reads a pack in small pieces as scenes need them. An SD card is
    slow at that, and the game stutters; internal storage keeps it smooth.
    Your ROMs can stay on the SD card: only the pack needs to move.

??? info "More detail"
    - **Beside the game, as on the handheld.** A pack also loads from a
      `.cache/` folder next to the game, such as
      `Roms/Nintendo 64 (N64)/.cache/MARIOKART64_HIRESTEXTURES.hts`. When
      both places have the pack, the one in `Textures/N64/` is used.
    - **Without All files access** the app reads the pack through the folders
      you picked, so packs work on every install.
    - **Memory.** **Max High-Res VRAM Limit** caps the memory the textures
      use. **Auto** picks by the device: 200 MB with up to 3 GB of RAM,
      500 MB with up to 6 GB, and no limit above that. Over the cap, the
      textures used least recently are dropped and read again when needed.
    - **Pack instructions from other emulators.** Only **Use High-Res
      textures** needs setting; the storage options they mention are already
      set. Ignore their PC cache paths.
    - The app never writes to a pack.

## Multiplayer

Up to four players can play, each on their own controller; see
[Local Multiplayer](../multiplayer.md). [Netplay](../netplay.md) isn't
available for the Nintendo 64 in the app yet (the handheld has it).

## Cheats and achievements

- [Cheats](../cheats.md): the cheat download has codes for Nintendo 64
  games, or add your own `.cht` files.
- [RetroAchievements](../retroachievements.md) works for Nintendo 64 games.
