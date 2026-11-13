---
title: Mobile FAQ
---

# Mobile FAQ

Common questions about NX Redux for Android. Using a TrimUI
handheld? See the [Handheld FAQ](handheld.md).

## Can I use the same games folder as my handheld?

Yes. A copy of your handheld's folders, BIOS files included, works as the
app's home folder. See [Library & ROM folders](../../mobile/library.md).

??? info "More detail"
    The app uses the NX Redux layout: `Roms/<Name (TAG)>/`, `Bios/<TAG>/`,
    `Saves/<TAG>/`, `Collections/` and `map.txt`. A handheld's BIOS layout
    (such as `Bios/PS/psxonpsp660.bin`) works unchanged.

## Do my handheld saves carry over?

Battery saves carry over for systems that run the same core on both. Where
the app uses the same core as the handheld, save states carry over too.

The Sega systems run PicoDrive on both, so their saves and states carry over
too. For games from a legacy handheld `(GPGX)` folder, see below.

Dreamcast memory cards carry over: both name them
`Saves/DC/<game>.A1.bin`. See [Sega Dreamcast](../../mobile/emulators/dreamcast.md#memory-cards-vmu).

## Do my handheld's Sega save states work on the phone?

Yes. The phone runs the Sega consoles on PicoDrive, as the handheld does, so
a state made in a handheld folder such as `Sega Genesis (MD)` resumes on the
phone.

- **Games from a handheld `(GPGX)` folder** ran on Genesis Plus GX there.
  [Device Sync](../../mobile/device-sync.md) sets such a game's
  **Emulator** to Genesis Plus GX when it brings the game over, so its
  states resume too. For a game you copied yourself, pick Genesis Plus GX in
  its **Emulator** menu.
- **Battery saves** work in either emulator: PicoDrive and Genesis Plus GX
  share them.

See [Emulators](../../mobile/emulators/sega.md).

## Do I need to download emulators or cores?

No. Every core is bundled in the app. See
[Emulators](../../mobile/emulators/index.md) for the full list.

## Is there DraStic or Dreamcast?

There is no DraStic. It is closed-source and no longer available, so
Nintendo DS runs on **melonDS DS** instead. DraStic battery saves carry over.

Dreamcast is included, with the NAOMI and Atomiswave arcade games. See
[Sega Dreamcast](../../mobile/emulators/dreamcast.md).

## Can I play netplay with the app?

Yes. Two players can play over Wi-Fi or a USB-C cable, phone to phone or
phone to an NX Redux handheld (TrimUI Brick, Brick Pro or Smart Pro S).
Press `Y` **Netplay** on a game. Nintendo 64 is included, and Game Boy and
Game Boy Advance games link for trades and battles. See
[Netplay](../../mobile/netplay.md).

??? info "More detail"
    - Game Boy Advance games that need a real link cable, such as Mario Kart
      Super Circuit, link between two phones with
      [Cable Link over Wi-Fi](../../mobile/netplay.md#cable-link-over-wi-fi).
    - DS, 3DS and PSP games play together through their own wireless
      modes. See the next question.

## Can I play DS, 3DS or PSP games wirelessly with a friend?

Yes. Put both devices on the same Wi-Fi, start the game on each, and use the
game's own wireless or ad hoc menu, as with two real consoles side by side.
There is nothing to set up. See
[Local Wireless](../../mobile/local-wireless.md).

??? info "More detail"
    - The name the others see is your
      [Player name](../../mobile/about.md#player-name).
    - While a game's wireless is on, the in-game menu is **Continue**,
      **Disconnect** and **Quit**, and save states, rewind and fast forward
      are off.

## Can I sync saves with my handheld?

Yes. **Tools → Device Sync** carries saves and save states between the phone
and an NX Redux handheld, over Wi-Fi or a USB-C cable. Update the handheld to
the latest NX Redux first. ROMs sync too when you turn them on, with
**All files access** allowed. See [Device Sync](../../mobile/device-sync.md).

## Can two people play on one phone?

Yes. Two to four people can play one game, each on their own controller.
Start the game and press a button on each controller to join. Nintendo 64,
GameCube, Wii, Sega Dreamcast, Arcade and TurboGrafx-16 take up to four
players, and most other home consoles two. See
[Local Multiplayer](../../mobile/multiplayer.md).

## Can a second player use the touch controls?

No. The on-screen [pad skin](../../mobile/controls.md#pad-skins) always
controls Player 1, so every other player needs a controller.

## Why did my Joy-Cons become two players?

Android sees a pair of Joy-Cons as two controllers, so each one joins as its
own player. Multitap adapters, such as the NES Four Score, aren't supported
yet either. See [Local Multiplayer](../../mobile/multiplayer.md#limits).

## Can I remap controller buttons?

Not freely. Each console has a fixed mapping, and face buttons work **as
printed**: your controller's `A` is the console's `A`. To swap the layout,
use **Controller Layout** in the in-game menu's
[Options](../../mobile/in-game-menu.md#options) **→ Controls**.

On a controller without a mode button, press `SELECT` + `START` to open the
in-game menu, or on the main menu the highlighted item's menu. If your controller's `SELECT`, `START` or `MENU` does the
wrong thing, bind it in
[System buttons](../../mobile/controls-settings.md#system-buttons). See
[Controls](../../mobile/controls.md).

??? info "More detail"
    - PlayStation, PSP, Sega, arcade and a few others go by position instead
      of by letter.
    - **Controller Layout** names your controller's letters: **Auto-detect**,
      **Xbox (A at the bottom)** or **Nintendo (A on the right)**. Pick the
      one that isn't your controller's for the console's original button
      positions, such as the right button as `A` on Super Nintendo with an
      Xbox pad.

## Can I move or resize the on-screen buttons?

Yes. **Tools → Settings → Appearance → Button layout** moves and resizes
the button groups of each console's pad skin. In a game, the same editor is
**Adjust buttons** in the in-game menu's **Options → Controls**. See
[Button layout](../../mobile/controls-settings.md#button-layout).

To play with the game filling the screen and see-through buttons over it,
turn [Pad skin](../../mobile/appearance.md#pad-skin) off.

## Can I type with my controller?

Yes. Search, rename, sign-ins and every other text prompt use NX Redux's own
keyboard, which works with the d-pad or touch. To use your phone's keyboard
instead, for a password manager or swipe typing, set **Tools → Settings →
System → Keyboard** to **Android**. See
[Keyboard](../../mobile/about.md#keyboard).

## Is there a RetroAchievements hardcore mode?

No, the same as on the handheld. RetroAchievements in the app is softcore
only, so cheats and save states are not blocked. See
[RetroAchievements](../../mobile/retroachievements.md).

## How do I find a game in a big library?

Press `START` on the main menu, or tap the **Search** icon, and type part of
its name. Case, accents, punctuation and word order don't matter, and
`fantasy 6` finds *Final Fantasy VI*. In a game list, `START` searches just
that list. See [Search](../../mobile/main-menu.md#search).

The [Games tab](../../mobile/main-menu.md#games-tab) lists every game from
every console, A to Z. `L2` / `R2` jump by letter there.

## Can I make the text smaller?

Yes. **Tools → Settings → Appearance → Text size** has **Large** (the
default) and **Small**. It sets the text of the lists, page titles and
button hints across the app. First-run setup asks it first. See
[Text size](../../mobile/appearance.md#text-size).

## Where does the game artwork come from?

The app fetches it. Open **Tools → Artwork** and pick **Fetch missing art**,
or **Fetch by console**. To fetch one game, press `MENU` on it and pick
**Fetch art**, or **Change art** once it has art, to pick the pictures you
like. See [Artwork](../../mobile/artwork.md).

??? info "More detail"
    - The art comes from ScreenScraper, libretro-thumbnails, TheGamesDB and
      SteamGridDB, and is saved in each game folder's `.media` folder. Art
      you put there yourself is used too.
    - Resting on a game in a list also fetches its missing art in the
      background. Turn that off with **Fetch art and info when browsing**
      in **Tools → Artwork → Settings**.

## Where do a game's genre, year and publisher come from?

From ScreenScraper, with the art. The app also looks them up in the
background for the game you rest on. A game shows **Game** until its info
has arrived. See [Game info](../../mobile/artwork.md#game-info).

A game with achievements shows them in that place by default. To show the
genre, year and publisher for every game, set **Layouts → Game info** to
**Details**. See [Game info](../../mobile/layouts.md#game-info).

## Why does artwork need a ScreenScraper account or API keys?

It doesn't have to. libretro-thumbnails needs nothing, and ScreenScraper
works without an account, on an allowance shared with other players.

- **Signing in to ScreenScraper** gives you your own daily allowance, which
  goes much further on a large library.
- **TheGamesDB** and **SteamGridDB** are only used with your own free API
  key.

Set them in **Tools → Artwork → Settings**. See
[Artwork](../../mobile/artwork.md).

## Can I use the app as my home screen?

Yes. Turn on **Use as home screen** in **Tools → Settings → System**. The
phone's Home key then brings you back to the app's **Home** tab. You can also
open any Android app from **Tools → Apps**, and add apps to **Tools**. See
[Launcher Mode & Android Games](../../mobile/launcher.md).

## Why do Android games have no play time?

The app only starts an Android game. The game runs in its own app, so NX
Redux can't tell how long you play. Android games have no play time, and
they don't show in recents or on the Continue card. See
[Launcher Mode & Android Games](../../mobile/launcher.md).

## Does the app work on foldables?

Yes. On a half-folded phone with a horizontal hinge, the game moves above the
fold and the controls go below it. This is automatic. On a wide screen, such
as an unfolded Fold held sideways, some pages split into two panes. See
[Foldables & Large Screens](../../mobile/foldables.md).

??? info "More detail"
    - Half-folded, Nintendo DS and 3DS games put the top screen above the
      fold and the touch screen below it, between the pad's halves, like
      the real handheld.
    - The pages that split into two panes are Settings, the in-game menu,
      RetroAchievements, Game Tracker and Artwork.

## I removed my SD card and some games disappeared

Games from a folder on a card that is not mounted are left out until the card
is back. **Tools → Settings → Library** marks the folder **Not available**. Nothing is lost. See
[Library & ROM folders](../../mobile/library.md).

## How do I use Kids Mode, and what if I forget the PIN?

**Tools → Settings → Kids Mode** opens games only in the play times you
set, behind a 6-digit PIN. Outside them your child sees large tiles of the
apps you allowed. It needs NX Redux as the home screen.

If you forget the PIN, delete the file `kids-mode.flag` in your home folder
with a file manager or from a computer. Kids Mode turns off and the PIN is
cleared; your play times and allowed apps stay. See
[Kids Mode](../../mobile/kids-mode.md).

## How do I send a log with a bug report?

Turn on **Tools → Settings → System → Debug log**, then repeat the
problem. The app writes a log file each time it or a game starts, to the
`Logs` folder in your home folder, such as
`20261109-203153-game-PS2-armsx2.log`. Attach that file to your report. No
computer is needed. See
[Debug log](../../mobile/about.md#debug-log).

## Will a still picture burn into my OLED screen?

**Screen care** guards against it, and is on by default in **Tools →
Settings → System**. Everything on screen shifts by a tiny step every 2
minutes, and a game left alone dims after 5 minutes without input. See
[Screen care](../../mobile/about.md#screen-care).

## Is there an iOS version?

Not yet. NX Redux runs on Android only for now. An iOS version follows
the Android one.
