# OpenStarbound Server Manager
[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/assasin34/OpenStarbound-Server-Manager)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/github/license/assasin34/OpenStarbound-Server-Manager)
![Platform](https://img.shields.io/badge/Platform-Windows-blue)

A graphical server manager for OpenStarbound, built with Python and PySide6. This tool provides an easy-to-use interface for managing your OpenStarbound dedicated server, monitoring its performance, and viewing connected players.

## Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Configuration](#configuration)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Acknowledgements](#acknowledgements)
- [License](#license)

## Features

*   **Server Control:** Easily Start, Stop, and Restart your OpenStarbound server with dedicated buttons.
*   **Live Console:** View the raw server console output in real-time.
*   **Player Monitoring:** See a list of currently connected players and a live player count.
*   **Resource Tracking:** Monitor CPU and RAM usage for both the server process and your total system.
*   **Server Status:** Get at-a-glance information on the server's status (Offline, Starting, Online, etc.), uptime, and public IP address.
*   **Ngrok Integration:** Optional, one-click `ngrok` support to easily open your server to the public internet without manual port forwarding.
*   **Configuration UI:** A simple settings dialog to configure paths to your server and `ngrok` executables.

## Getting Started

### Prerequisites
*   Python 3.x
*   A local copy of the [OpenStarbound](https://github.com/OpenStarbound/OpenStarbound) dedicated server.

### Installation

1.  Clone the repository to your local machine:
    ```sh
    git clone https://github.com/assasin34/OpenStarbound-Server-Manager.git
    cd OpenStarbound-Server-Manager
    ```

2.  Install the required Python packages:
    ```sh
    pip install PySide6 psutil
    ```

### Configuration

1.  The first time you run the application, it will create a `settings.json` file in the same directory with default values.
2.  Open the application and click the **Settings** button in the top-right corner.
3.  In the Settings window, you must provide the correct paths for:
    *   **Server Executable:** The full path to your `starbound_server.exe`.
    *   **Server Executable Folder:** The directory where the server executable is located.
4.  (Optional) If you want to use `ngrok` for easy public access:
    *   Check the **Use Ngrok** box.
    *   Provide the path to your `ngrok.exe` and its containing folder.
5.  Click **Save** to apply your changes.

Alternatively, you can manually edit the `settings.json` file:

```json
{
    "server_executable": "C:/path/to/your/starbound_server.exe",
    "server_directory": "C:/path/to/your/server_folder",
    "ngrok_executable": "C:/path/to/your/ngrok.exe",
    "ngrok_directory": "C:/path/to/your/ngrok_folder",
    "universe_path": "...",
    "assets_path": "...",
    "use_ngrok": true
}
```

## Usage

Run the main application file from the project's root directory:

```sh
python main.py
```

*   **Server Controls:** Use the `Start`, `Stop`, and `Restart` buttons to manage the server. Buttons will enable or disable based on the server's current state.
*   **Players and Console:** The main window displays the list of connected players on the left and the live server console on the right.
*   **Server Info:** The bottom-left panel shows the server's status, uptime, public IP address (either your public IP or an `ngrok` URL), and the current player count.
*   **Resources Usage:** The bottom-right panel displays real-time CPU and RAM usage percentages.

## Roadmap

### Completed

- [x] Server management
- [x] Live console
- [x] Player monitoring
- [x] Resource monitoring
- [x] Ngrok integration

### Planned

- [ ] Crash Handling
- [ ] Server Config Editor
- [ ] Automatic backups
- [ ] Plugin/Mod manager
- [ ] Multiple server profiles

## Acknowledgements

- [OpenStarbound](https://github.com/OpenStarbound/OpenStarbound) – The open-source reimplementation and enhancement of the Starbound engine.
- [Starbound Server GUI (PenGUIn)](https://community.playstarbound.com/threads/penguin-starbound-server-gui.118075/) – Inspiration for the overall concept and several server management features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.