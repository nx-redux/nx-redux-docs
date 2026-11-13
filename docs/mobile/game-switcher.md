# Game Switcher

The Game Switcher shows your recent games, ready to resume any of them where
you left off. Open it with `SELECT` (**Recent**) on the main menu or in a game
list, or tap the **Recent** icon at the top right.

It has two layouts, picked in
[**Tools → Settings → Layouts → Game Switcher → Layout**](layouts.md#game-switcher-layout):
**Full screen** (the default) and **List**.

??? info "More detail"

    The **Recent** icon always shows: at the top right of the main menu, and
    at the right of a game list's title.

## Full screen

![The Game Switcher showing Mario Kart DS, Nintendo DS 2 / 15, with its time and achievements over the Remove, Back and Resume hints](../assets/screenshots/mobile/game-switcher.webp)

Each game fills the screen with its picture, with its name, console and place
in the list, such as **1 / 23**. The info line above the hints shows when you
last played it and for how long, then its achievements, or its genre, year
and publisher, as [Game info](layouts.md#game-info) picks.

- `LEFT` / `RIGHT`, or a swipe, move between games.
- `A` **Resume**, or a tap on the picture, continues the game.
- `Y` **Remove** takes the game out of your recent games, after asking.
- `B` **Back**, or `SELECT` again, returns to where you were.

??? info "More detail"

    - With [**Game info**](layouts.md#game-info) on **Achievements** (the
      default), the info line shows your achievement progress and the next
      achievement to unlock, for games that have achievements. Other games,
      and every game with **Details**, show the genre and release.
    - **Remove** asks **Remove "‹name›" from recents?**; choose **Remove** to
      confirm.
    - On a touchscreen with no controller there is no hint bar: **Remove** is
      a trash icon at the top right, level with the game's name.
    - `LEFT` and `RIGHT` stop at the first and last game; they do not wrap.

## List

Your recent games as a list titled **Recent**, drawn like a
[List](main-menu.md#games-list) game list, with the selected game's picture behind the
rows.

![The Game Switcher in List: Streets of Rage 2 selected over its picture, then Contra - Hard Corps, Comix Zone, Sonic 3D Blast and Super Street Fighter II, with its time and achievements at the bottom](../assets/screenshots/mobile/game-switcher-list.webp)

- `UP` / `DOWN` move through the games.
- A tap on a row highlights it, and a second tap resumes it.
- `A` **Resume**, `Y` **Remove** and `B` **Back** work as in Full screen.

??? info "More detail"

    - `UP` on the first game wraps to the last and `DOWN` on the last to the
      first, on a fresh press only: holding the button stops at the end.
      `LEFT` and `RIGHT` do nothing.
    - The selected game's info sits under the **Recent** title, as in a List
      game list. With **Page title** hidden it moves to the bottom row,
      while Button hints is hidden or with touch alone.
    - Two games with the same name from different consoles show the
      console's tag, such as **Tetris (GB)**, or their whole file names when
      those differ only by extension, such as **Tetris.nes (FC)**. A copy of a
      game kept in an extra folder shows that folder's name after the title,
      dimmed.
    - The background is the first of these that loads:

        1. the screenshot of the game's resume point, with any black bars
           trimmed off,
        2. its screenshot,
        3. its generated abstract picture.

    - With no recent games, the List shows the same **No Recents** screen as
      Full screen.

## The picture

In Full screen the picture is the game's resume point screenshot, or else its
box art. The box follows **Backdrop art** in
[Layouts](layouts.md#backdrop-art). See [Artwork](artwork.md) for where box
art comes from.

??? info "More detail"

    The switcher shows the first of these it has for the game:

    1. the screenshot of its resume point,
    2. the box art **Backdrop art** names, then its 3D box art, its 2D box
       art, then its wheel, shown in a case,
    3. **No Preview**.

## Play time and achievements

The info line follows [**Extra info**](layouts.md#extra-info),
[**Game info**](layouts.md#game-info) and
[**Button hints**](layouts.md#page-title-and-button-hints) in
**Tools → Settings → Layouts**, in both layouts.

??? info "More detail"

    - With **Extra info** hidden, the info line is left out.
    - **Game info** picks what follows the play time: the game's genre, year
      and publisher (**Details**) or its achievements (**Achievements**,
      the default).
    - With **Button hints** hidden, the hint bar's row stays, without hints.
      In Full screen the info line moves into it, and the row keeps its dark
      shade so the line reads over a light picture.

## Always resumable

Every game you have played can be resumed, with no manual save state needed:

- **Save & Quit** in the [in-game menu](in-game-menu.md#quitting) saves your
  place, and so does leaving the app while a game is open.
- **Quit** leaves the last resume point as it was.

PICO-8 is the exception for now (see [Emulators](emulators/index.md#limits)).

??? info "More detail"

    The resume point is a hidden resume state. This works with nearly every
    core.

## Only resumable games are listed

The switcher lists only recent games that can be resumed. With none, it shows
**No Recents** and **Play a game to see it here**. Android games are never
listed.

In a game list, `A` **Resume** resumes the highlighted game when it can. To
start it fresh instead, choose **Play from start** in its `MENU` menu.

??? info "More detail"

    Unlike the handheld, there is no setting to list every recent game
    instead.
