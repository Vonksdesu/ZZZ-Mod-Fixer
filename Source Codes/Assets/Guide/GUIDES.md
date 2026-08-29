# Hash Character Mods Updater

## Overview

This tool is used to **update the hash** of all character mods installed in your ZZMI folder. Hash updates are necessary to keep mods compatible after Zenless Zone Zero receives a game update.

> [!NOTE]
> This process will modify `.ini` and `.buf` files in your mod folder. Make sure to create a backup if needed.

---

## Step-by-Step Guide

### Step 1 - Select the Mods Folder

1. Look at the **Target Folder** panel at the top of the GUI
2. Click the **Browse** button
3. Navigate to the **Mods** folder in your ZZMI installation

   Example path:
   ```
   D:\ZZMI\Mods
   ```

4. Once selected, the path will appear in the Target Folder field

> [!TIP]
> You can also click the **Refresh** button to rescan the folder contents.

---

### Step 2 - Backup Settings (Optional)

In the **left panel**, there are two **optional** backup options:

| Option | Description |
|--------|-------------|
| **Create INI Backup Folder** | Creates a backup of `.ini` files before updating |
| **Create BUF Backup Folder** | Creates a backup of `.buf` files before updating |

**How to use:**

1. Check the **Create INI Backup Folder** checkbox if you want to backup INI files
2. Click the folder icon next to the path field to select the backup location
3. Repeat for **Create BUF Backup Folder** if needed

> [!WARNING]
> If no files need updating, the process will still run but no changes will be applied.

---

### Step 3 - Run the Update

1. Click the **Update Hashes** button in the left panel
2. Wait for the process to complete
3. Monitor progress in the **CLI Output** panel on the right
4. Process completion is indicated by the message `Updates applied` or `No changes applied`

> [!TIP]
> Use the **Clear CLI** button to clear the CLI output panel.

---

## Status Indicators

| Status | Meaning |
|--------|---------|
| `Active` | Tool is ready to use |
| `Running...` | Process is currently running |
| `Updates applied` | Update was successfully applied |
| `No changes applied` | No changes were needed |

---

## Troubleshooting

**Q: I see "Folder not found" message?**
> Make sure the path in the Target Folder field is correct and the folder exists.

**Q: I see "Please Select the Path for INI/BUF Backup Folder"?**
> The backup checkbox is checked but no backup location has been selected. Choose a location or uncheck the checkbox if you don't want backups.

---

# Jane Doe Remapper

## Overview

This tool is used to **remap blend indices** for Jane Doe character mods. Remapping is required to fix visual glitches such as incorrect hair or hand mesh binding after game updates.

> [!NOTE]
> This process will modify `.buf` files in your mod folder. Create a backup before proceeding.

---

## Step-by-Step Guide

### Step 1 - Select the Jane Doe Mod Folder

1. Look at the **Target Folder** panel at the top of the GUI
2. Click the **Browse** button
3. Navigate to your **Jane Doe mod folder**

   Example path:
   ```
   D:\ZZMI\Mods\JaneDoe_Mod
   ```

4. The path will appear in the Target Folder field once selected

> [!TIP]
> Click **Refresh** to rescan the folder contents.

---

### Step 2 - Backup Settings (Optional)

In the **left panel**, you can enable a backup option:

| Option | Description |
|--------|-------------|
| **Create BUF Backup Folder** | Creates a backup of `.buf` files before remapping |

**How to use:**

1. Check the **Create BUF Backup Folder** checkbox
2. Click the folder icon to select the backup location

> [!WARNING]
> If no backup location is selected while the checkbox is enabled, you will see an error message.

---

### Step 3 - Run the Remapper

1. Click the **Remap Now** button in the left panel
2. Wait for the process to complete
3. Monitor progress in the **CLI Output** panel on the right
4. Process completion is indicated by the remapping output messages

> [!TIP]
> Use the **Clear CLI** button to clear the CLI output panel.

---

## What Gets Remapped

The tool remaps two categories of blend indices:

| Category | Blend Hash | Description |
|----------|-----------|-------------|
| **Hair** | `e42171df` | Hair mesh blend indices |
| **Hand** | `d06a9206` | Hand mesh blend indices |

---

## Troubleshooting

**Q: I see "Folder not found" message?**
> Make sure the path in the Target Folder field is correct and the folder exists.

**Q: I see "Please Select the Path for BUF Backup Folder"?**
> The backup checkbox is checked but no backup location has been selected. Choose a location or uncheck the checkbox.

**Q: Some files show "Skipping" message?**
> This means the file does not match any known blend hash. It is skipped automatically.

---


# Dialyn Remapper

## Overview

This tool is used to **remap blend indices** for Dialyn character mods. Remapping ensures correct mesh binding and prevents visual issues after game updates.

> [!NOTE]
> This process will modify `.buf` files in your mod folder. Create a backup before proceeding.

---

## Step-by-Step Guide

### Step 1 - Select the Dialyn Mod Folder

1. Look at the **Target Folder** panel at the top of the GUI
2. Click the **Browse** button
3. Navigate to your **Dialyn mod folder**

   Example path:
   ```
   D:\ZZMI\Mods\Dialyn_Mod
   ```

4. The path will appear in the Target Folder field once selected

> [!TIP]
> Click **Refresh** to rescan the folder contents.

---

### Step 2 - Backup Settings (Optional)

In the **left panel**, you can enable a backup option:

| Option | Description |
|--------|-------------|
| **Create BUF Backup Folder** | Creates a backup of `.buf` files before remapping |

**How to use:**

1. Check the **Create BUF Backup Folder** checkbox
2. Click the folder icon to select the backup location

> [!WARNING]
> If no backup location is selected while the checkbox is enabled, you will see an error message.

---

### Step 3 - Run the Remapper

1. Click the **Remap Now** button in the left panel
2. Wait for the process to complete
3. Monitor progress in the **CLI Output** panel on the right
4. Process completion is indicated by the remapping output messages

> [!TIP]
> Use the **Clear CLI** button to clear the CLI output panel.

---

## What Gets Remapped

The tool remaps one category of blend indices:

| Category | Blend Hash | Description |
|----------|-----------|-------------|
| **Body** | `3d7e53cf` | Body mesh blend indices |

---

## Troubleshooting

**Q: I see "Folder not found" message?**
> Make sure the path in the Target Folder field is correct and the folder exists.

**Q: I see "Please Select the Path for BUF Backup Folder"?**
> The backup checkbox is checked but no backup location has been selected. Choose a location or uncheck the checkbox.

**Q: Some files show "Skipping" message?**
> This means the file does not match any known blend hash. It is skipped automatically.

---

# Rolling Back

## Overview

This feature allows you to **restore or permanently delete** backed-up mod files from previous tool runs. Every time a tool modifies a file, the original version is automatically saved as a hidden backup in the background — completely separate from the optional checkbox backup. If something goes wrong after an update or remap, Rolling Back lets you revert those files without having to redo anything manually.

> [!NOTE]
> Rollback backups are created **automatically and silently** every time the tool actually modifies a file. No setup is required. If a run produces no changes (e.g. all mods are already up to date), no backup session is created.

---

## Understanding the Layout

The Rolling Back section has three main areas:

| Area | Description |
|------|-------------|
| **Section Tab Bar** (top) | Switch between `Hash Character Mods Updater`, `Jane Doe Remapper`, and `Dialyn Remapper` to view their respective backup history |
| **Left Panel** | Lists all recorded backup sessions grouped by type (INI and BUF) |
| **Right Panel** | Shows the files backed up in the selected session, with individual and bulk restore/delete options |

---

## Step-by-Step Guide

### Step 1 - Select a Section Tab

1. At the top of the Rolling Back section, click one of the three tab buttons:
   - **Hash Character Mods Updater** — shows INI Backup History and BUF Backup History
   - **Jane Doe Remapper** — shows BUF Backup History only
   - **Dialyn Remapper** — shows BUF Backup History only
2. The left panel will populate with session cards for that section

> [!TIP]
> The active tab is highlighted in orange.

---

### Step 2 - Choose a Backup Session

The **left panel** is divided into two list areas:

| List | Content |
|------|---------|
| **INI Backup History** | Sessions containing backed-up `.ini` files (Hash section only) |
| **BUF Backup History** | Sessions containing backed-up `.buf` files |

Each session card shows:
- **Session Mods Sync** — label identifying the card as a rollback session
- **Date and time** — when the tool run occurred (e.g. `2026-04-15 10:12:58`)

1. Locate the session you want to inspect
2. Click the **Sync** button on the right side of the card
3. The right panel will load all the files backed up during that session

> [!NOTE]
> An orange vertical line on the left edge of a card indicates the currently active session.

---

### Step 3 - Restore or Delete Files

Once a session is loaded in the right panel, each file is displayed as a row with:
- **File name** — the name of the backed-up file (truncated with `…` if too long)
- **Restore** button — restores this single file to its original location
- **Delete** button — permanently removes this single backup file without restoring

At the top of the right panel there are also two bulk action buttons:

| Button | Action |
|--------|--------|
| **Restore All** | Restores every file in the current session to its original location |
| **Delete All** | Permanently deletes every backup file in the current session |

> [!WARNING]
> **Delete** and **Delete All** permanently remove backup files. This action cannot be undone. Use **Restore** or **Restore All** if you want the original files back first.

> [!TIP]
> You can mix single and bulk actions freely. For example, restore two files individually and then delete the rest with **Delete All**.

---

### Step 4 - After Restoring or Deleting

- When all files in a session are consumed (restored or deleted), the **right panel** returns to the default `No files detected` state
- The **session card** for that session disappears automatically from the left panel — it no longer has any backup data
- Remaining sessions are unaffected

---

## INI File Restoration

When restoring an INI file, the tool:
1. Reads the `.txt` backup from the rollback cache
2. Copies it back to the **original `.ini` path** where it was before the tool ran

> [!NOTE]
> Backup INI files are stored as `.txt` internally. When restored, they are automatically written back as `.ini` files at the original location. No manual renaming is needed.

---

## Troubleshooting

**Q: The left panel shows "No backups found (.INI)" or "No backups found (.BUF)"?**
> No backup sessions exist yet for this section and file type. Run the corresponding tool at least once on a folder that contains files needing changes.

**Q: The right panel shows "No files detected" after clicking Sync?**
> The session data may have already been cleared, or the backup files were deleted outside the application.

**Q: I restored a file but it appeared in the wrong location?**
> The file is always restored to the exact path it was at when the tool originally ran. If you moved or renamed the mod folder after the run, the restored file will go back to the old location. You will need to move it manually to the new location.

**Q: A session card won't disappear after I deleted all files?**
> Try switching to a different section tab and back. The panel refreshes automatically when the tab is changed.

**Q: Why is there no session for a run I just did?**
> If the tool ran but found no files that needed changes, no backup is created and no session appears. This is expected behaviour — only actual modifications are recorded.
