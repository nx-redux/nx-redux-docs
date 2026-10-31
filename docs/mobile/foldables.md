# Foldables & Large Screens

NX Redux fits itself to the screen it's on. A half-folded foldable
gets Flex mode, a wide or large screen gets a fuller Home, and Settings and
the in-game menu split into two panes when there is room. For handhelds with
a second screen, and displays on USB-C, see
[Dual Screens & External Displays](dual-screen.md).

## Flex mode

Fold a foldable partway, like a small laptop, with the hinge running across
the screen. The app splits at the hinge:

- **Above the hinge:** the game, or the menu.
- **Below the hinge:**
    - in portrait, the portrait pad;
    - in landscape, the two pad halves, drawn solid;
    - with a controller connected, nothing. The lower half stays empty.

There is no setting. Flex mode starts when you fold the phone and stops when
you open it flat. It works in games and in the main menu alike, and a game
you start while half-folded starts in it. Nintendo DS and 3DS games get a
layout of their own: see [below](#nintendo-ds-and-3ds-half-folded).

??? info "More detail"
    - The hinge must run across the screen, and each half must be at least a
      quarter of the screen. A book-style fold, with the hinge from top to
      bottom, keeps the usual layout.
    - On a phone that doesn't report its half-folded state, such as the
      Galaxy Z Fold, the app reads the hinge angle: between 30° and 150°
      counts as folded.

### Nintendo DS and 3DS half-folded

Half-fold the inner screen of a foldable such as the Galaxy Z Fold, and a DS
or 3DS game is held like the real handheld:

- **Above the hinge:** the top screen, right against the fold.
- **Below the hinge:** the touch screen, right against the fold, with the
  pad either side of it: the d-pad on the left, the face buttons on the
  right, the shoulders above each, `MENU` `STICK` under the left side and
  `SELECT` `START` under the right, and **STYLUS** and **SWAP** on a second
  row.
- **With a controller connected:** no pad, and the touch screen alone below
  the hinge, bigger.

The touch screen takes touches, and **SWAP** trades the two screens across
the hinge. Fold or open the phone mid-game and the layout follows; your
[layout](emulators/nintendo-ds.md#screen-layouts) comes back when the phone
is flat.

??? info "More detail"
    - The DS screens are drawn at whole-number scales: on the Galaxy Z Fold,
      the top screen at 6× and the touch screen at 4×. The 3DS screens fill
      their room at their shape.
    - The buttons are the size of the cover screen's pad, and always solid.
      The touch screen may run under each side's buttons by a quarter of
      their reach at most.
    - While half-folded, `SELECT` + `LEFT` / `RIGHT` doesn't change the
      layout and shows **Layout is set by the fold**. On a phone that can
      half-fold, the **Layout** rows in Console Settings say they set the
      layout used when the phone isn't half-folded.
    - On a narrower foldable, such as a Galaxy Z Flip, there is no room for
      the touch screen between the pad's halves: both screens stack above
      the hinge, and the portrait pad sits below it.
    - If the hinge reading leaves no room for this layout, the game keeps
      its flat layout.
    - Move or resize these buttons with **Half-folded** in
      [Pad layout](controls-settings.md#pad-layout).
    - With a [second screen](dual-screen.md#nintendo-ds-and-3ds) the game
      keeps the split across the two screens instead.

## Home on wide and large screens

Home lays itself out for the screen's shape. In portrait and on most
screens it looks as in [Main Menu](main-menu.md#home). On a wide or large
landscape screen, such as a Galaxy Z Flip sideways or an unfolded Galaxy Z
Fold, the tool squares, and the first one or two pinned games, sit beside
the Continue card.

??? info "More detail"
    **Wide face:** a phone in landscape with a 20:9 or wider screen, such as
    a Galaxy Z Flip.

    - The first one or two pinned games sit beside the Continue card, in the
      top section. The rest go in rows below it, a scroll away.
    - The pinned tools are smaller squares, five to a column, up to three
      columns. With more, the last square is **+N**, which opens Tools.

    **Large face:** a landscape screen at least 840 × 480 dp, such as an
    unfolded Galaxy Z Fold or a tablet.

    - The top section is as on the wide face: Continue, the first one or two
      pinned games and the tool squares, five to a column, up to two columns.
    - The other pinned games fill the rows below, four to a row.
    - Under them come the [shelves](#shelves), up to four games each in one
      row, at the pinned games' size.

### Shelves

Home shows up to four shelves of games from your library, to help you
pick something to play. They show on every screen size and in every Home
layout.

| Shelf | What it holds |
| --- | --- |
| **Most played** | The games you've played longest, most first, each with its play time. Right under your pinned games. |
| **New** | Games the app first found in the last 30 days, newest first. |
| **Not started** | Games you have never played. Picked again each day. |
| **Pick up again** | Games you last played more than 14 days ago, most played first. |

[Layouts](layouts.md) can hide the **Most played**, **New** and **Not
started** shelves, each with its own row in **Layouts → Home**. **Pick up
again** always shows when it has games.

??? info "More detail"
    - Shelves show in portrait and landscape alike. Each shelf shows only
      when it has games, and a game is never on two shelves, the shelves
      filling in the order of the table. A shelf holds at most 4 games; Grid
      Home in landscape shows as many whole rows as fit within that.
    - Each shelf has its name as a label above it; on Carousel and List Home
      each game wears it as a badge or tag instead. A **Most played** game's
      badge is its play time.
    - The game on the Continue card, your pinned games, Unassigned games and
      Android games are left off the shelves.
    - A hidden shelf takes no games, so the shelves after it can show them.

## Two-pane screens

On a wide screen, such as most phones in landscape or an unfolded Fold held
sideways, some pages show two panes side by side. Portrait screens keep one
page at a time.

??? info "More detail"
    A window counts as wide when it is at least 600 dp wide and at least 1.3
    times as wide as it is tall.

### Settings

**Tools → Settings** shows its sections on the left and the selected
section's page on the right. Moving through the sections previews each page.

### RetroAchievements

Below the [RetroAchievements](retroachievements.md) page, each level opens
beside the one it came from, such as an achievement's details beside the
game's achievements list. The page you came from stays on the left, dimmed.
The [Game Tracker](game-tracker.md) shows a game's sessions the same way.

??? info "More detail"
    The dimmed page keeps the row that opened the right pane highlighted. A
    game's achievements open beside the games list.

### Artwork

[Artwork](artwork.md) works the same way: its pages open beside the
Artwork page. Tap a row in the dimmed left pane to open it instead.

??? info "More detail"
    **Fetch by console**, **Progress** and **Settings** open beside the
    Artwork page, and **Reset artwork** beside Settings. The page you came
    from keeps its row lit.

### In-game menu

The [in-game menu](in-game-menu.md) splits too:

- On the first page, the right pane shows the save slot on **Save** and
  **Load**, and the [game panel](in-game-menu.md#the-game-panel) on the
  other rows.
- Deeper in, the open page is on the right and the page it came from on the
  left, dimmed.
- Deeper in, `RIGHT` on a row that opens a page opens it, as `A` does. On
  the first page, `RIGHT` moves into the game panel. Value rows still change
  with `LEFT` / `RIGHT`.
- Tap a row in the dimmed pane to go back to it.
