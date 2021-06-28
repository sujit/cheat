# Install

* Navigate to the [official repo](https://github.com/cheat/cheat/releases) and download the binary as per your OS.
* Execute the following commands:
  ```bash
  $wget https://github.com/cheat/cheat/releases/download/4.2.2/cheat-linux-amd64.gz
  $gzip -dk cheat-linux-amd64.gz
  $sudo mv cheat-linux-amd64/cheat /usr/local/bin/
  $chmod +x /usr/local/bin/cheat
  $cheat # Now choose 'Yes` to generate the Config YML file 
  ```

# Commands

* Show all tags in the local DB
  ```bash
  cheat -T
  ```

* Show all cheats (regardless of tags)
  ```bash
  cheat -l
  ```

* Search tags

  ```
  cheat -l -t awake           # Show all (global catch-all) awake tagged functions
  cheat -l -t ava             # AVA Functions
  cheat -l -t stats           # EAQL functions returning statistical data
  cheat -l -t bruteForce      # Bruteforce EAQL functions (chainSame tag works too)
  cheat -l -t chainDifferent  # chainDifferent EAQL functions (chainDifferent tag works too)
  cheat -l -t [tag|tagging]   # EAQL functions related to device tagging
  cheat -l -t builtins        # Show builtins e.g. any, all
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
* ARM
* AMD (64-bit)
* Mac OS X
* Windows

