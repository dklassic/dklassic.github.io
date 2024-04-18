---
title: "Autopanic Zero Tech Fixes"
date: 2022-05-10T19:07:26+08:00
draft: false
enableComments: false
showTip: false
---

**IF YOU'RE HAVING ANY TECHNICAL ISSUES WITH *AUTOPANIC ZERO*, READ THIS FIRST**

Thank you for playing my game! It’ll be a bummer if you can’t enjoy it at its best. Below, I prepared some potential fixes for problems you may encounter: 

# Steam Deck Experience

*Autopanic Zero* runs through Proton on Steam Deck instead of a native port, the reason is because Unity's native Linux port runs way worse than emulation through Proton.

*Autopanic Zero* can confidently run at 60FPS with dynamic resolution but 90FPS is much iffy due to the massive enemy count. Hence it's best to lock FPS at 60 for Steam Deck OLED players using system setting. But if for some reason you feel like 90FPS is worth pushing for at the cost of some visual fidelity, you can enable "Visual"→"Advance"→"CPU Lightweight Mode" to push for an extremely high framerate.

Currently Unity Engine has some problem locking FPS on Steam Deck OLED: in-game framerate lock might results into a weird 68FPS. If such problem occurs and there's a need to run past 60FPS, please unlock framerate in-game and rely on only system framerate lock.

Upon first launch on Steam Deck, the following settings will be applied:

- Change Destruction Simulation to "Off"
- Change Dynamic Lighting to "Off"
- Enable Dynamic Resolution：with target as 90FPS and lower bound at 0.5x
- Enable CPU Lightweight Mode
- Unlock in-game Vsync


As to why 90FPS, it's because while Steamworks allow the detection of played through Steam Deck, it lacks the ability to detect OLED model. The setting is much more aggressive by default to ensure out-of-the-box good experience.

# Please Be Sure You Have the Latest Graphics Drivers!

If you're experiencing any problems with the game, please verify that you have the latest drivers for your graphics card. Many issues can be solved by downloading the latest drivers from your card's manufacturer. You can get the latest drivers here:

- **AMD Cards**: [http://support.amd.com/en/download](http://support.amd.com/en/download)
- **NVIDIA Cards**: [http://www.nvidia.com/Download/index.aspx](http://www.nvidia.com/Download/index.aspx)
- **Intel Cards**: [https://www.intel.com/content/www/us/en/download-center/home.html](https://www.intel.com/content/www/us/en/download-center/home.html)

# Verifying the Game Files

Sometimes, issues can occur when downloading game updates. This can manifest as not being able to start the game or as weird graphical glitches happen in game. If you're experiencing anything like this, try verifying your installation through the game’s launcher to replace missing or corrupted files:

*On Steam:*
1. Right-click on *Autopanic Zero* in your Steam Library
2. Select 'Properties...', then select the 'Installed Files' tab
3. Select 'Verify Integrity of Game Files...'

You may also try uninstalling and re-installing the game completely. You may need to restart your computer for changes to take effect.

# If You're Having Issues Launching the Game, or See a Black Screen

Please try the following solutions, whichever ones are relevant to your system, in this order:

1. Windows and Proton Users: 

    Vulkan and 32-bit executables are planned. If the options are available when you see this, you should try it first: the options should presented immediately when you launch the game.

2. If you're using Steam, please try disabling your Steam Overlay:
    1. Right-click on *Autopanic Zero* in your Steam Library
    2. Select 'Properties...'
    3. Toggle 'Enable the Steam Overlay while in-game'

3. If you ran the game and it worked for you before, try backing up and then deleting your settings file in register:

    `Computer\HKEY_CURRENT_USER\Software\ChosenConcept\Autopanic Zero`

    *Note*: This is not your save progress. This will simply make the game restore its default settings.

4. Try running Steam itself in Admin mode: Exit the program if it's already running, locate the respective EXE file, right-click on it, and select "Run as Administrator..."

5. Try downloading and installing the [latest Visual C++ redistributable](https://learn.microsoft.com/en-US/cpp/windows/latest-supported-vc-redist?view=msvc-170), as there's a chance it hasn't been installed correctly.

6. Disconnect any nonessential USB or bluetooth devices plugged into your PC.

7. Windows 8 Users: If you get an error about D3DCompiler_47.dll being missing, you can download and install that from [here](https://wikidll.com/microsoft/d3dcompiler_47-dll).

8. Proton Users: Check the following links to make sure your graphics card is configured correctly:
    [https://github.com/ValveSoftware/Proton/wiki/Requirements#amdintel](https://github.com/ValveSoftware/Proton/wiki/Requirements#amdintel)

    "Arch Linux - Intel Graphics Drivers - Modesetting VS Intel"
    [https://www.youtube.com/watch?v=zEhAJMQYSws](https://www.youtube.com/watch?v=zEhAJMQYSws)

# If the Game Won't Start or Read/Write Save Data

Please try the following solutions, whichever ones are relevant to your system, in this order:

1. Certain antivirus software may cause such issues. If you see the error message "Warning: Unable to Save" or "Warning: Unable to Read Data", this is the likely cause. To resolve the issue, whitelist the game in your antivirus software, or disable it completely.

2. Ensure that you have the following folder: 

    `Documents\Saved Games\Autopanic Zero`

    And allow access to it in Windows Defender and Windows Controlled Folder Access: [https://support.microsoft.com/en-us/help/4046851/windows-10-allow-blocked-app-windows-security](https://support.microsoft.com/en-us/help/4046851/windows-10-allow-blocked-app-windows-security)

3. OneDrive and Google Drive sync can also interfere with saving. Follow Step 5 here ([https://windowsreport.com/access-is-denied-windows-10/](https://windowsreport.com/access-is-denied-windows-10/)) to disable OneDrive sync for the game's save folder.

# If You're Experiencing Hitching / Freezing / Lag / Frame Rate / Performance Issues

***Autopanic Zero*** is generally a CPU heavy game due to my enemy AI implementation. Though it may not work well on lower power devices (e.g. older U series CPU from Intel and AMD), it should scale suitably well on multicore.

There are also some ways to improve general gameplay:

- Enable framerate limit for a consistent gameplay
- Disable "Destruction Simulation" Setting in "Visual" → "Advanced"
- Disable "Dynamic Lighting" Setting in "Visual" → "Advanced"
- Enable "Dynamic Resolution" and/or "FSR2"/"DLSS" setting in "Visual" → "Advanced"

Usually lowering resolution isn't associated with easing CPU overhead, but due to the way this game is rendered, lowering resolution can drastically improve the CPU performance. If you'd like to further reduce CPU load at a cost of changing visual presentation, you can:

- Enable "CPU Lightweight Mode" setting in "Visual" → "Advanced"

If all of above doesn’t help and you believe your device is better than minimum tested device, try each of the following steps:

1. Ensure you have the latest graphics drivers.
2. Try toggling the Fullscreen and/or VSync settings in-game.
3. If you have Nvidia G-Sync or AMD FreeSync, please disable them and turn on AMD Anti-Lag if available.
4. Windows and Proton Users: If the feature is implemented in the future, try the Vulkan and 32-bit executables.
5. Close all other running programs.
6. If available, in your graphics device control panel, set "Maximum Performance Priority" and/or "Fast VSync".
7. Ensure Windows 7 compatibility mode is NOT turned on for Autopanic Zero.exe.
8. Disable any overlays, e.g. Steam, GeForce, etc.
9. Physically disconnect all secondary display devices.
10. If you have an Nvidia graphics card, follow this guide ([https://www.techadvisor.co.uk/how-to/pc-components/how-set-default-graphics-card-3612668/](https://www.techadvisor.co.uk/how-to/pc-components/how-set-default-graphics-card-3612668/))  to ensure the game is using that card, and not your onboard Intel card.
11. After that, make sure that your Windows power settings are set for High Performance while running ***Autopanic Zero***. Ensure that the monitor running the game is connected to your Nvidia graphics video card on the back of your computer.

*Note*: If you cannot find an option to select your GPU, you may have to manage it in your system BIOS. Disable Intel HD and make sure you set PCIe as the default for graphics in the BIOS, don't leave it at Auto.

# If the footage too blurry even when using high resolution setting

That’s probably due to dynamic resolution. You can manually disable it in `Visual` → `Advanced`.

Dynamic resolution will be enabled automatically if the platform supports it and your first few minutes is too janky, which is maybe a bit too aggressive but I want to ensure those who can’t hit 60FPS consistently have a smooth gameplay experience.

# If you cannot change monitor despite having multiple screen available

It’s a conscious choice to prevent monitor change while using exclusive fullscreen.

There are too many weird behavior occurring when triggering monitor change for exclusive fullscreen, so you’ll have to use borderless or windowed before switching.

# Mouse and Controller Input Issues

If you are experiencing issues with the game registering input at times, please disconnect any controllers that may be plugged in.

***Autopanic Zero*** may have issues with some wireless or bluetooth game controllers; turning off Vibration in the Settings menu may alleviate any issues.

If you experience any other issues with mouse input, such aiming not as smooth as you expect, try the following: In the System Menu, go to `Accessibility`, then change `Use Mouse Aim` to `Mouse Only`. In most cases, this should alleviate the issue.

If your controller isn’t detected by the game, try disconnecting all controllers and ensuring all controller devices are removed from the Device Manager. Then, reconnect your primary controller and try again. Keep in mind the game will always recognize all controller at all times.

You can also toggle on/off Steam Input, both of which might lead to a proper detection of controller input.

There are also some known issues around:

- DualShock 4 and DualSense controller’s Touch Button will be shown as (and actually mapped to) Share Button instead if you’re using Steam Input. It’ll be properly shown as Touch Button if you disable Steam Input though.

# Audio Issues

If you are experiencing issues with the game audio, please first make sure your audio drivers are updated:

1. Open Windows Device Manager
2. Open the Audio Inputs and Outputs list of devices
3. Right-click on your audio device and choose "Update Driver"

If sound effects are weirdly cut-off, check the in-game settings menu and try adjusting any lowered volume sliders back to maximum, and control game volume with your system’s volume settings instead.

If you're using a controller, make sure it’s disabled as a sound device. I know this might be an issue if you’re using DualShock 4 or DualSense.

# If You Unexpectedly Lose Saved Progress

If something happens and you lose progress or find your save data missing, chances are it can still be recovered. 

If your save files have disappeared or seemly corrupted for cannot load in the game properly, please try uninstalling and reinstalling the game. Otherwise, please follow these steps:

- On **Windows**, navigate to '\Documents\Saved Games\Autopanic Zero'
    1. Rename 'save.dat' to 'save.dat.old' just in case
    2. Sort by **Date modified** to locate your most recent backup save
        - For example: 'save.dat.bak1', 'save.dat.bak2'
    3. Rename that file to 'save.dat'
    4. Open the game and see if it loads properly
    5. If that doesn't work, repeat from **Step 1** with the next most recent '.sav' file

If you've checked all of your '.sav' files without success, please go to Steam and send a message in **Technical Support** forum, and I’ll do my best to help you get your progress back.

# If All Else Fails

If you don't find a solution to your issue, please send a message in Steam **Technical Support** forum or Discord **#autopaniczero-tech-support** channel to request assistance.
Please also provide the following files:

1. For Windows users, your DxDiag: [https://support.microsoft.com/en-us/help/4028644/windows-open-and-run-dxdiagexe](https://support.microsoft.com/en-us/help/4028644/windows-open-and-run-dxdiagexe)

2. Your Player.log located here:

Windows:
`Users\[Username]\AppData\LocalLow\ChosenConcept\Autopanic Zero\Player.log`
Or just input the address `%userprofile%\AppData\LocalLow\ChosenConcept\Autopanic Zero\` in File Explorer and you should reach this folder, then provide Player.log within it.

Thank you for reading. Hopefully this post helps you find a solution quickly.