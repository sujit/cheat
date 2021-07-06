# cheat

Installation
---------------------------
1. Download "cheat" binary as per your OS from the [official repo](https://github.com/cheat/cheat/releases)
2. Run the following commands (linux) to install:
    ```bash
    $wget https://github.com/cheat/cheat/releases/download/4.2.2/cheat-linux-amd64.gz
    $gzip -dk cheat-linux-amd64.gz
    $sudo mv cheat-linux-amd64/cheat /usr/local/bin/
    $chmod +x /usr/local/bin/cheat
    $cheat # Choose 'Yes` to generate the default config YML
    ```
3. Create a new folder named "awake"
    ```bash
    mkdir -p /home/<username>/.config/cheat/cheatsheets/awake
    ```
4. Open the "cheat" tool's config file
    ```bash
    $vim /home/<username>/.config/cheat/conf.yml
    ```
5. Add a new and custom entry (Awake's cheat files):
    ```yaml
      # New custom entry
      # Awake cheats: https://github.com/sujit/cheat/tree/main/cheats/tool.cheat
      - name: awake
        path: /home/<username>/.config/cheat/cheatsheets/awake
        tags: [ awake ]
        readonly: false
    ```
6. That's it!

Usage
---------------------------

* Show all tags in the local DB
  ```bash
  cheat -T  # Show all tags
  ```

* Show all cheats (regardless of tags)
  ```bash
  cheat -l
  ```

* Search tags
  ```
  cheat -l -t <tagname>         # Custom tag name goes here
  cheat -l -t awake             # Show all (global catch-all) awake tagged functions
  cheat -l -t ava               # AVA Functions
  cheat -l -t stats             # EAQL functions returning statistical data
  cheat -l -t visualization     # Visualization
  cheat -l []-t bruteForce        # Bruteforce EAQL functions
  cheat -l -t [anomaly|rad]     # Threat hunting anomaly functions (anomaly,rad,hunting)
  cheat -l -t differentActivity # Chaining EAQL functions
  cheat -l -t tagging           # Device tagging EAQL functions
  cheat -l -t builtins          # Show builtins e.g. any, all
  ```

* View a cheat
  ```bash
  cheat awake_<TAB>               # Show all cheats with `awake_` as prefix
  cheat awake_bruteForce          # bruteForce EAQL function usage
  cheat awake_differentActivity   # chainDifferent EAQL function usage
  cheat awake_exceptionBase       # Awake exception template
  cheat awake_toCsv.uniqueBy      # Example usage for toCsv.uniqueBy EAQL function
  cheat awake_any                 # any built-in function usage example
  cheat brute<TAB>                # Fuzzy search that auto-fills "awake_bruteForce" 💖
  cheat -cs "toCsv"               # Seach inside all cheats where "toCsv" literal string matches ✨
  cheat -crs "toCsv\.uni"         # Search inside all cheats for the given RegEx pattern 🔥
  ```

* Edit/modify a cheat :warning:
  ```bash
  cheat -e awake_bruteForce
  ```
  > `editor` macro needs to be set in `~/.config/cheat/conf.yml` e.g `editor: vim`



# Supported OS

* Linux
* Mac OS X
* Windows


![example](./screenshots/test.svg)
