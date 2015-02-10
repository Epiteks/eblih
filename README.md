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
    config                      -- Modify blihtek configuration

Environment variables :
    EPITECH_LOGIN               -- Your login
    EPITECH_TOKEN               -- Your UNIX password in SHA512
    EPITECH_FOLDER              -- Your work folder
````

* Repository mode
````
Commands :
    new repo                    -- Create and clone the repository repo
    create repo                 -- Create the repository repo
    clone repo                  -- Clone the repository repo
    clone user repo             -- Clone the repository repo of user
    link repo                   -- Link the current directory with repo
    link user repo              -- Link the current directory with repo
    info repo                   -- Get the repository metadata
    list                        -- List the repositories created
    list text                   -- List the repositories created containing text
    backup repo                 -- Backup the repository repo of user
    backup user repo            -- Backup the repository repo
    backupall                   -- Backup all your repositories
    getacl repo                 -- Get the acls set for the repository
    setacl repo user acl        -- Set (or remove) an acl for "user" on "repo"
                                ACL format:
                                r for read
                                w for write
                                a for admin
````

* SSHKey mode
````
Commands :
    upload file                 -- Upload a new ssh-key
    list                        -- List the ssh-keys
    delete sshkey               -- Delete the sshkey with comment <sshkey>
````

* Config mode
````
Commands :
    crypt                       -- Crypt your password in SHA512 for EPITECH_TOKEN
    disp                        -- Display all the values of blihtek variables
    disp variable               -- Display the value of blihtek variable
                                Variables:
                                login  for EPITECH_LOGIN
                                token  for EPITECH_TOKEN
                                folder for EPITECH_FOLDER
````

## Changelogs

* v0.8
    * Add "repository backup" mode
        * "repository backup repo" of "repository backup user repo" to save a (sharred) repository
        * "repository backupall" to save all your repositories
    * Catch "CTRL+C" when a command is too long or if you want to stop a command

* v0.7
    * Add "search mode" for "repository list"
        * You can use "repository list text" to display all the repositories containing text

* v0.6
    * Add "config" mode
        * Add "config crypt" to crypt your password in SHA512
        * Add "config disp" to display values of all the blihtek variables
        * Add "config disp variable" to display the value of blihtek variable

* v0.5
    * Add "repository new" to create, set the ACL ans clone a repository

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

* Add explicit error output for subprocess.check_output ("repository clone / link")
