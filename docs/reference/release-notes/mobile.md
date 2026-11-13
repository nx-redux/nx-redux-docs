---
title: Mobile Release Notes
---

# Mobile Release Notes

What changed in each release of NX Redux for Android phones, tablets and
Android handhelds. Download the APK from the
[releases page](https://github.com/nx-redux/nx-mobile/releases).

## v0.6.0

*13 November 2026 · v0.6.1 and v0.6.2 on 14 November*

The on-screen pad is now a rendered **pad skin**, with layouts of its own
for every console and a freer button editor. DS, 3DS and PSP games find
each other over Wi-Fi for local wireless play with nothing to set up, GBA
cable games link between two phones with **Cable Link over Wi-Fi**, and
N64 joins netplay. **Kids Mode** opens games only in the play times a
parent sets. Text is typed on NX Redux's own keyboard, which a controller
can drive. The main menu gains a **Games** tab, games show their genre,
year and publisher, and on two screens the bottom one acts while the top
one informs. Most bundled emulators are updated, and three rounds of
review fixed crashes, lost play time and lost achievement unlocks.

### New features

- **Pad skins.** The drawn pad is replaced by rendered skins in seven
  packs: **NX Carbon** (the default), Onyx, Obsidian, Plasma, Ember, Volt
  and Tide. Every console has its own layouts, for phone portrait and
  landscape, the folded and unfolded Fold, and tablets. The in-game menu
  sits in the skin's screen glass. **Appearance → Pad skin** Off draws the
  skin's buttons see-through over a full-screen game. The Charcoal, Retro
  and Black pad themes, Menu pad, Flex mode and Portrait Pad are gone. The
  main menu's skin hides while a controller is connected.
- **Button layout editor.** Move and resize button groups per console,
  from **Settings → Appearance → Button layout** or the in-game menu's
  **Options → Controls → Adjust buttons**. A group goes anywhere in the
  window and may reach a little into the screen; touch areas never stack.
  With Pad skin off, the see-through buttons have a layout of their own.
- **DS, 3DS and PSP local wireless.** Devices on the same Wi-Fi meet in a
  game's own wireless or ad hoc menu, as real consoles side by side do:
  start the game on each device and use its multiplayer mode. Nothing goes
  on the network until the game turns its wireless on. Up to 8 players on
  DS, 2 to 4 on PSP. DS and 3DS also use a USB cable between two phones
  when one is plugged in. Each console has a **Local Wireless** option, on
  by default, and DS, 3DS and PSP games can also host or join from the
  Netplay menu. While a game's wireless is on, the in-game menu is
  **Continue · Disconnect · Quit**, and save states, rewind, fast forward
  and reset are off.
- **Player name.** A new first row in **Settings → System**, up to 10
  characters, defaulting to the device's name. It is the name other
  players see on DS, 3DS and PSP.
- **Cable Link over Wi-Fi.** A third connection in the Netplay menu for
  GBA games: real link-cable play between two phones, for any two-player
  Multi-Pak cable game, such as Mario Kart Super Circuit, Zelda Four
  Swords and Pokémon Ruby ↔ Sapphire trades. A missing ROM is sent to the
  other phone for the session, and saves are only written from moments
  both phones agreed on. Phones only; the handheld can't join. Its
  settings (**Input delay**, **Delay overlay**, **Clear link ROM cache**)
  are on mGBA's page in **Settings → Emulation → Default settings**.
- **mGBA over Wi-Fi.** mGBA links over Wi-Fi for games that use the
  Wireless Adapter (Pokémon FireRed, LeafGreen and Emerald's Union Room)
  or the Pokémon and Advance Wars cable protocols, and an mGBA player can
  link with a gpSP player. See
  [Game Boy Advance link](../../mobile/netplay.md#game-boy-advance-link).
- **N64 netplay.** Two players, phone to phone or phone to an NX Redux
  handheld. See [Netplay](../../mobile/netplay.md).
- **Kids Mode.** A PIN-guarded play schedule for a device a young child
  uses with NX Redux as the home screen. Set a play time per day; outside
  it the child sees large tiles of the apps you allowed, and any other app
  is sent back to the tiles. Ten minutes before the time ends a warning
  shows, then a running game quits with its save written. A parent's PIN
  gives a timed unlock or the full menu. Turn it on in **Settings → Kids
  Mode**, or at the end of setup under **Who's this for?**
- **NX keyboard.** Every text prompt (search, rename, new collection, new
  folder, sign-ins, API keys) uses NX Redux's own keyboard, for touch or a
  controller: the d-pad moves, `A` types, `X` deletes, `Y` is space, `L` /
  `R` move the cursor, `SELECT` goes to the next field, `START` confirms
  and `B` cancels. It has Paste and a Show / Hide for passwords. On two
  screens it types on the bottom screen for a prompt on the top one.
  **Settings → System → Keyboard** switches back to Android's keyboard,
  for password managers and swipe typing.
- **Games tab.** A new main-menu tab between Home and Consoles with every
  game from every console and your Android games, A to Z. `L2` / `R2` jump
  by letter. Hide it in Layouts or in setup.
- **Game details.** Genre, year, publisher and a synopsis come from
  ScreenScraper with the art, and are fetched in the background for the
  game you rest on (**Artwork → Fetch art and info when browsing**, on by
  default). Games show their genre and "year · publisher" under the play
  time; **Layouts → Game info** switches that line back to achievements.
- **Change art.** A game's menu has **Fetch art** or **Change art**: pick
  any picture ScreenScraper, TheGamesDB, SteamGridDB and libretro
  thumbnails offer, per kind (Screenshot, 2D box, 3D box, Wheel, Mix). A
  picked picture stays until you pick another or reset it. With **Mix**
  on, fetches download ScreenScraper's own mix where it has one. See
  [Change art](../../mobile/artwork.md#change-art).
- **Screen care.** For OLED screens, on by default in **Settings →
  System**: everything on screen shifts by a tiny step every 2 minutes, a
  game left alone dims after 5 minutes without input and lets the screen
  sleep after 10. Netplay dims but never sleeps.
- **RetroAchievements profile.** A new page sums your unlocks, games
  played and mastered, the latest unlocks and the games nearest mastery.
  New **Unlock sound** (on) and **Screenshot on unlock** (off) rows;
  screenshots go to `Pictures/NX Redux/Achievements`.
- **Fill Audio Gaps and Audio Buffer.** When a game runs below full speed
  its sound is stretched at the same pitch instead of crackling. **Audio
  Buffer** is Auto by default, longer on Wii, GameCube and PS2.
- **Frame Skip for Wii and GameCube.** **Off**, the new default, shows
  every frame and lets heavy scenes slow down a little; **Auto** holds the
  game's speed by dropping frames, as before.
- **Debug log file.** With **Settings → System → Debug log** on, the menu
  and each game write a log file to `Logs/` in the home folder, so a
  report needs no computer. The newest 20 sessions are kept. See
  [Debug log](../../mobile/about.md#debug-log).

- **First-launch tips.** The main menu shows a tips dialog at launch:
  `MENU` opens the highlighted item's menu, a pad with no `MENU` button can
  set one in **Settings → Controls → System buttons** or press `SELECT` +
  `START`, `START` searches your games and `SELECT` opens the Game
  Switcher. The first game list adds `Y` for Netplay and `X` for
  achievements. **Got it** closes a tip until the next launch, **Don't show
  again** for good. (v0.6.1)
- **Two-screen board on foldables and tablets.** With a pad skin on the
  unfolded Fold, a tablet or a half-folded Flip, the in-game menu opens in
  the bottom screen, as on a dual-screen handheld, and the paused game on
  the top screen gets the pause cover. DS and 3DS games get a **Panel**
  pill that flips the game panel over the touch screen, and a **Game** pill
  that flips it back, both at the window's bottom-right. (v0.6.1)

### Improvements

- **Two screens: the bottom acts, the top informs.** Tools, game lists,
  Settings, prompts and the in-game menu open on the bottom screen. The
  top screen shows the highlighted game's details (synopsis, play time,
  achievements and a picture) or a console's or collection's stats. See
  [Dual Screens](../../mobile/dual-screen.md).
- **Second-screen game panel.** Shortcuts is a grid of tiles, your touch
  buttons first, over a strip of save-state slots with their screenshots.
  A new Settings tab has volume, Screen Scaling, Screen Sharpness and
  Shader, applied live.
- **Apps on the top screen.** Home takes the top screen back from an app.
  A one-screen game leaves the app there so you can watch while playing,
  and **Use top screen** in the in-game menu moves the game up anyway.
  The Apps tile no longer fills the top screen with its list.
- **Options by group.** Console Settings and Frontend become **Display**,
  **Controls**, **Gameplay**, **Audio** and **Multiplayer**, and Core
  Options is now **Emulator**. In two panes, `Left` / `Right` only move
  between the panes; press `A` on a row to change its value.
- **In-game menu.** A tab row runs across the menu: **Menu**,
  **Achievements**, **Cheats** and **Players**. **Reset** is a row on the
  first page, and the shortcut tiles are gone.
- **Launch and quit.** A game opens straight from the menu and quits
  straight back: no app-icon splash, no system slide in launcher mode, and
  no launch sequence in Minimal.
- **Netplay menu.** One card with **Connection** tabs (Wi-Fi · USB Cable ·
  Cable Link) and **Emulator** tabs, and **Host Game** and **Join Game**
  side by side. Every pop-up shares its look. A linked session (GB / GBA
  cable, DS wireless) offers **Continue · Disconnect · Quit**, and
  Disconnect lets the game play on from its own save.
- **DS and 3DS shortcuts match.** `L3` or `SELECT` + `L1` swaps the
  screens and `SELECT` + `R1` toggles stylus mode on both; in stylus mode
  the right stick, left stick or d-pad moves the pen and `R3` or `A` taps.
  On 3DS, `SELECT` + `L1` and `SELECT` + `R1` traded places.
- **System buttons.** Setup no longer asks for your controller's buttons.
  A pad's Back and Menu keys stand in for the `SELECT`, `START` or `MENU`
  it lacks, and the small button beside an AYANEO's logo button is `MENU`.
  **Controls → System buttons** binds a button from any device, such as a
  handheld's own buttons beside its pad. See
  [System buttons](../../mobile/controls-settings.md#system-buttons).
- **Button hints** show by default again, unless you set them yourself.
- **Home.** Most played is back on List and Minimal Home. Grid Home in
  landscape puts pinned tools in a row under Continue. Pinned tools and
  the Tools tab use one fixed tile on every screen.
- **Game lists.** The horizontal Carousel draws the selected game's
  details under its title, and Grid shows them on the selected tile.
- **Tools.** RetroAchievements, Cheats & Patches, Device Sync and Artwork
  use the Settings look. **Sync now** shows how many unlocks are waiting.
- **Device Sync asks before it syncs.** After pairing it shows the other
  device's address and your own; press `A` to sync. A search with no
  answer gives up after 5 minutes. See
  [Device Sync](../../mobile/device-sync.md).
- **Updates.** An in-app update only downloads from GitHub and installs
  only when its checksum matches.
- **Screen sleep.** The menu never keeps the screen on, and a game does
  only while it runs: a paused game sleeps on the device's timeout.
- **GBA sound.** gpSP sounds like mGBA: clearer highs in sampled music,
  such as Pokémon FireRed's, and the same volume.
- **Wii and GameCube.** Each game's own fixes stay on after an option
  change, frames are paced more evenly, and the emulator is updated with
  an ARM64 texture decoder. **Wii Screen → Auto** picks 16:9 only on a
  wide screen in landscape, and the touch pointer follows the shape a
  resumed game really has.
- **Nintendo DS.** melonDS DS 1.4.0 with its new OpenGL renderer: screen
  captures and scaled 2D are drawn at the 3D Resolution. Shaders apply to
  the top screen only, as a whole picture, on DS and 3DS.
- **Nintendo 3DS.** Azahar 2126.2. Save states keep loading after an
  emulator update, the OpenGL ES shader cache is kept between runs, and
  Vulkan compiles new shaders in the background.
- **PlayStation 2.** ARMSX2 2.9.2. With the picture on a second display,
  3D Resolution measures that display instead of falling to 1x.
- **Emulator updates.** FBNeo (8,510 sets), PPSSPP, Flycast,
  Mupen64Plus-Next, PCSX ReARMed, SwanStation, PicoDrive, PrBoom (Heretic
  and Hexen), Gearcoleco, Stella 2014, Beetle PCE Fast, Beetle VB, RACE,
  ProSystem, A5200, PokeMini, FCEUmm, Supafaust, Gambatte, Genesis Plus
  GX, Handy and Fake-08 move to their latest versions. Save states from
  v0.5.1 still load, except DS states made before melonDS DS 1.4.0 and
  FBNeo states whose size changed, such as Neo Geo games'. Those are
  refused, and the game starts fresh from its in-game save. 89 FBNeo sets
  changed their ROMs and need updated zips, and a few were renamed (`alienaru` →
  `alienar`, `gradiusb` → `bs_gradius`, `sailormnj` → `sailormn`).
- **Vertical arcade and WonderSwan games** are turned correctly on a
  second display and stay there.
- **Speed and battery.** Pausing a game or pressing Home no longer waits
  on the save, the menu rebuilds less while you move, art fetches make
  fewer requests, and a paused game or a picture hidden behind the panel
  costs less to draw.

- **Screen Scaling Auto fills the screen.** Every console now fits the
  space it has at any size; **Native** keeps whole-number scales. A picture
  at an in-between size is drawn sharp bilinear while Screen Sharpness is
  Nearest. (v0.6.1)
- **DS and 3DS full width in portrait.** With Auto, a DS **Large screen**
  puts the top screen across the full width with the touch screen under it,
  and **Stacked** makes both screens full width. The 3DS opens in Large
  screen by default with the on-screen pad (Stacked with a controller).
  A two-screen stack starts under the camera cutout. (v0.6.1)
- **Game lists.** New installs use **Backdrop**, and **Game info** shows
  achievements by default. On two screens Backdrop is offered again; only
  the vertical Carousel and Backdrop run across. The Layout dropdown is as
  wide as its choices. (v0.6.1)
- **Tools grid** uses the fewest columns that fill the rows in view and is
  centred, so 7 tools on a 6 × 3 screen sit 3, 3 and 1. (v0.6.1)
- **Small screens.** On a pad skin's touch screen, Settings pages scroll
  with the next row peeking under a thin fade, the Carousel's selected item
  takes at most 60% of the width, and the game panel and in-game menu show
  a one-line header (name, clock, battery). (v0.6.1)
- **Notifications** sit at the top centre in portrait, never on a DS or 3DS
  touch screen. (v0.6.1)
- **Button layout editor.** Buttons that only touched at a corner are no
  longer one group, the large layouts' touch shortcuts can be moved, and
  the buttons show at full opacity while editing. (v0.6.1)
- **Setup buttons** look like a pop-up's: the page's main action, such as
  **Continue**, is always in your accent, the others are outlined, and a
  ring shows where the controller is. A page whose only button is **Skip**
  shows it in the accent. (v0.6.2)
- **Folder picker.** **Use this folder** and **New folder** sit side by
  side, the first in your accent. `Left` / `Right` move between them and
  back to the folders. See
  [The folder picker](../../mobile/library.md#the-folder-picker). (v0.6.2)

### Fixes

- **Play time** is no longer cut short when the menu reads game time while
  a game is running, and merging split ROM folders moves their play time
  too.
- **RetroAchievements** unlocks are no longer lost when the menu and a
  game write at once, or when the server refuses the sign-in mid-game.
  Refresh and Cancel no longer crash when storage can't be read.
- **Save slots:** a slot saved over shows its new screenshot.
- **Second display:** Wii and GameCube games no longer show half-drawn
  frames and flicker there.
- **DS:** some scenes drew warped textures with OpenGL, such as Mario Kart
  DS's start-line flyover.
- **3DS:** stylus mode moves its pointer again.
- **Dreamcast:** the memory card is written out after every save.
- **Disc games** whose `.cue`, `.m3u` or `.gdi` sheet uses an older text
  encoding, a byte-order mark or different letter case now move, merge and
  open.
- **Artwork:** Replace no longer deletes the picture it just wrote on
  storage that ignores letter case, and Pause, Cancel and Reset can't
  hang a fetch.
- **Device Sync** never sends the temporary files of an interrupted
  write.
- **Cheats & Patches** only removes files it installed itself.
- **Half-folded launch:** a game started on a half-folded phone opens in
  the hinge layout.
- **Settings changed while a game is in the background** apply when it
  comes back.
- **Two-pane Settings:** holding `Left` or `Right` moves one level, not
  page after page.
- **Pause when unfocused:** the screen can sleep while it holds a game.
- **`SELECT` + `START`** opens the context menu on the main menu; before,
  `SELECT` or `START` acted the moment it was pressed. (v0.6.1)
- **DS:** `L2` swaps the screens and `R2` toggles the stylus, as `L3` /
  `R3` and `SELECT` + `L1` / `R1` do. (v0.6.1)
- **Pad Opacity** applies again to on-screen buttons moved over the
  picture. (v0.6.1)
- **3DS:** the top screen no longer stops short of full width after the
  touch screen's size changes. (v0.6.1)
- **In-game menu:** the Options column shows that more rows are below.
  (v0.6.1)
- **Pad skins:** the touch shortcuts no longer show under the game panel,
  and the DS touch screen takes taps beside the on-screen buttons. (v0.6.1)
- **Device Sync** opens again. Since v0.6.1 it closed the app, from
  **Tools** and as setup's Device Sync step. (v0.6.2)

## v0.5.0

*31 October 2026 · v0.5.1 on 2 November*

The picture and the on-screen pad are now laid out together. In landscape the
pad sits beside the game instead of over its edges, and pixel-art consoles
get the largest whole-number size that fits. DS and 3DS games get new
layouts, a half-folded layout on foldables, and a **Mic** for games that ask
you to blow or shout. The main menu moves its tabs to the bottom, colour now
marks the selected game in every layout, and Settings is rebuilt as a quiet
block of words; the in-game menu and every pop-up follow its look. The
PlayStation 2 joins the bundled consoles, N64 games take high-resolution
texture packs, and your own shaders go in the home folder. Games now run
in a process of their own, so quitting one frees everything it used.

### New features

- **PlayStation 2.** PS2 games run on the new **ARMSX2** core, with a full
  DualShock 2 on screen: the d-pad and both sticks always there, and `L3` /
  `R3` buttons under the sticks. Put a BIOS (any `.bin` dump) in `Bios/PS2/`
  and games in `Roms/Sony PlayStation 2 (PS2)/`; both folders appear on the
  first start after updating. Each game gets its own memory card in
  `Saves/PS2/<game>/`, and save states, resume and the Game Switcher work as
  on the other consoles. Two controllers give two players. **3D Resolution**
  (Auto up to **Max Scale**, 2x by default; Quality; Performance at native)
  and **Graphics API** (OpenGL ES or Vulkan) apply as on the 3DS. ISO, CHD and ZSO games open in place,
  never copied. See [PlayStation 2](../../mobile/emulators/playstation-2.md).
- **Cheats & Patches.** The cheat download also fetches PCSX2's patches for
  PS2: widescreen and no-interlacing patches for many games, turned on in
  **Core Options** in Game Settings or Emulator Settings. Your own `.pnach` cheats go in `Cheats/PS2/`. See
  [Cheats & Patches](../../mobile/emulators/playstation-2.md#cheats-patches).
- **Microphone for DS and 3DS.** Games that listen, such as Fossil Fighters,
  Zelda Spirit Tracks or Nintendogs, hear your phone's microphone while their
  **Mic** is on. Turn it on with the round mic button on the pad (bottom
  left in portrait, right of `L` in landscape), the **Mic** tile in the game panel, or a **Toggle mic**
  shortcut. Android asks for the microphone the first time; without it, the
  game hears a made-up blow so mic puzzles can still be passed. The Mic is
  off each time a game starts. See
  [Nintendo DS](../../mobile/emulators/nintendo-ds.md#microphone) and
  [Microphone access](../../mobile/library.md#microphone-access).
- **Pad beside the picture.** In landscape the pad's two halves sit either
  side of the game, solid where they clear it and see-through only where
  they overlap. DS and 3DS **STYLUS** and **SWAP**, and your touch buttons,
  get a second row under `MENU` and `START`. See
  [Landscape](../../mobile/controls.md#landscape).
- **Screen Scaling → Auto**, the new default. Arcade and 2D home consoles
  take the largest whole-number size that fits, 2D handhelds play at Native,
  and 3D consoles fill their space at their own shape. A Screen Scaling you
  picked yourself is kept. See
  [Display](../../mobile/in-game-menu.md#display).
- **New DS and 3DS layouts.** Large screen, Stacked, Single screen, Picture
  in picture and Side by side, at whole-number sizes, with a default that
  suits your screen. Your old pick carries over. See
  [Screen layouts](../../mobile/emulators/nintendo-ds.md#screen-layouts).
- **Half-folded DS and 3DS.** Fold a Galaxy Z Fold partway and the game
  lays itself out like a DS: the top screen above the hinge, the touch
  screen below it with the pad either side. See
  [Foldables](../../mobile/foldables.md#nintendo-ds-and-3ds-half-folded).
- **Black pad theme.** A pure black portrait pad, with **Pad buttons** Grey
  or Outline. See [Pad theme](../../mobile/appearance.md#pad-theme).
- **Tabs at the bottom.** The main menu's tabs sit along the bottom, with
  Home's stats and the **Recent** and **Search** icons at the top. Swipe
  sideways to switch tabs: the page slides while the tabs and icons stay put.
  The main menu has no hint bar any more. See [Tabs](../../mobile/main-menu.md#tabs).
- **Colour marks the selection.** In Grid, Carousel and Backdrop, the
  selected game is in full colour with its name in your accent, and the
  others are grey and dimmed. No ring goes round the selection. See
  [Main Menu & Home](../../mobile/main-menu.md#home).
- **N64 high-resolution texture packs.** GLideN64's ready-made cache,
  `<NAME>_HIRESTEXTURES.hts`, loads from `Textures/N64/` in the home folder
  or from `.cache/` beside the game; `Textures/N64/` wins when both have it,
  so a pack can sit on internal storage while the games stay on an SD card.
  Turn on **Use High-Res textures** in the game's Core Options. Packs load
  with OpenGL ES only, and PNG packs aren't supported. **Max High-Res VRAM
  Limit** has a new **Auto** default, picked by the phone's memory. See
  [High-resolution texture packs](../../mobile/emulators/nintendo-64.md#high-resolution-texture-packs).
- **Your own shaders.** Put RetroArch GLSL shaders (`.glslp` presets, or a
  bare `.glsl` in `Shaders/` or `Shaders/glsl/`) in a `Shaders/` folder in
  the home folder, and they appear at the end of **Shaders → Shader** as
  `User/…`. Updates never touch that folder. Prefer a shader's `.glslp`: it
  can ask for sharp pixels, while a bare `.glsl` follows **Screen
  Sharpness**. See [Your own shaders](../../mobile/in-game-menu.md#your-own-shaders).
- **System buttons.** Tell NX Redux which buttons on your controller are
  `SELECT`, `START` and `MENU`, for handhelds whose menu button sends a code
  Android doesn't name. Setup asks when a controller is connected, a new
  controller model is asked once, and **Tools → Settings → Controls →
  System buttons** rebinds them. Without a `MENU`, `SELECT` + `START` opens
  the menu. See [System buttons](../../mobile/controls-settings.md#system-buttons).
- **Audio Resampling Quality.** A Console Settings row for every console,
  **Low**, **Medium**, **High** (the default) or **Max**, as on the
  handheld. Sound is now converted to the phone's rate with libsamplerate,
  so it's cleaner than before, with no seam between buffers. See
  [Audio](../../mobile/in-game-menu.md#audio).
- **Most played shelf.** Home's first shelf under your pinned games holds
  up to four games with the most play time, each showing its time. Hide it
  in **Layouts → Home → Most played shelf**. See
  [Shelves](../../mobile/foldables.md#shelves).

### Improvements

- **DS 3D Resolution.** A new Console Settings row for DS games: **Auto**
  draws 3D at the size the screen is shown (up to **Max Scale**),
  **Quality** has no cap, and **Performance** uses a fixed **Scale**.
  melonDS's own Internal Resolution and unused screen options are gone. See
  [3D rendering](../../mobile/emulators/nintendo-ds.md#3d-rendering).
- **3DS 3D Resolution.** The same row for 3DS games: **Auto** draws at the
  whole multiple of the 3DS's screen width that fits (up to **Max Scale**,
  3x by default), **Quality** has no cap, **Performance** uses a fixed
  **Scale**. Azahar's own Internal Resolution, Large Screen Proportion and
  Stereoscopic 3D Mode are gone. In a game, Console Settings lists only the
  Layout row in use. See
  [3D rendering](../../mobile/emulators/nintendo-3ds.md#3d-rendering).
- **Portrait band.** The pad band is the same height in the menu and in a
  game. With the band hidden (DS, 3DS, and tall arcade, WonderSwan and Lynx
  games), one see-through pad lies across the bottom, and the New 3DS
  C-stick sits between the d-pad and the face buttons. Your touch buttons
  sit in its top row, and DS and 3DS screens may reach a third into it, so
  the unfolded Galaxy Z Fold shows a DS game at 6× + 3×. See
  [Pad skin off](../../mobile/controls.md#pad-skin-off).
- **Shortcuts without a controller.** The bind rows only show with a
  controller connected, since the on-screen pad can't be bound. Without
  one, the page points you to **Touch button 1** and **2**. See
  [Shortcuts](../../mobile/controls-settings.md#shortcuts).
- **3DS touch.** The bottom screen takes touches wherever it is drawn, in
  every layout, with the pad shown or hidden. See
  [Touch](../../mobile/emulators/nintendo-3ds.md#touch).
- **3DS Large screen in portrait.** The bottom screen grows to fill the
  height left under the top screen, up to the top's size (half its size
  when swapped). See
  [Screen layouts](../../mobile/emulators/nintendo-3ds.md#screen-layouts).
- **Pad layout editor.** The landscape editor shows the pad as the game
  draws it, and DS and 3DS get a Half-folded layout of their own on
  foldables. Landscape moves made for the old pad over the game are cleared
  once; portrait layouts are kept.
- **Launch and quit.** A game shows black until its picture is placed,
  with no flash at the wrong size, and the menu no longer jiggles on the
  way back.
- **Grids scroll up and down.** Every Grid (Home, Consoles, Collections,
  Tools and game lists) scrolls vertically only, as many columns as the
  screen's width holds, settling on a whole row. `Left` / `Right` move
  within a row and switch tab from the first or last column. Consoles show
  their logos alone, sized to look even, with the game count under the
  selected one. See [Grid](../../mobile/main-menu.md#consoles-grid).
- **Home.** Home now starts in **Minimal**. List Home is one list with
  **Continue**, **New** and **Not started** tags and the game's facts under
  the stats. Grid Home drops its shelf labels. Carousel Home sits centred on
  the screen. See [Home](../../mobile/main-menu.md#home).
- **Game lists.** The selected game's stats sit under the list's title in
  Minimal and Grid, and in List while the hint bar shows. Carousel and
  Backdrop centre on the screen, their unselected games grey, and
  Backdrop's picture is dimmer behind the boxes. See
  [Game lists](../../mobile/main-menu.md#game-lists).
- **Button hints off by default.** Hints show only in game lists, Recent,
  search results and the tools. With a full bar, `A` **Select** and `B`
  **Back** go first. **Recent** and **Search** are always icons now, so their
  two hint rows are gone from Layouts. See
  [Page title and button hints](../../mobile/layouts.md#page-title-and-button-hints).
- **Settings.** The sections sit as a block of words at the bottom left, the
  current one in your accent; on a wide screen the rows sit beside them at a
  fixed place. One tap opens a section, a tap on a control acts, and a long
  press opens the help. Resets ask first. Section labels are in the accent.
  See [Settings](../../mobile/settings.md).
- **Accents.** The nine accents are lighter, and **Secondary accent** has its
  own darker colours, with **Auto** (a dark shade of the accent) the new
  default. Both rows are colour swatches. See
  [Accent](../../mobile/appearance.md#accent).
- **Folder picker.** Its actions sit at the bottom, under the folders, in one
  column on every screen. `Left` / `Right` jump between the folders and the
  actions. See [The folder picker](../../mobile/library.md#the-folder-picker).
- **Launching from Minimal.** The screen goes black outward from the game's
  name, and the name stays in your accent until the game's first frame. A
  long name wraps onto more lines rather than running off the screen. It
  follows Android's **Remove animations** setting.
- **Game Switcher layout** is picked from a row of choices in Layouts.
- **Games run in their own process.** A game no longer shares the menu's
  memory: **Quit** ends it and frees everything its core used. Home or sleep
  leaves it paused, and picking it again brings it back at the same moment;
  if Android reclaims it meanwhile, it resumes from its auto-save. Starting
  another game saves and closes the paused one first.
- **Launcher mode and Recents.** With NX Redux as the home app, Recents no
  longer shows a card for NX Redux's home screen, and quitting a game always
  lands back on NX Redux. See
  [Use as home screen](../../mobile/launcher.md#use-as-home-screen).
- **GBA clock and sound.** Pokémon Ruby, Sapphire and Emerald keep the real
  time after a state is resumed. gpSP plays at 65536 Hz by default, and its
  music no longer holds notes too long at 32768 Hz. GBA games start on
  low-memory handhelds such as the AYANEO Pocket Air Mini.
- **The in-game menu.** The first page and **Options** are lists of words
  as in Settings, with no pills: the selected one in your accent. Actions
  such as **Reset Parameters** and **Save Changes'** saves are words too.
  **Quit Game** and **Reset game?** put their choices side by side, and the
  **Shortcuts** tiles take fewer columns rather than cutting a label short.
  See [In-game Menu](../../mobile/in-game-menu.md).
- **Pop-ups.** Every pop-up's buttons sit inside it, side by side, with no
  key hints under it. The controller works in it alone: it opens on its
  first button, `Left` / `Right` move between the buttons, `A` presses the
  lit one and `B` cancels. In **Rename**, `Down` moves from the text to
  **OK**. The left stick works as the d-pad, also behind a text box.
- **Setup.** Every setup step uses the Settings look: the step's question
  as a large title, its rows, and the buttons as words at the bottom.
  **Fetch artwork** holds the ScreenScraper sign-in and the SteamGridDB and
  TheGamesDB keys. With **Move** on, a new ROMs folder asks before moving
  its games, and says they are moved, not copied.
- **Grid and Home.** Unselected tiles are brighter. Tool and collection
  names break only between words and keep clear of the tile's edges
  (**Cheats & / Patches**). In the Carousel's **Consoles**, **Collections**
  and **Tools**, the centred item is in your accent. List Home puts the
  game's facts on one line under the stats.
- **Settings → Layouts.** The picture under the rows is no longer dimmed
  while the list scrolls.
- **Accents.** Orange, Violet and Pink are a little brighter, so a selected
  name stands out from the grey ones around it.
- **Achievements.** Running **Download all game data** again finds a game
  that moved to another folder, such as an SD card, so its achievement line
  comes back. See
  [Downloading all game data](../../mobile/retroachievements.md#downloading-all-game-data).
- **System buttons: Back can be bound.** Handhelds whose home button acts
  as Back, such as the Retroid Pocket Classic, can bind it as `MENU` in
  setup and in **Controls → System buttons**. Only `B` goes back now.
  (v0.5.1)

## v0.4.0

*25 October 2026 · v0.4.1 and v0.4.2 on 25 October*

Play on two screens: DS and 3DS games put the bottom screen on a second
display, other games get a game panel there, and the main menu spreads across
both. Fast forward, rewind and reset arrive with shortcuts you set yourself,
saves move into your home folder so an uninstall keeps them, and the GitHub
build now updates itself.

Patch v0.4.1 brings back save-state screenshots, resumes without a black
screen, quits instantly and adds page jump and a Save & Quit shortcut;
v0.4.2 fixes **Ready to install** in About. Their changes are listed below,
marked with their version.

### New features

- **Dual screen.** With a second display, a dual-screen handheld's built-in
  screen or a wired monitor, DS and 3DS games get one screen each: the top
  screen on the picture screen and the bottom screen on the touch screen.
  The **Panel** pill puts both on the picture screen
  and the game panel on the touch screen; **Game** brings them back. Setup
  asks which screen is the bottom one on handhelds with a built-in second
  screen, and **Tools → Settings → Second screen** holds **Enable** and
  **Bottom screen**. See [Dual Screens & External
  Displays](../../mobile/dual-screen.md) and
  [Nintendo DS and 3DS](../../mobile/dual-screen.md#nintendo-ds-and-3ds).
- **The game panel.** Other games show a panel on the touch screen: box art,
  title, play time, achievements, the clock and battery, with the tabs
  **Shortcuts**, **Achievements**, **Cheats** and **Players**. Cheats now live
  in the panel's **Cheats** tab, and setting a player slot to **Empty**
  benches a pad for this game only. See
  [The game panel](../../mobile/dual-screen.md#the-game-panel).
- **The main menu on two screens.** On **Consoles** and **Collections**, the
  picture screen previews the highlighted row's games; `A` or a tap opens
  that list there, while the touch screen shows the highlighted game's
  details and achievements. Your buttons, hints and menus follow the screen
  you're on. See [The main menu](../../mobile/dual-screen.md#the-main-menu).
- **Apps and tools on the picture screen.** Apps you open from **Tools**,
  Home or the Android console open on the picture screen while the menu
  stays put, and the built-in tools (Settings, RetroAchievements, Artwork and
  the rest) open there too. See
  [Apps on the picture screen](../../mobile/dual-screen.md#apps-on-the-picture-screen).
- **Fast forward.** Toggle it, or hold it while a button is down. A
  per-console **Max FF Speed**, 2x to 8x (4x by default), caps it, and
  **FF Audio** plays the sound along.
- **Rewind.** Toggle or hold, turned on per console in **Console Settings**.
  It's off by default, and isn't offered on the 3DS, Dreamcast, PSP, Doom,
  GameCube or Wii.
- **Reset** restarts the game, and always asks first.
- **Shortcuts.** **Tools → Settings → Controls → Shortcuts** binds fast
  forward, rewind and reset to your controller: press the button you want.
  `MENU` plus a button makes a combo; a tap on `MENU` still opens the menu,
  a held one doesn't. `SELECT` and `START` can't be used. The in-game
  **Options → Shortcuts** changes them for one console or one game.
- **Touch buttons.** Two optional on-screen buttons, each **FF**, **RW**,
  **Hold FF**, **Hold RW** or **Reset**, show once you assign them. Move them
  in [Button layout](../../mobile/controls-settings.md#button-layout).
- **Fast forward, Rewind and Reset in the game panel.** The panel's
  **Shortcuts** tab has working tiles for them, and **Screenshot** is gone.
  A ►► or ◄◄ mark at the top right of the game shows while either runs.
- **In-app update** for the build from GitHub. On the main menu, at most once
  a day, **Update available** shows the new version and what's in it:
  **Update** downloads and installs it, **Not now** keeps that version quiet.
  The install waits until no game, sync or download is running.
  **Tools → Settings → System → About → Check for updates** checks at any
  time. See [Check for updates](../../mobile/about.md#check-for-updates).
- **Saves in your home folder.** Battery saves, save states and per-game
  settings now live in the home folder, laid out as on the handheld's card
  (`Saves/<TAG>/` and `.userdata/`), so uninstalling the app no longer loses
  them. Without All files access, the home is
  `Android/media/com.nxredux.mobile/`, which a file manager can reach. Your
  saves from v0.3.0 and earlier move the first time you open this version.
  See [Saves](../../mobile/library.md#saves),
  [Without All files access](../../mobile/getting-started.md#without-all-files-access)
  and [Upgrading from an earlier version](../../mobile/getting-started.md#upgrading-from-an-earlier-version).
- **The Apps drawer.** **Tools → Apps** is a grid of every installed app:
  open one, add it to Tools or pin it to Home. It replaces
  **Settings → Launcher → Android apps**. See
  [Android apps](../../mobile/launcher.md#android-apps).
- **Cheats for more systems.** Dreamcast, Arcade (FBNeo), ColecoVision,
  Atari 7800 and Lynx games now show and use cheats, and RAM-patch cheats
  work. With All files access, the cheat database goes in your home folder's
  `Cheats/<TAG>/`, one folder per console, so a reinstall finds it. See
  [Where the files go](../../mobile/cheats.md#where-the-files-go).
- **Page jump in game lists.** `L1` / `R1` jump to the previous or next
  letter in a console's game list, in every layout. `Left` / `Right` move a
  page in List, Minimal and the vertical Carousel and Backdrop. See
  [Game lists](../../mobile/main-menu.md#game-lists). (v0.4.1)
- **Save & Quit shortcut.** Bind it in
  [Controls → Shortcuts](../../mobile/controls-settings.md#shortcuts) to quit
  a game from a controller, saving your place, without opening the menu.
  Nothing is bound by default. (v0.4.1)

### Improvements

- **Settings, reorganised.** **Library** holds your games, folders, All files
  access and **Saves**; the new **System** section, last, holds Pause when
  unfocused, Use as home screen, Debug log, About and the licenses.
  **Emulators** is now **Emulation**, and its **Settings** row is
  **Default settings**. See [Settings](../../mobile/settings.md).
- **Touch-friendly settings rows** in Settings, Emulator and Game Settings,
  RetroAchievements and Artwork settings, and the in-game options: a switch,
  a row of choices, or the value with `›` that opens a picker. The full
  description is behind the ⓘ icon or `X`. See
  [Touch](../../mobile/settings.md#touch).
- **The in-game menu** puts the game's header across the top of every page,
  with the panel beside the list. See
  [In-game Menu](../../mobile/in-game-menu.md).
- **Fades in place of scroll arrows** on lists, the settings and the in-game
  menu, and Consoles, Collections and Tools fill the page with taller rows.
- **List text** is the same size in portrait and landscape.
- **Grid Home** shows five tool squares a column and up to four games a
  shelf, with the first two pinned games beside the squares in landscape.
- **App icons in Tools** are white like the built-in tools, and built-in and
  app tools sort A–Z together, with Settings last.
- **Better cheat matching.** PSP cheat files match by region when the disc's
  serial isn't read, a ROM named without a region gets its region's files
  over a source-only pack such as `(Rumbles)`, same-ROM files and alternate
  titles that share codes merge, and names match across spacing and
  punctuation (`Soulcalibur` finds `Soul Calibur.cht`). Long codes load
  whole.
- **Pad layout.** On the portrait pad, DS and 3DS **STYLUS** and **SWAP** and
  the Wii's **MOTION** move to the top row. The GameCube pad keeps its logo,
  with `START` in the middle.
- **Shader Parameters** show only once a shader is chosen.
- **GB, GBC and GBA link sessions** carry on as a normal game when the link
  ends, with the full menu, save states and cheats.
- **Collections** opens in the Minimal layout by default.
- **Popups** follow **Appearance → Text size**, and context menus split their
  rows evenly between their two columns.
- **A stuck game** is closed after 20 seconds, and the menu says it stopped
  responding, instead of the app freezing.
- **Resume without black.** A game you resume shows the save's screenshot
  from the moment it opens until the game itself is ready, instead of a
  black screen and a glimpse of the game starting over. (v0.4.1)
- **Instant Save & Quit.** Quitting cuts straight back to Home, the game
  list or the Game Switcher, with no fade. Resuming from the
  [Game Switcher](../../mobile/game-switcher.md) no longer slides the
  switcher away first, and quitting lands back on it with the game's new
  screenshot. (v0.4.1)

### Fixes

- **Wii games** no longer sometimes freeze the app on quit.
- **Quitting a game resumed from the Game Switcher** returns to the
  [Game Switcher](../../mobile/game-switcher.md), not the page under it.
- **PSP cheats:** every cheat you turn on runs, not only the last one. Long
  codes no longer crash the SNES, Mega Drive, N64 and PC Engine emulators.
- **Moving a display in DeX** no longer reloads the game or ends netplay.
- **An extra ROM folder** emptied of games but left with subfolders no longer
  makes every rescan fail.
- **Layouts → Reset to defaults** now updates Home straight away.
- **Save-state screenshots** show again in the in-game menu's
  [Save and Load](../../mobile/in-game-menu.md#the-first-page) slots, on
  Home's Continue card and in the Game Switcher. With saves in your home
  folder they were missing, and Continue showed the game's artwork
  instead. (v0.4.1)
- **Continue** shows the screenshot of your latest save after you leave a
  game from a game list or the Game Switcher, without restarting the app.
  (v0.4.1)
- **Ready to install** in Settings → About installs when you press it.
  Before, a download that finished while Settings was open only installed
  after you went back to the main menu. (v0.4.2)

## v0.3.0

*21 October 2026*

A new Minimal layout: just big names, no art, on Home, every tab and the game
lists. Art you delete or add outside the app now shows without a rescan.

### New features

- **Minimal layout.** Pick **Minimal** for Home, Consoles, Collections, Tools
  or any game list in **Tools → Settings → Layouts**. Only the names show, big:
  the selected one solid in your accent, the others outlined and fading away
  from it. Opening a console or a collection flies its name into the game
  list's title, and **Back** drops it into the list again. The Layouts page
  has pictures of it. See [Minimal Home](../../mobile/main-menu.md#minimal),
  [Minimal Consoles](../../mobile/main-menu.md#consoles-minimal) and
  [Minimal game lists](../../mobile/main-menu.md#games-minimal).

### Improvements

- **Art changed outside the app** shows when you come back to the app or open
  **Artwork**, without a rescan. Art you deleted is counted as missing again,
  so **Fetch art** is offered for it in the game menu.
- **The selection ring** on Home, the Grid and the Carousels is thinner.

## v0.2.0

*20 October 2026*

Bring your saves over from another app, a folder or a zip file. The DS and
3DS get a portrait pad you can hide, more screen layouts and on-screen Stylus
and Swap buttons. The Consoles Carousel can show your own console
backgrounds.

### New features

- **Import saves from anywhere.** **Tools → Settings → Emulators → Saves →
  Import saves** copies battery saves and save states **From a folder**,
  **From a zip file** or **From RetroArch**. Saves are matched to your games
  by name, nothing is moved or deleted, and a state never overwrites one you
  already have. First-run setup gets a matching **Bring your saves** step.
  See [Import saves](../../mobile/library.md#import-saves).
- **DS and 3DS: hide the portrait pad.** Long-press the arrow at the bottom
  right of the pad to hide it: the screens take its room and see-through
  buttons sit over the game. Long-press again to bring it back. See
  [Nintendo DS](../../mobile/emulators/nintendo-ds.md#pad-skin) and
  [Nintendo 3DS](../../mobile/emulators/nintendo-3ds.md#pad-skin).
- **DS and 3DS: more screen layouts.** Large screen on both, Side by side in
  portrait and Stacked in landscape on the DS, and separate layouts for
  portrait, portrait with a controller and landscape on the 3DS. See the
  [DS](../../mobile/emulators/nintendo-ds.md#screen-layouts) and
  [3DS](../../mobile/emulators/nintendo-3ds.md#screen-layouts) screen layouts.
- **DS and 3DS: Stylus and Swap buttons** on the on-screen pad. **Swap**
  trades the two screens, so you can touch the bottom screen under the
  see-through pad. See
  [Stylus mode](../../mobile/emulators/nintendo-ds.md#stylus-mode).
- **Console backgrounds in the Carousel.** **Consoles controller** is now
  **Consoles background** and works in the Carousel too: **Background** shows
  the console's own `.media/bg.png` behind the row, **None** shows neither,
  and the picture on the Layouts page follows it. See
  [Consoles background](../../mobile/layouts.md#consoles-background).

### Improvements

- **Artwork for badly named zips.** When a zipped game's name isn't found,
  the second lookup now uses the ROM inside the zip, so it gets its art. A
  7z is no longer looked up a second time, which saves ScreenScraper quota.
- **Artwork progress** drops games as they finish, so the one being fetched
  stays in view on a long library.
- **On-screen pad labels** are bigger on the portrait pad, and the Wii
  Classic Controller's lowercase letters sit in the middle of their buttons.
- **Bring your saves** has **Skip** at the top right, as the other setup
  steps do.

### Fixes

- **BIOS files in ROM folders** (such as `scph1001.bin` or `bios7.bin`) are
  no longer listed as games, so artwork fetches stop asking for them.

## v0.1.0

*18 October 2026 · v0.1.1 on 19 October*

The first public release: an early preview, so our first players can try it
and tell us what works and what doesn't before v1.0. Expect rough edges, and
keep a copy of your saves (**Tools → Settings → Emulators → Saves → Export saves**)
while it settles.

It needs Android 8.0 or later on a 64-bit ARM (arm64) device. Bring your own
games and, for the systems that need them, BIOS files. See
[Getting Started on Mobile](../../mobile/getting-started.md).

Patch v0.1.1 fixes games that failed to start on Android 14 and older with
**Could not start the game … library not found**.

### What's in it

- **First-run setup.** Text size, your folders, your handheld, artwork,
  RetroAchievements and the menu's look, page by page.
  [Getting Started](../../mobile/getting-started.md#first-run-setup)
- **The NX Redux menu.** Home, Consoles, Collections and Tools tabs in
  List, Grid, Carousel or Backdrop, search, pinned games and tools, and the
  Game Switcher. [Main Menu & Home](../../mobile/main-menu.md),
  [Menu Layouts](../../mobile/layouts.md)
- **One library with the handheld.** The same `Roms/`, `Bios/` and
  `Collections/` folders, extra ROM folders scanned in place, and saves kept
  inside the app with Export and Import.
  [Library & ROM folders](../../mobile/library.md)
- **30+ systems, built in.** From the Game Boy and NES to the PlayStation,
  PSP, Nintendo 64, Dreamcast, Nintendo DS and 3DS, and Wii & GameCube.
  [Bundled Emulators](../../mobile/emulators/index.md)
- **The in-game menu.** Save states with previews, per-console and per-game
  options, shaders, screen scaling and [cheats](../../mobile/cheats.md).
  [In-Game Menu](../../mobile/in-game-menu.md)
- **Controls your way.** An on-screen pad for each console with themes and an
  editable layout, any Android controller, and rumble.
  [Controls](../../mobile/controls.md)
- **Play together.** [Netplay](../../mobile/netplay.md) with another phone
  or an NX Redux handheld over Wi-Fi or a USB-C cable, Game Boy and GBA link
  trades included, and [local multiplayer](../../mobile/multiplayer.md) for
  up to four controllers.
- **RetroAchievements.** Earn achievements offline and sync them later, with
  an achievements panel on every game list.
  [RetroAchievements](../../mobile/retroachievements.md)
- **Device Sync.** Carry games, saves and save states between the phone and
  an NX Redux handheld. [Device Sync](../../mobile/device-sync.md)
- **And more.** [Artwork](../../mobile/artwork.md) for your games, a
  [Game Tracker](../../mobile/game-tracker.md), the app as your
  [home screen](../../mobile/launcher.md) with your Android games, Flex mode
  on [foldables](../../mobile/foldables.md), and Large or Small
  [text size](../../mobile/appearance.md#text-size).

### Not in this release

Features many retro frontends have that this preview doesn't yet:

- **Fast-forward, slow motion and rewind.**
- **Screenshots** of a game while you play.
- **Turbo (autofire) buttons**, other than the few cores with their own
  turbo option.
- **Full button remapping.** Controller Layout swaps the `A`/`B` and `X`/`Y`
  letters, and Pad layout moves the on-screen buttons, but you can't assign
  any button to any action.
- **Run-ahead** to cut input lag, other than the few cores with their own
  run-ahead option.
- **ROM patches** (IPS, BPS, UPS) applied at launch: a patched game has to be
  patched into its own file.
- **RetroAchievements leaderboards**, and hardcore mode (the same as on the
  handheld).
- **Cloud saves.** Saves stay on the phone; Device Sync carries them to a
  handheld, and Export saves makes a backup.
- **External display:** playing on a TV or monitor over a cable or casting.
- **Home computers** such as the Amiga and C64, which the handheld runs.
- **iOS.**

### Feedback

This preview is for finding what to fix and improve before v1.0. Tell us
what goes wrong, which games don't run well on your phone, and what you'd
like to see. Open an issue on
[GitHub](https://github.com/nx-redux/nx-mobile/issues), with your phone's
model and Android version (**Tools → Settings → About → Copy device info** copies them
for you).
