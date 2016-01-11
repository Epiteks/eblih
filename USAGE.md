## Usage

* General
````
Usage: eblih [options] command ...

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
    group                       -- Group management
    sshkey                      -- SSH-KEYS management
    config                      -- Modify blihtek configuration
    NO_COMMAND                  -- GUI Mode

Environment variables :
    EPITECH_LOGIN               -- Your login
    EPITECH_TOKEN               -- Your UNIX password in SHA512
    EPITECH_FOLDER              -- Your work folder
````

* Repository mode
````
Commands :
[TODO]new repo                    -- Create and clone the repository repo
    create repo                 -- Create the repository repo
[TODO]clone repo                  -- Clone the repository repo
[TODO]clone user repo             -- Clone the repository repo of user
[TODO]link repo                   -- Link the current directory with repo
[TODO]link user repo              -- Link the current directory with repo
    info repo                   -- Get the repository metadata
    list                        -- List the repositories created
    list text                   -- List the repositories created containing text
[TODO]backup repo                 -- Backup the repository repo
[TODO]backup user repo            -- Backup the repository repo of user
[TODO]backupall                   -- Backup all your repositories
    getacl repo                 -- Get the acls set for the repository
    setacl repo user acl        -- Set (or remove) an acl for user on repo
[TODO]setgacl repo group acl        -- Set (or remove) an acl for users in group on repo
                                ACL format:
                                r for read
                                w for write
                                a for admin
````

* [TODO]Group mode
````
Commands :
[TODO]create name                 -- Create the group name
[TODO]create name users           -- Create the group name with users (one or more)
[TODO]add name users              -- Add users (one or more) to the group name
[TODO]remove name                 -- Remove the group name
[TODO]remove name users           -- Remove users (one or more) from the group name
[TODO]list                        -- List the groups
[TODO]list name                   -- List the users in the group name
````

* SSHKey mode
````
Commands :
    upload file                 -- Upload a new ssh-key
    list                        -- List the ssh-keys
    delete sshkey               -- Delete the sshkey with comment <sshkey>
````

* [TODO]Config mode
````
Commands :
[TODO]crypt                       -- Crypt your password in SHA512 for EPITECH_TOKEN
[TODO]disp                        -- Display all the values of blihtek variables
[TODO]disp variable               -- Display the value of blihtek variable
                                Variables:
                                login    for EPITECH_LOGIN
                                token  for EPITECH_TOKEN
                                folder for EPITECH_FOLDER
````
