---
title: Local Wireless
---

# Local Wireless

Nintendo DS, Nintendo 3DS and PSP games play their own wireless
multiplayer between phones on the same Wi-Fi, the way real consoles side
by side do. There is nothing to set up and no address to type: start the
game on each phone and use the game's own multiplayer menu.

| Console | The game's mode | Players | Links over |
| --- | --- | --- | --- |
| [Nintendo DS](emulators/nintendo-ds.md) | DS wireless play | Up to 8 in a room | Wi-Fi, or a USB cable between two phones |
| [Nintendo 3DS](emulators/nintendo-3ds.md) | Local play, including Download Play | Set by the game | Wi-Fi, or a USB cable between two phones |
| [PSP](emulators/psp.md) | Ad hoc | 2 to 4 | Wi-Fi |

Local wireless is between phones and other Android devices running NX
Redux. An NX Redux handheld can't join. For every other system, and for
Game Boy link cables, see [Netplay](netplay.md).

## Starting a game

1. Put every phone on the same Wi-Fi.
2. Start the same game on each phone, the normal way.
3. Use the game's own multiplayer menu on each: one player creates or
   hosts, the others search and join, as on the real console.

The phones find each other when the game turns its wireless on. Until
then nothing is sent on the network.

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

### The Local Wireless option

Each of the three consoles has a **Local Wireless** option, **On** by
default, in the **Multiplayer** group of
[Emulator Settings](emulator-settings.md) and Game Settings. It is read
when a game starts.

| Value | What it does |
| --- | --- |
| **On** | A game's wireless finds other NX Redux devices on the same Wi-Fi by itself. |
| **Off** | Games don't look for other devices. You can still host or join from the [Netplay menu](#from-the-netplay-menu). |

Turn it off on a network you share with people you don't want to play
with.

### From the Netplay menu

DS, 3DS and PSP games also have `Y` **Netplay**. One phone picks **Host
Game**, the other **Join Game** and then the host, and both games start.
Then use the game's own multiplayer menu as above. See
[Netplay → Starting a session](netplay.md#starting-a-session).

This works with **Local Wireless** off. On DS and 3DS, a game hosted this
way is also found by phones that just started the game.

### USB cable

Two phones can link a DS or 3DS game over a USB-C to USB-C cable instead
of Wi-Fi. Plug the cable in and play as usual: when the game turns its
wireless on and another phone is on the USB port, the game starts the
cable link itself.

- **Android asks once to allow a VPN.** It only carries the cable link.
- **Host first.** Create the game's room on one phone, then search on the
  other.
- **Two phones only.** Three or more players use Wi-Fi.
- **Not for PSP.** PSP games link over Wi-Fi only.

??? info "More detail"

    - Android's VPN question shows over the game and takes it out of the
      room. Answer it, then enter the game's wireless menu again.
    - A computer on the USB port doesn't start the cable.
    - From the Netplay menu, set **Connection** to
      [**USB Cable**](netplay.md#usb-cable) for a DS or 3DS game.
    - A room joined over Wi-Fi stays on Wi-Fi when a cable is plugged in
      later.

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
the room.

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
- No USB cable for PSP.
- A PSP game started with no Wi-Fi stays offline until you start it
  again.
- Every phone needs to be on the same Wi-Fi network, or, for two phones
  on DS and 3DS, on the USB cable.
- No save states, rewind or fast forward while a game's wireless is on.
