# Privacy Policy

How the NX Redux mobile app handles your data. This covers the app from Google
Play and the APK from GitHub.

*Last updated: 26 October 2026*

## In short

NX Redux has no accounts of its own, no ads, no analytics and no crash
reporting. Your games, saves, settings and play time stay on your device. The
app only sends data over the internet when you use a feature that needs an
online service, and only to that service.

## What stays on your device

- Your games, BIOS files, saves, save states and screenshots.
- Settings, controls, collections, play time and Recently Played.
- Downloaded artwork, cheats and achievement badges.
- The debug log, when you turn it on under Developer. It is only shared if you
  send the file yourself.

The developers of NX Redux never receive any of this.

## Online services the app uses

Each service is used only when you turn on or use the feature. What it receives
is covered by that service's own privacy policy.

| Service | Used for | What it receives |
| --- | --- | --- |
| [RetroAchievements](https://retroachievements.org) | Achievements (optional, needs your account) | Your username and password when you sign in, then a sign-in token; which game you play, identified by a hash of the game file; the achievements you unlock |
| [ScreenScraper](https://www.screenscraper.fr) | Artwork | The game's file name, a checksum and size of the file, and the system; your ScreenScraper username and password if you sign in |
| [TheGamesDB](https://thegamesdb.net) | Artwork (optional, needs your own key) | The game's name and system, and your API key |
| [SteamGridDB](https://www.steamgriddb.com) | Artwork (optional, needs your own key) | The game's name, and your API key |
| [libretro thumbnails](https://thumbnails.libretro.com) | Artwork | The game's name and system |
| [libretro buildbot](https://buildbot.libretro.com) | Cheat database download | Nothing beyond the download request |
| [GitHub](https://github.com) | Update check, GitHub APK only | Nothing beyond the download request. The Google Play app is updated by Google Play instead |

All of these connections use HTTPS. Like any website, each service also sees
your IP address when the app connects to it.

Your RetroAchievements password is not stored: the app keeps only the sign-in
token RetroAchievements returns. Your ScreenScraper login and any API keys are
stored only in the app on your device, to make requests on your behalf.

## Playing and syncing with other devices

Netplay and Device Sync connect straight to your other device over the same
Wi-Fi network or a USB cable. Nothing passes through an NX Redux server, and
there is no online matchmaking.

## Permissions

| Permission | Why |
| --- | --- |
| Internet and network state | The online services above, and Netplay and Device Sync on your Wi-Fi |
| Wi-Fi multicast | Finding your other device on the same Wi-Fi |
| Notifications and foreground service | Showing progress while a Device Sync runs |
| Vibration | Feedback from the on-screen controls |
| All files access (GitHub APK only, optional) | Reading your games and saving to a folder you choose anywhere on your storage. The Google Play app uses its own folder and folders you pick instead |
| Install packages (GitHub APK only) | Installing an update you download from inside the app |

## Deleting your data

- **Sign out** of RetroAchievements or ScreenScraper in Settings, and the app
  deletes the stored sign-in.
- **Uninstall** the app to remove everything it stores in its own storage. In
  the Google Play app this includes its games folder, `Android/media/`, so back
  up your saves first.
- Data held by RetroAchievements or ScreenScraper, such as your account or
  unlocked achievements, is deleted through those services.

## Children

NX Redux is not directed at children under 13 and does not knowingly collect
data from them.

## Changes

If this policy changes, the new version is posted on this page with a new date.

## Contact

Questions about privacy: open an issue on
[GitHub](https://github.com/nx-redux/nx-mobile/issues).
