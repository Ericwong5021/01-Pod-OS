# GitHub Actions 构建

Actions → AOSP Android 9 system image → Run workflow。

工作流依次检查配置及容量、构建 Ubuntu 18.04 / JDK 8 工具环境、同步锁定的 Android 9 源码、继承上游 Treble 产品并编译 x08c-userdebug systemimage。成功后检查 sparse 镜像展开容量与 SHA-256；失败也上传日志。缓存仅包含 2 GiB ccache，不把整个 AOSP 放入 GitHub 缓存。

默认 ubuntu-22.04 Runner 用于验证流程能否开始。GitHub 标准 Runner 通常达不到本项目 300 GiB 空闲预算，会在容量检查明确失败，不代表编译成功。完整编译需事先注册可信、专用于本项目、具备 Docker 和充足磁盘的 x86_64 Linux Runner，标签 aosp-builder。当前工作流不会购买机器、自动注册 Runner 或删除主机缓存来挤空间。仅提供手动触发，不在外部 PR 上运行自托管任务。

工作流最多运行 350 分钟；慢速构建可能超时。Linux Runner 的运行用户须能访问 Docker。AOSP 源码及输出保存在工作目录 aosp，缓存位于 .ccache；自托管环境的这些目录需要按自身存储政策维护。

当前产品继承 Android 9 Treble 通用系统配置，补齐了 ARM ABI、VNDK、通用 init/SELinux 与系统基础包的上游继承。它仍包含通用产品组件，尚未实现最终极简系统，也未集成专有 MTK 扩展和 01OS 面板。厂商 fstab 和 HAL 保留在设备原厂 boot/vendor 中，未伪造替代配置。

成功的 CI 只证明编译出系统候选。没有原厂 vendor 配套检查和真机启动证据，不声明 VINTF 通过，也不自动刷设备。镜像产物明确标为 unvalidated，禁止当作已验证发布固件使用。
