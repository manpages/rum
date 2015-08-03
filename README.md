# rum
Prototype implementation for personal security system

## Build
The easiest way to build the project is to install Nix package manager
and then execute nix-shell.sh, which in turn will install all the deps.

You will now be able to simply execute sqlInit.sh to initialize database
schema (in ``rum.db`` file) and then python ./prototype.py to run the
server.

## Documentation
For now we don't generate any automated docs, everything is contained
in commentaries in code. Follow the white rabbit.
