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
| [Nintendo 3DS](emulators/nintendo-3ds.md) | Local play, including [3DS Download Play](#3ds-download-play) | Set by the game | Wi-Fi, or a USB cable between two phones |
| [PSP](emulators/psp.md) | Ad hoc | 2 to 4 | Wi-Fi, or a USB cable between two phones |

Local wireless is between phones and other Android devices running NX
Redux. An NX Redux handheld can't join. For every other system, and for
Game Boy link cables, see [Netplay](netplay.md).

## Starting a game

1. Put every phone on the same Wi-Fi, or join two phones with a
   [USB cable](#usb-cable). For DS and 3DS games, one phone's hotspot works too.
2. Start the same game on each phone, the normal way.
3. Use the game's own multiplayer menu on each: one player creates or
   hosts, the others search and join, as on the real console.

The phones find each other when the game turns its wireless on. Until
then nothing is sent on the network.

!!! tip "Less lag: a USB cable or a hotspot"
    A home router adds delay between phones, and DS and 3DS games wait for
    each other's answers many times a second. For the smoothest game:

    - **Two phones:** join them with a [USB cable](#usb-cable).
    - **DS and 3DS games:** or turn on one phone's hotspot, turn that
      phone's own Wi-Fi off, and put the others on the hotspot. With its
      Wi-Fi still on, the phone shares one radio between the two networks
      and the game slows down.

    With two phones playing Mario Party DS, the home Wi-Fi ran at about 21
    fps, the host's hotspot at 50 to 54, and the cable at nearly full speed.
    Mario Kart 7 on the hotspot ran at about 50 fps with the host's Wi-Fi
    on and close to 60 with it off.

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
    - DS and 3DS games also find rooms on a phone's own hotspot, with that
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

![DS Download Play's picture in the list: a soft gradient with translucent shapes](../assets/screenshots/mobile/ds-download-play.webp){ .nx-wide }

1. On the host's phone, start the game and pick its DS Download Play mode
   (in Mario Party DS, **Multiplayer**).
2. On each guest's phone, open the **Nintendo DS** console and start
   **DS Download Play**, its first row. It lists the games hosted nearby.
3. Pick the host's game and press `A`. It downloads, then starts.

Nothing of the player's is needed: no game, no BIOS, no firmware.
**DS Download Play** is always in the Nintendo DS list, and a library with
no DS games gets a **Nintendo DS** console with just that row.

!!! tip "Smoothest on the cable or a hotspot"
    The host waits for each guest's answer several times a frame, so
    [less lag](#starting-a-game) matters most here: use a
    [USB cable](#usb-cable) or the host's hotspot (its own Wi-Fi off)
    rather than the home Wi-Fi.

??? info "More detail"
    - The downloaded game is kept for next time: joining the same game
      again skips the download, unless the host's game is another version.
      Start **DS Download Play** again for each session.
    - When the host leaves, the guest's game closes a few seconds later.
    - It is our own app in place of the DS menu's Download Play, so a
      guest needs no files from a DS. Its downloads are kept for this
      phone only.
    - DS Download Play has no save states, resume point or achievements,
      and makes no Recents entry.
    - It shows the top screen alone until the game starts, then your
      layout. Until then its in-game menu is **Continue** and **Quit**.

## 3DS Download Play

3DS games with Download Play, such as Mario Kart 7, let friends without the
game join from one copy: the host plays the full game, and each guest
receives a smaller version of it for the session.

![3DS Download Play's picture in the list: a soft gradient with translucent shapes](../assets/screenshots/mobile/3ds-download-play.webp){ .nx-wide }

1. On the host's phone, start the game and go to its local multiplayer
   (in Mario Kart 7, **Local Multiplayer**).
2. On each guest's phone, open the **Nintendo 3DS** console and start
   **3DS Download Play**, its first row.
3. Pick the host's game and press `A`. When the host starts the game, it
   downloads and starts.

Nothing of the player's is needed: no game, no BIOS, no system files.
**3DS Download Play** is always in the Nintendo 3DS list, and a library
with no 3DS games gets a **Nintendo 3DS** console with just that row.

!!! tip "Smoothest on the cable or a hotspot"
    A slow guest pulls the race out of sync. Use a [USB cable](#usb-cable)
    or the host's hotspot (its own Wi-Fi off), and keep the guest at full
    speed: on a phone with a Mali GPU, 3DS Download Play starts on Vulkan
    with your custom GPU driver, or at 1x 3D resolution without one.

??? info "More detail"
    - The downloaded game is kept for next time: joining the same game
      again skips the download, unless the host's game is another version.
    - When the host leaves, the guest's game closes a few seconds later.
    - A system message over the game, such as the USB prompt, keeps the
      session. Switching to another app ends it: the downloaded game can't
      rejoin its host.
    - **Local Wireless** has to be on (Game Settings → Multiplayer).
    - If you own the game too and have played it once on this phone, its
      Game Settings apply to the downloaded game, except the graphics, 3D resolution, layout and controls, which
      come from **3DS Download Play**'s own Game Settings.
    - No save states, resume point or achievements, and no Recents entry.
    - It shows the top screen alone until the game starts, then your
      layout. Until then its in-game menu is **Continue** and **Quit**.
    - It is our own app in place of the 3DS's Download Play, so a guest
      needs no files from a 3DS. Its downloads are kept for this phone only.

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
looks for the room again. **Reset** does the same.

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
  on the USB cable. DS and 3DS games also link on one phone's hotspot.
- PSP players on the cable and players on Wi-Fi can't share a game.
- No save states, rewind or fast forward while a game's wireless is on.
