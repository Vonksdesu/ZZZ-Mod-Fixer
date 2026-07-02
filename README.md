# ZZZ-Mod-Fixer (Community Update)

This is a Python-based tool designed to update and fix character skin mod hash IBs for the game **Zenless Zone Zero (ZZZ)** to ensure compatibility with the latest versions of the game.

---

## About The Project

This project is a community-driven continuation of the original **ZZZ-Mod-Fixer** tool. 

Since the original creator is no longer releasing updates, I have taken the initiative to independently maintain the program and keep it updated for newer game versions of *Zenless Zone Zero*.

### Core Features & Improvements:
* **Continuous Hash Updates**: The character hash database is regularly updated to support newer game versions. To see which exact game version is currently supported, please check the [Releases](../../releases) page (where all version-specific updates are posted).
* **Backup File Conflict Fix**: In the original version, updated `.ini` mod files often conflicted with the backup (original) `.ini` files when left in the same folder. I have modified the code to automatically move the old/backup `.ini` files to a separate folder, preventing any conflicts and keeping your mod directory clean.

*Note: This tool is exclusively designed to fix and update character skin mods. It is not intended for other types of mods.*

---

## Project Origins & Credits

This project is built upon the amazing work of the original creators in the modding community.

* **Original Tool on GameBanana**: [ZZZ-Mod-Fixer (GameBanana)](https://gamebanana.com/tools/21671)
* **Original Owner**: [petrascyll](https://gamebanana.com/members/2644630)
* **Contributors**:
  * [HammyCate](https://gamebanana.com/members/3539653)
  * [EnteleJiang](https://gamebanana.com/members/4064027)
  * [leotorrez](https://gamebanana.com/members/5127033)
  * [ConfoundedHermit](https://gamebanana.com/members/3335346)

---

## Character Hash Source

I used a data source containing character hashes from other GitHub users, the result is not entirely my own work.

* **Character hash data source**: [hefengchang (GreenLzz)](https://github.com/hefengchang)

---

## Requirements

Before using this tool, make sure you have the following installed:
* **XXMI Launcher** (by SpectrumQT): This fixer is designed to work specifically with the directory structure created by this launcher.
  * Download the official launcher here: [SpectrumQT/XXMI-Launcher](https://github.com/SpectrumQT/XXMI-Launcher)

---

## How to Use

1. **Download**: Download the latest `zzz-mod-fixer-v3.0.exe` from the [Releases](../../releases) page.
2. **Placement**: Place the `.exe` file **directly** inside the `Mods` folder within your **XXMI Launcher** installation directory. 
   > ⚠️ **Important:** Do *not* create a new folder for the `.exe` inside the `Mods` folder, as the program may not work properly.
3. **Run**: Run the program and wait for the process to complete.
4. **Launch**: Once the process is finished, open your **XXMI Launcher** and launch *Zenless Zone Zero*.

### ⚠️ Notice for Users of the Original ZZZ-Mod-Fixer

If you have previously processed your mods using **Petrascyll's original tool**, you may experience conflicts due to left-over backup files that cause the mods to fail to load. 

To resolve this, please choose one of the two options below:

#### **Option 1: Quick Cleanup (Manual)**
Use this option if you want to keep your current mod setup:
1. Open your mod folder(s).
2. Manually find and **delete** all old backup `.ini` files that start with `DISABLED_BACKUP_` (e.g., `DISABLED_BACKUP_1.ini`).
3. Run the game via **XXMI Launcher**.

#### **Option 2: Clean Setup (Highly Recommended)**
This is the most recommended method to prevent any hidden conflicts and ensure the best results:
1. **Delete all mod folders** inside your main `Mods` directory.
2. Replace them with **fresh, untouched mod files** (use backups that have *never* been modified or processed by Petrascyll's original program).
3. Place and run my `zzz-mod-fixer-v3.0.exe` inside the `Mods` folder to automatically update them.
4. Launch the game via **XXMI Launcher**.

### ⚠️ Attention to users who have problems with Windows Security

If you're having trouble running the `zzz-mod-fixer.exe` file due to Windows Security, you can run it using the `run-fixer.bat` file in the `Source Codes` folder.

So, the first thing you need to do is download the `Source Codes` folder in `.zip` format (where you want to place it). Once downloaded, extract the folder. Then, you need to copy three things. But before copying these three things, create a special folder to store the three things you'll copy later (you can name it whatever you like).

After creating the special folder, copy these three things:

1. `Assets/PlayerCharacterPYData` folder
2. `zzz-mod-fixer.py` file
3. `run-fixer.bat` file

After you've copied these three things, place them in your custom folder. Then you put the folder you created in the main `Mods` folder, not the ZZZ mods folder directly. Then, you can run the `run-fixer.bat` file.

---

## Troubleshooting & FAQs

### ❓ My mod is still broken after running the fixer. What should I do?
If you have successfully run the program but your mod is still not working, please check the following:

* **Check the Premium Skin Requirement**: Some skin mods are specifically designed to replace *premium, paid, or event-exclusive* character skins rather than the character's default skin. **You must actually own that specific premium skin in-game** for the mod to work. If you do not own the required premium skin, the mod will remain broken even after updating the hashes.
* **Read the Mod Creator's Instructions**: Always carefully read the instructions, description, and requirements provided by the original mod author on GameBanana. Some mods require extra steps, specific settings, or unique files to function correctly. In many cases, a broken mod is caused by user error or missing a step in the author's guide, rather than an outdated hash.

### ❓ My mod textures are glitched or some parts are missing. Is it a folder issue?
Yes, **poor folder organization and nested folders are the most common causes of broken mods.** Please follow these rules after downloading a mod:

* **Do Not Blindly Drag and Drop**: When you download a `.zip` or `.rar` mod from GameBanana and extract it, **do not just blindly drop the extracted folder straight into your `Mods` directory.**
* **Rename the Folder**: First, rename the extracted folder to a clear and recognizable name so you can easily identify and manage it in the future.
* **Inspect the Folder Structure**: Open the extracted folder and look inside before placing it.
  * *Is it just a flat list of files, or are there sub-folders?* 
  * If there are sub-folders, check what they are. Sometimes, modders bundle multiple different skin options, recolors, or weapon variants for the same character in one single download. Each of these options has its own unique 3D model structures, coordinates, and hashes.
  * If you blindly throw nested folders or conflicting variants into the directory without separating them, **no fixer tool in the world will ever be able to repair them** due to user negligence.
* **Read the Local README Files**: If you find a `README.txt`, `README.md`, or any text instruction file inside the extracted mod folder, **please take a moment to read it carefully.** Modders often include crucial local instructions or troubleshooting tips that were not posted on their GameBanana page. Please do not skip reading these files.

---

## Disclaimer

This project is not my own original creation from scratch; I am simply maintaining and updating it of my own volition to keep the tool working for the community. 

As this is my first time maintaining a project like this and I am working on it solo, there may still be bugs or edge cases where some mods cannot be fully repaired. I apologize for any inconvenience, and I highly appreciate your understanding and support!
