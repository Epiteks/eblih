## Changelogs

* v1.0
    * Add "group" mode
        * You can now use groups to set easily ACLs for your repositories
        * Availables actions are "create / add / remove / list"
        * You can check [here](https://github.com/hug33k/blihtek/blob/master/USAGE.md) to see all the commands
    * Add redirection modes for password (By [pouleta](https://github.com/pouleta))
        * You can now send your password to blihtek with two other methods
            ````
            blihtek command <<< "password"
            echo "password" | blihtek command
            ````

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
