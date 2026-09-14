# 构建准备

## 基准版本

上游锁定位于 ../upstream.lock.json。android-9.0.0_r61 的 manifest 提交已通过 git ls-remote 核对；完整源码同步、依赖解析和构建尚未执行。该版本是候选基准，未证明与 X08C vendor 完全兼容。

使用 x86_64 Linux 构建主机与 SSD。首次源码及输出建议规划 300–500 GB 可用空间，这是容量预算，不是本项目实测。Apple Silicon 上模拟 x86 构建未经验证。

## 获取上游

安装官方 repo 工具及 Android 9 对应依赖后，在独立空目录执行：

```bash
mkdir -p aosp
cd aosp
repo init -u https://android.googlesource.com/platform/manifest -b android-9.0.0_r61
repo sync -c -j4
git -C .repo/manifests rev-parse HEAD
```

最后一条应与 upstream.lock.json 中 manifest_commit 一致。同步完成后将 repo manifest -r 导出的解析结果保存在私有构建记录中。下载量很大，repo sync 不应在空间不足的系统盘运行。

将本仓库 device/xiaomi/x08c 目录复制到 AOSP 源码树中的同一路径。保留独立仓库作为修改真值，每次构建记录其 Git 提交。

## 尚未完成的构建门槛

- 验证原厂 boot ramdisk、system-as-root、fstab 与候选系统布局相容。
- 接入所需 init 配置、1280×800 横屏 overlay 和 SELinux 策略。
- 完成 vendor VINTF 与 Framework compatibility matrix 校验。
- 按依赖保留必要 MTK Framework 扩展；不能仅凭文件名前缀删除。
- 集成 WebView 和 01OS 面板安装方式、Home 默认值及启动服务。
- 核实 BoardConfig 的其余参数；Binder 设置已由真机内核确认，其他配置仍需要实际构建验证。

这些门槛完成后，预期构建入口为：

```bash
source build/envsetup.sh
lunch x08c-userdebug
m systemimage
```

上述命令是待验证的构建入口，不承诺当前骨架可直接成功构建。输出须通过格式、容量、VINTF、启动类路径和文件清单检查后才可进入设备实验。配置中的 BOARD_AVB_ENABLE=false 是当前解锁实验设置，不是生产安全策略。

参考：
- https://source.android.com/docs/setup/create/new-device
- https://source.android.com/docs/setup/start/requirements
- https://source.android.com/docs/core/tests/vts/gsi
