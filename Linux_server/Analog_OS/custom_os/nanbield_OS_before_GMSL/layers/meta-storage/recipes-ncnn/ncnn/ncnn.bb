SUMMARY = "NCNN: High-performance neural network inference framework"
DESCRIPTION = "ncnn is a high-performance neural network inference framework optimized for mobile platforms."
HOMEPAGE = "https://github.com/Tencent/ncnn"
LICENSE = "BSD-3-Clause"
LIC_FILES_CHKSUM = "file://LICENSE.txt;md5=8c8b5b19ef89ee9cfa47e768aa904935"

SRC_URI = "git://github.com/Tencent/ncnn.git;protocol=https;branch=master;tag=20240820"

S = "${WORKDIR}/git"

inherit cmake pkgconfig

DEPENDS += "protobuf"

EXTRA_OECMAKE = "\
    -DNCNN_BUILD_EXAMPLES=OFF \
    -DNCNN_BUILD_TOOLS=OFF \
    -DNCNN_BUILD_TESTS=OFF \
    -DNCNN_PYTHON=OFF \
"

FILES_${PN} += "${libdir}/*.so*"

