---
title: Local Wireless
---

# Local Wireless

Nintendo DS, Nintendo 3DS and PSP games play their own wireless
multiplayer between phones on the same Wi-Fi, or between two phones on a
USB cable, the way real consoles side by side do. There is nothing to set up and no address to type: start the
game on each phone and use the game's own multiplayer menu.

| Console | The game's mode | Players | Links over |
| --- | --- | --- | --- |
| [Nintendo DS](emulators/nintendo-ds.md) | DS wireless play, including [DS Download Play](#ds-download-play) | Up to 8 in a room | Wi-Fi, or a USB cable between two phones |
| [Nintendo 3DS](emulators/nintendo-3ds.md) | Local play, including Download Play | Set by the game | Wi-Fi, or a USB cable between two phones |
| [PSP](emulators/psp.md) | Ad hoc | 2 to 4 | Wi-Fi, or a USB cable between two phones |

Local wireless is between phones and other Android devices running NX
Redux. An NX Redux handheld can't join. For every other system, and for
Game Boy link cables, see [Netplay](netplay.md).

## Starting a game

1. Put every phone on the same Wi-Fi, or join two phones with a
   [USB cable](#usb-cable). For DS games, one phone's hotspot works too.
2. Start the same game on each phone, the normal way.
3. Use the game's own multiplayer menu on each: one player creates or
   hosts, the others search and join, as on the real console.

The phones find each other when the game turns its wireless on. Until
then nothing is sent on the network.

!!! tip "Less lag: a USB cable, or a hotspot for DS"
    A home router adds delay between phones, and DS and 3DS games wait for
    each other's answers many times a second. For the smoothest game:

    - **Two phones:** join them with a [USB cable](#usb-cable).
    - **DS games:** or put the others on one phone's hotspot, instead of
      the home Wi-Fi.

    With two phones playing Mario Party DS, the home Wi-Fi ran at about 21
    fps, the host's hotspot at 50 to 54, and the cable at nearly full speed.

!!! tip "Other players see your Player name"
    Set it in **Settings → System →
    [Player name](about.md#player-name)**. It is the DS nickname, the
    3DS's profile and Mii name, and your name in PSP ad hoc.

??? info "More detail"

    - A DS or 3DS game leaves its room 10 seconds after it turns its
      wireless off.
    - A PSP game goes on the network at its first ad hoc search, create or
      join.
    - Only a game's local modes link. Online modes that used Nintendo
      Wi-Fi Connection don't.
    - Each phone has its own console address, so games tell the players
      apart. A DS `firmware.bin` of your own is never changed.
    - A game keeps the name stored in its own save, so an old save can
      show an old name.
    - A DS game also finds rooms on a phone's own hotspot, with that
      phone's Wi-Fi on or off.

### The Local Wireless option

Each of the three consoles has a **Local Wireless** option, **On** by
default, in the **Multiplayer** group of
[Emulator Settings](emulator-settings.md) and Game Settings. It is read
when a game starts.

| Value | What it does |
| --- | --- |
| **On** | A game's wireless finds other NX Redux devices on the same Wi-Fi, or on the USB cable, by itself. |
| **Off** | Games don't look for other devices. You can still host or join from the [Netplay menu](#from-the-netplay-menu). |

Turn it off on a network you share with people you don't want to play
with.

### From the Netplay menu

DS, 3DS and PSP games also have `Y` **Netplay**. One phone picks **Host
Game**, the other **Join Game** and then the host, and both games start.
Then use the game's own multiplayer menu as above. See
[Netplay → Starting a session](netplay.md#starting-a-session).

This works with **Local Wireless** off. On DS and 3DS, a game hosted this
way is also found by phones that just started the game. A PSP game hosted
over **USB Cable** is only found by the phone on the cable.

### USB cable

Two phones can link a DS, 3DS or PSP game over a USB-C to USB-C cable
instead of Wi-Fi. Plug the cable in and play as usual: with another phone
on the USB port, the game starts the cable link itself. A DS or 3DS game
starts it when it turns its wireless on, a PSP game as soon as it starts.

- **Android asks once to allow a VPN.** It only carries the cable link.
- **Android may ask to allow the USB device.** Allow it on both phones.
- **Host first.** Create the game's room on one phone, then search on the
  other.
- **Two phones only.** Three or more players use Wi-Fi.
- **No Wi-Fi needed.** The cable alone is enough.

#### PSP over the cable

A PSP game is on one network at a time: the cable or the Wi-Fi, never
both.

- **Plug in before you enter ad hoc.** Both phones then meet over the
  cable.
- **A cabled pair plays alone.** A third phone on Wi-Fi can't join them.
- **Pull the cable** and both games drop out of ad hoc and go back to
  Wi-Fi. Enter the game's ad hoc menu again to meet there.

??? info "More detail"

    - Android's VPN and USB questions show over the game and take it out
      of the room. Answer them: a DS or 3DS game then looks for the room
      again by itself. On PSP, enter the game's ad hoc menu again.
    - A computer on the USB port doesn't start the cable.
    - From the Netplay menu, set **Connection** to
      [**USB Cable**](netplay.md#usb-cable).
    - A DS or 3DS room joined over Wi-Fi stays on Wi-Fi when a cable is
      plugged in later.
    - Plug a cable in while a PSP game is in its ad hoc lobby and the game
      drops out of the lobby. Enter it again and it uses the cable.
    - Starting a PSP game with a phone on the cable switches the other
      phone to the cable too, and can bring NX Redux to the front there.
    - A PSP game entering ad hoc while the cable is still coming up waits
      up to 6 seconds for it.

## DS Download Play

Some DS games play together from one copy: the host runs the game, and
each guest downloads it from the host, with no copy of their own. Mario
Party DS plays together only this way.

![The Nintendo DS list on a Retroid Pocket Nova with DS Download Play selected: its box reads Play together from one Game Card, and the line under it reads System, 2004 · Nintendo](../assets/screenshots/mobile/ds-download-play-row.webp){ .nx-wide }

1. On the host's phone, start the game and pick its DS Download Play mode
   (in Mario Party DS, **Multiplayer**).
2. On each guest's phone, open the **Nintendo DS** console and start
   **DS Download Play**, its first row. The DS menu opens, as on a DS with
   no game card.
3. Pick the host's game from the list. It downloads, then starts.

!!! note "Needs a real DS's BIOS and firmware"
    Copy `bios7.bin`, `bios9.bin` and `firmware.bin` from your own DS into
    `Bios/NDS/`. **DS Download Play** shows only when they are there. With
    no DS games in your library, a **Nintendo DS** console then shows with
    just that row.

!!! tip "Smoothest on the cable or a hotspot"
    The host waits for each guest's answer several times a frame, so
    [less lag](#starting-a-game) matters most here: use a
    [USB cable](#usb-cable) or the host's hotspot rather than the home
    Wi-Fi.

??? info "More detail"
    - The guest's game is gone when it ends, as on a DS: start
      **DS Download Play** again for the next session.
    - DS Download Play has no save states, resume point or achievements,
      and makes no Recents entry. Its in-game menu has no **Save** or
      **Load**.
    - Quitting from the DS menu closes it, as **Quit** does.

## In a session

While the game's wireless is on, the in-game menu shows only three rows:

| Row | What it does |
| --- | --- |
| **Continue** | Back to the game. |
| **Disconnect** | Leaves local multiplayer. The game plays on. |
| **Quit** | Closes the game. No resume point is written. |

The full menu comes back by itself when the game turns its wireless off.

The game keeps running under the menu in a room, so the other players
aren't held up.

!!! warning "Come back within 60 seconds"
    A menu left open in a room for 60 seconds disconnects by itself. The
    row counts down, such as **Disconnect (45s)**.

Switched off while the wireless is on:

- Save states and loading one. A load is refused with a message.
- Rewind, fast forward and reset.
- **Options**, cheats and the **Players** tab.

Their touch shortcuts and second-screen tiles hide too.

Pressing Home, turning the screen off or switching to another app leaves
the room. Back in a DS or 3DS game, with **Local Wireless** on, your phone
looks for the room again.

### Disconnect

**Disconnect** takes your phone out of the room with the game still
running. The other players' games see you drop out, as if your console
was switched off: on DS everyone gets the game's own communication error.
Your phone stays out until the game turns its wireless off and on
again (on PSP, until you leave ad hoc mode and enter it again); then it
finds the others as before.

After a session started from the Netplay menu, **Disconnect** does the
same when **Local Wireless** is on. With it off, the game stays offline
until you quit it.

## Limits

- Phones only: no NX Redux handheld, and no real DS, 3DS or PSP.
- Every phone needs to be on the same Wi-Fi network, or, for two phones,
  on the USB cable. DS games also link on one phone's hotspot.
- PSP players on the cable and players on Wi-Fi can't share a game.
- No save states, rewind or fast forward while a game's wireless is on.
