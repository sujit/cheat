# Table of Contents
1. [Cheat](#cheat)
   * [Installation](#cheatinstall)
   * [Usage](#cheatusage)
2. [Navi](#navi)
   * [Installation](#naviinstall)
   * [Usage](#naviusage)
3. [Search tags](#tags)

:dart: cheat <a name="cheat"></a>
========================

*Installation* <a name="cheatinstall"></a>
---------------------------

1. Download the "cheat" binary:
    * [linux](https://github.com/cheat/cheat/releases/download/4.2.2/cheat-linux-amd64.gz)
    * [mac](https://github.com/cheat/cheat/releases/download/4.2.2/cheat-darwin-amd64.gz)
    * [windows](https://github.com/cheat/cheat/releases/download/4.2.2/cheat-windows-amd64.exe.zip)
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
6. Copy all cheats flat files from this [absolute URL path](https://github.com/sujit/cheat/tree/main/cheats/tool.cheat)
7. Execute `cheat awake_<TAB>` to show all Awake cheats! 😻

*Usage* <a name="cheatusage"></a>
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
  ```bash
  cheat -l -t <tagname>           # Custom tag name goes here
  cheat -l -t awake               # Show all (global catch-all) awake tagged functions
  cheat -l -t ava                 # AVA Functions
  cheat -l -t stats               # EAQL functions returning statistical data
  cheat -l -t visualization       # Visualization
  cheat -l -t bruteForce          # Bruteforce EAQL functions
  cheat -l -t [anomaly|rad]       # Threat hunting anomaly functions (anomaly,rad,hunting)
  cheat -l -t differentActivity   # Chaining EAQL functions
  cheat -l -t tagging             # Device tagging EAQL functions
  cheat -l -t builtins            # Show builtins e.g. any, all
  ```

* View a cheat
  ```bash
  cheat awake_<TAB>               # Show all cheats with `awake_` as prefix
  cheat awake_bruteForce          # bruteForce EAQL function usage
  cheat awake_differentActivity   # chainDifferent EAQL function usage
  cheat awake_exceptionBase       # Awake exception template
  cheat awake_toCsv.uniqueBy      # Example usage for toCsv.uniqueBy EAQL function
  cheat awake_any                 # any built-in function usage example
  cheat -cs "toCsv"               # Seach inside all cheats where "toCsv" literal string matches ✨
  cheat -crs "toCsv\.uni"         # Search inside all cheats for the given RegEx pattern 🔥
  ```

* Fuzzy search
  ```bash
  cheat brute<TAB>                # Fuzzy search that auto-fills "awake_bruteForce" 💖
  ```

* Edit/modify a cheat :warning:
  ```bash
  cheat -e awake_bruteForce
  ```
  > :bangbang: **NOTE:**
  > `editor` macro needs to be set in `~/.config/cheat/conf.yml` e.g `editor: vim`


:dart: navi <a name="navi"></a>
========================

*Installation* <a name="naviinstall"></a>
------------------------

1. Download the binaries:
    * fzf
        * [linux](https://github.com/junegunn/fzf/releases/download/0.27.2/fzf-0.27.2-linux_amd64.tar.gz)
        * [mac](https://github.com/junegunn/fzf/releases/download/0.27.2/fzf-0.27.2-darwin_amd64.zip)
        * [windows](https://github.com/junegunn/fzf/releases/download/0.27.2/fzf-0.27.2-windows_amd64.zip)
    * navi
        * [linux](https://github.com/denisidoro/navi/releases/download/v2.16.0/navi-v2.16.0-x86_64-unknown-linux-musl.tar.gz)
        * [mac](https://github.com/denisidoro/navi/releases/download/v2.16.0/navi-v2.16.0-x86_64-apple-darwin.tar.gz)
        * [windows](https://github.com/denisidoro/navi/releases/download/v2.16.0/navi-v2.16.0-x86_64-pc-windows-gnu.zip)

    > :bangbang: **NOTE:** <br/>
    > `navi` won't work without `fzf` being installed.
2. Run the following commands (linux) to install:
    ```bash
    $wget https://github.com/junegunn/fzf/releases/download/0.27.2/fzf-0.27.2-linux_amd64.tar.gz
    $tar -zxvf fzf-0.27.2-linux_amd64.tar.gz
    $tar -zxvf https://github.com/denisidoro/navi/releases/download/v2.16.0/navi-v2.16.0-x86_64-unknown-linux-musl.tar.gz
    $sudo mv fzf-0.27.2-linux_amd64/fzf /usr/local/bin/
    $sudo mv navi-v2.16.0-x86_64-unknown-linux-musl/navi /usr/local/bin/
    $chmod +x /usr/local/bin/fzf /usr/local/bin/navi
    $navi
    ```
3. Copy all navi-related cheats from this [absolute URL path](https://github.com/sujit/cheat/tree/main/cheats/tool.navi) to the right folder. To know your existing cheats path, use the following command `navi info cheats-path`. In my case it prints something like:
   ```
   "/Users/sujit/Library/Application Support/navi/cheats"
   ```

   > :bangbang: **NOTE:** <br/>
   > You need to create a folder `awake__cheats` inside the above printed directory path, where the Awake related cheat files should be copied to.

*Usage* <a name="naviusage"></a>
------------------------

* Execute navi (print mode, in-stead of executing commands)
   ```bash
   navi --print
   ```
* Search for any [tag](#tags) listed in the table:
* Pressing `<Enter>` would print the cheat in STDOUT stream for the selected tag. 
  > :bangbang: **NOTE:** <br/>
  > Since fuzzy search is possible using navi tool's `interactive mode`, you can also search for tags, part of descriptions, or even the body of any function definitions as well.

:dart: Search Tags <a name="tags"></a>
========================
In general, even though we can search the body part of cheats in their own ways via `cheat` or `navi` tool in-built options, but using tags would help us find things even much faster. It is highly recommended to use the right set of tags while searching or adding your own cheats, as it helps to find things quickly.

| Tag               | Description                                               |
| :---              |    :----                                                  |
| awake             |  All Awake functions (superset of everything)             |
| ava               |  AVA functions                                            |
| exception         |  Exception framework preambles                            |
| bruteforce        |  Bruteforce detection                                     |
| differentactivity |  Chaining different activities                            |
| stats             |  Statistical data & aggregations                          |
| visualization     |  Data visualization functions                             |
| eaql              |  All EAQL functions                                       |
| builtins          |  Built-in functions (any, all)                            |
| tagging           |  Device tagging functions                                 |
| csv               |  CSV data format view and export                          |
| export            |  Data format view and export                              |
| rad               |  Device characteristics functions                         |
| anomaly           |  Anomaly detection functions                              |
| hunting           |  Generic hunting functions                                |

> :bangbang: **NOTE:** <br/>
> When you would want to introduce any new tags, along with the new sets of function definitions into any of these tools cheat database, please update the **[Search tags](#tags)** table without fail. This would not only help you but others also.
