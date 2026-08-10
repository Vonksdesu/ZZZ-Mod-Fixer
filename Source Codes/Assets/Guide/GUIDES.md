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
