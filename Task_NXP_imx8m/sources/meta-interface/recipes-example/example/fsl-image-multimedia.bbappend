SUMMARY = "bitbake-layers recipe"
DESCRIPTION = "Recipe created by bitbake-layers"
LICENSE = "CLOSED"

inherit core-image

python do_display_banner() {
    bb.plain("***********************************************");
    bb.plain("*                                             *");
    bb.plain("*        Custom Image Starts Building         *");
    bb.plain("*                                             *");
    bb.plain("*     Enjoy Exploring the Custom Features     *");
    bb.plain("*                                             *");
    bb.plain("***********************************************");
}

do_display_banner[nostamp] = "1"

addtask display_banner before do_build
