# blihtek
BLIH simplified for Epitech

## Thanks
Thanks to "IONIS Bocal", korovi_o and [Shakarang](https://github.com/Shakarang)

## Before using
You can set the variables in commandline or in your shell's config file
````shell
#For BASH
export EPITECH_LOGIN="login_x"
export EPITECH_TOKEN="UNIX PWD in SHA512"
export EPITECH_FOLDER="/your/work/folder"
````
````fish
#For FISH
set -U EPITECH_LOGIN "login_x"
set -U EPITECH_TOKEN "UNIX PWD in SHA512"
set -U EPITECH_FOLDER "/your/work/folder"
````
And copy blihtek to your /usr/bin directory
````
sudo cp blihtek /usr/bin/
````
## Usage

* General
````
Usage: ./blihtek [options] command ...

Global Options :
    -u user | --user=user       -- Run as user
    -f folder | --folder=folder -- Execute in specific folder
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
    EPITECH_FOLDER              -- Your work folder
````

* Repository mode
````
Commands :
    create repo                 -- Create the repository repo
    clone repo                  -- Clone the repository repo
    clone user repo             -- Clone the repository repo of user
    link repo                   -- Link the current directory with repo
    link user repo              -- Link the current directory with repo
    info repo                   -- Get the repository metadata
    getacl repo                 -- Get the acls set for the repository
    list                        -- List the repositories created
    setacl repo user [acl]      -- Set (or remove) an acl for "user" on "repo"
                                ACL format:
                                r for read
                                w for write
                                a for admin
````

* SSHKey mode
````
Commands :
    upload [file]           -- Upload a new ssh-key
    list                    -- List the ssh-keys
    delete <sshkey>         -- Delete the sshkey with comment <sshkey>
````

## Changelogs

* v0.4
    * Add "repository link" to link your current directory with a repository (Yours or someone else's, if you have the ACL)

* v0.3
    * Add "-f folder | --folder=folder" option
        * This option can be used when you clone a repository
    * Add the variable "EPITECH_FOLDER"
        * Same as "-f" option
    * Add "repository clone" to clone an Epitech repository (Yours or someone else's, if you have the ACL)
    * Add color output for server requests
    * Add a sort for the "repository list"

* v0.2
    * Add "-V | --version" in usage
    * "Version" option shows you the BLIH version and the blihtek version
    * "Version" option shows you a message if there is an update available

* v0.1
    * Add colors to output
    * Add "-c | --nocolor" option
    * Set automaticaly the ACL "read" to ramassage-tek when you create a repository

## TODO

* WIP : Integration of [Epidepot](https://github.com/Shakarang/epidepot)
* Add explicit error output for subprocess.check_output ("repository clone / link")
* Add a "search" mode for the list of repository
