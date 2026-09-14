# 01 Pod OS

面向智能家庭面板的 Android 平台适配项目。首个实验设备是 Redmi 小爱触屏音箱 8（X08C）。

**状态：早期 bring-up，尚无成功构建或启动的 AOSP ROM。请勿将本仓库视为可直接刷入的固件。**

目标是在保留原厂 kernel、vendor/HAL、显示、触摸和 Wi-Fi 支持的基础上，以精简 AOSP Framework 运行 01OS 网页面板。

## 当前内容

- Android 9 / API 28 的 X08C device tree 骨架。
- 32 位 ARM 用户空间、64 位 Binder 接口配置。
- 上游 AOSP 基准版本锁定与构建准备说明。
- 分层适配、验证与恢复记录模板。

现有真机实验基于原厂 2.10.61 测试固件，已移除 B 槽中的小米桌面和激活 APK，并验证三次启动进入 01OS 面板。用户确认页面显示与触摸正常。这些结果**不代表本仓库的 AOSP Framework 已构建或启动成功**。

## 源码边界

本仓库保存自主编写的平台配置和文档，不镜像整个 AOSP。完整 Android 源码由 Google 上游提供，按 [构建说明](docs/build.md) 单独下载。

不包含小米固件、kernel/vendor 二进制、MTK JAR、从固件提取的 SELinux/VINTF 文件、设备备份、密钥、家庭数据或原始日志。硬件依赖须由设备持有人自行合法取得，且保存在不被 Git 跟踪的目录中。

01OS 网页和 Android 面板应用暂留在原产品仓库，不属于本次平台源码分离；本项目尚未将面板 APK 集成为系统预装应用。

## 开始

阅读 [构建准备](docs/build.md)、[适配状态](docs/status.md) 和 [恢复边界](docs/recovery.md)。

本仓库的新代码与文档采用 MIT 许可；外部 AOSP 和厂商组件保留各自许可。项目与 Xiaomi、MediaTek 和 Google 无隶属关系。
