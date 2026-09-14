# 适配状态

| 阶段 | 状态 |
| --- | --- |
| 原厂镜像备份、解锁、ADB/root | 已在开发设备完成；私有备份不发布 |
| L1 产品包运行时隔离 | 已完成部分隔离；更新服务仍有残留 |
| L2 B 槽移除 Launcher/Provision | 已写入并完整逐字节读回核对 |
| 01OS 页面与触摸 | 用户已确认；WebView 66 需 globalThis 兼容脚本 |
| B 槽连续三次启动 | 已观察进入 01OS 前台并连接中枢 |
| L3 独立预装 01OS Home | 尚未完成；当前面板安装在共享 userdata 中 |
| L4 AOSP Framework 替换 | 仅配置骨架；未构建、未刷入、未验证启动 |
| DA 完整恢复演练 | 尚未完成 |
| A 分区实验后完整重新哈希 | 尚未完成 |

X08C：32 位 ARM 用户空间，VNDK 28，Treble enabled，64 位 Binder 接口。内核 CONFIG_ANDROID_BINDER_IPC_32BIT 未启用，不能因此选择使用 32 位 Binder 的镜像。

当前仍保留小米/MTK 系统组件，不是完整纯 AOSP，也不是正式可发布 ROM。音频、语音、按键、灯光和 OTA 均不在当前 M1 范围内。
