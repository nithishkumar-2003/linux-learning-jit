SUMMARY = "Add jasmin user with password"
DESCRIPTION = "Creates user jasmin and sets encrypted password"
LICENSE = "CLOSED"

inherit extrausers

# Replace with your own secure hash
PASSWD_JASMIN = "raspberry"

EXTRA_USERS_PARAMS = "\
    useradd -p '${PASSWD_JASMIN}' raspberry; \
    usermod -a -G sudo raspberry; \
"
