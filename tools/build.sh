set -eo pipefail
cd /workspace
mkdir -p "$HOME" artifacts .ccache
git config --global user.name "01 Pod OS builder"
git config --global user.email "builder@users.noreply.github.com"
tag=$(python3 -c 'import json; print(json.load(open("upstream.lock.json"))["tag"])')
expected=$(python3 -c 'import json; print(json.load(open("upstream.lock.json"))["manifest_commit"])')
cd aosp
repo init -u https://android.googlesource.com/platform/manifest -b "$tag" --depth=1
test "$(git -C .repo/manifests rev-parse HEAD)" = "$expected"
repo sync -c -j4 --fail-fast --no-clone-bundle --no-tags
repo manifest -r -o /workspace/artifacts/resolved-manifest.xml
mkdir -p device/xiaomi/x08c
cp -R /workspace/device/xiaomi/x08c/. device/xiaomi/x08c/
export USE_CCACHE=1
export CCACHE_DIR=/workspace/.ccache
export CCACHE_EXEC=/usr/bin/ccache
ccache -M 2G
export BUILD_NUMBER="pod-${GITHUB_RUN_ID:-local}"
source build/envsetup.sh
lunch x08c-userdebug
m -j4 systemimage
python3 /workspace/tools/verify_image.py
ccache -s
