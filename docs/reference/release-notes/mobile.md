---
title: Mobile Release Notes
---

# Mobile Release Notes

What changed in each release of NX Redux for Android phones, tablets and
Android handhelds. Download the APK from the
[releases page](https://github.com/nx-redux/nx-mobile/releases).

## v0.5.0

*26 October 2026*

The picture and the on-screen pad are now laid out together. In landscape the
pad sits beside the game instead of over its edges, and pixel-art consoles
get the largest whole-number size that fits. DS and 3DS games get new
layouts, a half-folded layout on foldables, and a **Mic** for games that ask
you to blow or shout. The main menu moves its tabs to the bottom, colour now
marks the selected game in every layout, and Settings is rebuilt as a quiet
block of words.

### New features

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
  [Frontend](../../mobile/in-game-menu.md#frontend).
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
  [Hiding the portrait band](../../mobile/controls.md#hiding-the-portrait-band).
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
  **Back** go first. See
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
  name, and the name stays in your accent until the game's first frame. It
  follows Android's **Remove animations** setting.
- **Game Switcher layout** is picked from a row of choices in Layouts.

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
  in [Pad layout](../../mobile/controls-settings.md#pad-layout).
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
  [Nintendo DS](../../mobile/emulators/nintendo-ds.md#portrait-pad) and
  [Nintendo 3DS](../../mobile/emulators/nintendo-3ds.md#portrait-pad).
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
