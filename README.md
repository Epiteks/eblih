# blihtek
BLIH simplified for Epitech

## Thanks
Thanks to korovi_o and [Shakarang](https://github.com/Shakarang)

## Before using
You can set the variables
````
export EPITECH_LOGIN="login_x"
export EPITECH_TOKEN="UNIX PWD in SHA512"
````
And copy blihtek to your /usr/bin directory
````
sudo cp blihtek /usr/bin/
````
## Usage
````
Usage: ./blihtek [options] command ...

Global Options :
    -u user | --user=user       -- Run as user
    -v | --verbose              -- Verbose
    -c | --nocolor              -- Remove the colors
    -b url | --baseurl=url      -- Base URL for BLIH
    -t token | --token token    -- Specify token in the cmdline
    -V | --version              -- Version

Commands :
    repository                  -- Repository management
    sshkey                      -- SSH-KEYS management
    whoami                      -- Print who you are

Environment variables :
    EPITECH_LOGIN               -- Your login
    EPITECH_TOKEN               -- Your UNIX password in SHA512
````

## Changelogs

* v0.2
    * Add -V | --version in usage
    * "Version" option shows you the BLIH version and the blihtek version
    * "Version" option shows you a message if there is an update available

* v0.1
    * Add colors to output
    * Add -c | --nocolor mode
    * Set automaticaly the ACL "read" to ramassage-tek when you create a repository

## TODO

* Integration of [Epidepot](https://github.com/Shakarang/epidepot)