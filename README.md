# BTN-Collected-Rules

由 BTN 网络统计分析和维护的 BitTorrent 恶意/疑似恶意 IP 地址集合。

![page-views](https://raw.githubusercontent.com/PBH-BTN/views-counter/refs/heads/master/svg/792975044/badge.svg)

[点此查看 BTN 网络统计数据](https://grafana.ghostchu-services.top/public-dashboards/eded9089491241099c9ab3e384d33595)

> [!NOTE]
> 自 2024/08/21 起，大部分规则现在由 BTN 服务器直接生成更新，更新数据仅包含最近 45 天的活跃数据。当超过 45 天 IP 不活动时，将从列表中自动移除。

## 注意

此项目**不能**作为唯一反吸血手段使用，它无法代替由反吸血程序提供的本地检测能力。它也并非是 PeerBanHelper 的核心 “全量” 数据。此项目的存在一切皆依赖于连接到 BTN 网络的用户。**规则并不是大风吹来的**。  
鼓励您使用在可能的情况下优先使用[PeerBanHelper](https://github.com/PBH-BTN/PeerBanHelper)并[连接到 BTN 网络](https://pbh-btn.github.io/pbh-docs/docs/btn/connect)，以便向本仓库贡献数据。  

任何已在反作弊辅助脚本、工具、程序中使用本项目提供的数据的朋友，请您考虑[实现 BitTorrent Threat Network 标准规范](https://github.com/PBH-BTN/BTN-Spec)，以便向网络提交数据。

## 如何使用

你可以直接在 PeerBanHelper 规则订阅页面选择性订阅这些规则（或者干脆直接订阅 combine/all.txt 大合集）。  
当然，你也可以配合路由器/网关 ACL 或防火墙规则，直接在网关处掐断这些 IP 的连接。  

如果你已经在使用 qBittorrent, BiglyBT, Deluge, BitComet 或者 Vuze/Azureus，请优先使用[PeerBanHelper](https://github.com/PBH-BTN/PeerBanHelper)，该工具不但支持本仓库的规则，且带有更多如启发式检测等高级检测手段。且在加入 BTN 的情况下，可向本仓库自动提交贡献数据。  

## 订阅链接

以下链接默认均为 `combine/all.txt` 的链接，如果您需要分开订阅，请自行修改。

* [Github Raw (推荐，可能需要科学)](https://raw.githubusercontent.com/PBH-BTN/BTN-Collected-Rules/main/combine/all.txt)
* [CloudFlare Pages (和上面保持同步更新)](https://bcr.pbh-btn.ghorg.ghostchu-services.top/combine/all.txt)
* [jsdelivr (部分地区可能有污染，更新可能有数日延迟)](https://fastly.jsdelivr.net/gh/PBH-BTN/BTN-Collected-Rules@master/combine/all.txt)

## 使用指南

* qBittorrent 通过 [PeerBanHelper 内置集成](https://pbh-btn.github.io/pbh-docs/docs/downloader/qBittorrent)提供高级支持 
* qBittorrent Enhanced Edition 通过 [PeerBanHelper 内置集成](https://pbh-btn.github.io/pbh-docs/docs/downloader/qBittorrentEE)提供高级支持和 qbEE 的 ShadowBan 支持
* BiglyBT/Vuze/Azureus 通过 [PeerBanHelper 及其适配器插件](https://pbh-btn.github.io/pbh-docs/docs/downloader/BiglyBT)提供插件级高级支持
* Deluge 通过 [PeerBanHelper 及其适配器插件]([https://github.com/PBH-BTN/PeerBanHelper](https://pbh-btn.github.io/pbh-docs/docs/downloader/Deluge))提供插件支持（目前暂无百科页面，参见[这里](https://github.com/PBH-BTN/PBH-Adapter-Deluge)安装）
* BitComet 通过 [PeerBanHelper 内置集成](https://pbh-btn.github.io/pbh-docs/docs/downloader/BitComet)提供基本支持
* 其他下载器可通过 [BT_BAN](https://github.com/Oniicyan/BT_BAN) 获取支持

您编写了一个针对某个下载器的教程？欢迎打开一个 Issue 提交它！

## 鸣谢

感谢所有加入 BTN 威胁防护网络计划的所有成员。本仓库的所有 IP 数据均来自使用 PBH 并加入了 BTN 计划的成员提交的匿名数据而整理分析得出的。  
没有这些提交数据的朋友们，就没有本仓库。如果这些信息对您有所帮助，请考虑也[加入 BTN 计划](https://pbh-btn.github.io/pbh-docs/docs/btn/intro)，贡献自己的一份力量，共建 BT 反吸血防护网络。

## 更新

Sparkle 服务端每隔 1 小时就会自动更新此仓库中的对应规则文件，建议您订阅 Github Raw 或者 CloudFlare Pages 以保证时效性。

## 注意事项

本仓库的规则仅作为辅助用途，您不应将其作为主要封禁手段。  
大量零散吸血 IP 可能并不会被记录在这里，本仓库重点记录 IP 段滥用的地址。对于零散地址（通常是家宽 DHCP 动态池），请使用反吸血工具屏蔽。  
本仓库数据均为用户手动或者自动提交，且可能由自动程序处理和生成，仓库维护者不对其准确性和可靠性负责。您也不应将其用于除个人使用外的其它用途。  
本仓库并非反 PCDN 规则仓库，因此在除了 BitTorrent 环境外使用本仓库提供的规则可能效果欠佳。

## IP 规则说明

* `combine/all.txt` 包含下列所有规则
* `multi-dial.txt` 包含被观测到/用户报告的多拨下载的 IP 地址，这些 IP 段下批量部署大量客户端并进行吸血活动。此规则由人工手动更新
* `untrusted-ips.txt` 被多位 BTN 的客户端标记为问题 Peer 的 IP 地址列表
* `overdownload-ips.txt` - 由 BTN 网络统计的超量下载列表，当单一 IP 地址在 BTN 网络上下载总量超过种子大小的一定比例（目前为 250%）时才会加入此列表
* `high-risk-ips.txt` - 符合近期流行的吸血特征且因吸血而被的 IP 地址列表，此列表内的 IP 不受共识机制的最低共认人数的限制
* `tracker-high-risk-ips.txt` - 通过 Sparkle Tracker 的数据生成的 BTN 规则，借助 Tracker 的力量生成更加准确的规则数据
* `aria2c.txt` - 使用 aria2 特征刷流的 IP 地址，按主机名分类，非完整列表
* `cevskxsnm-10-idc.txt` - 分布在特定 IDC 下运行刷流业务的 IP 地址，按主机名分类，非完整列表
* `gopeeddev.txt` - 执行 Gopeed dev 刷流业务的 IP 地址，按主机名分类，非完整列表
* `poonisxq-10.txt` - 某运行电影文件分发业务公司的刷流边缘节点，由于边缘节点过多，因此本列表未按照主机名分类，非完整列表，可能频繁变动
* `tiantang-pcdn.txt` - 由 BTN 用户上报封禁列表时，整理过程发现运行甜糖 PCDN 节点的 IP 地址列表，非完整列表
* `wangxin-pcdn.txt` - 由 BTN 用户上报封禁列表时，整理过程发现运行网心云 PCDN 节点的 IP 地址列表，非完整列表
* `concurrent-downloads-ips.txt` - 同时进行大量下载任务的 IP 地址列表
* `random-identity.txt` - 使用随机 PeerID + 客户端名称进行吸血的 IP 地址列表
* `rain0.0.0.txt` - `Rain 0.0.0` 特征 IP 名单

## 被移除的规则

* ~~`gopeed dev.txt` Gopeed dev 修改版本，已经变成被人拿来吸血的形状了~~
  * 已合并到 `random-peerid.txt`
* ~~`progress-rewind.txt` 包含了被观测到为进度重置/回退的 IP 地址，这通常意味着恶意刷流（该 IP 集的内容不会增量，而是每次替换）~~
  * 已合并到 `untrusted-ips.txt`
* ~~`gitlab.i.ljyun.cn-hangzhou-monitoring.txt` 包含被观测到使用 `gitlab.i.ljyun.cn/hangzhou/monitoring (devel) (anacrolix/torrent v1.55.0)` 的 IP 地址，此特征 Peers 使用较为固定的 IP 段刷流~~ 
  * 长时间未再发现拥有此特征的 IP 地址
* ~~`ipv6-dhcp-address.txt` - 使用 DHCP 分配的 IPV6 地址（IPV6 常使用 SLAAC 而非 DHCP），根据 Sparkle 统计数据显示，大部分 DHCP 的 IPV6 地址都为吸血 Peer （由于更改 IPV6 后缀地址绕过反吸血和用作混淆）。此规则内包含**已被用户标记为吸血**的 DHCP IPV6 地址。无封禁记录的 DHCP IPV6 地址并不会被一刀切到此规则内。~~
  * 改进了识别方式并已合并到 `strange_ipv6_block.txt`
* ~~`dot1_v6_tagging.txt` 包含以 ::1 结尾的 IPV6 地址，考虑到大部分正常用户都是无状态 IPV6，这种特征极度明显的有状态 IPV6 非常可疑，且出现明显吸血行为~~
  * 已合并到 `strange_ipv6_block.txt`
* ~~`hp_torrent.txt` 包含被观测到的 `hp/torrent` 的 IP 地址~~
  * 建议使用客户端名称过滤，主流下载器已全部支持
* ~~`dt_torrent.txt` 包含被观测到的 `dt/torrent` 的 IP 地址~~
  * 建议使用客户端名称过滤，主流下载器已全部支持
* ~~`go.torrent dev 20181121.txt` 包含被观测到的百度网盘离线下载的 IP 地址~~
  * 建议使用客户端名称过滤，主流下载器已全部支持
* ~~`0xde-0xad-0xbe-0xef.txt` 包含被观测到的 `ޭ__` 乱码客户端的 IP 地址~~
  * 建议使用客户端名称过滤，主流下载器已全部支持
* ~~`123pan.txt` 包含被观测到使用 `offline-download (devel) (anacrolix/torrent unknown)` 的 IP 地址，此 UA 由 123 云盘使用~~
  * 建议使用客户端名称过滤，主流下载器已全部支持
* ~~`random-peerid.txt` 包含了全随机 PeerID IP 地址列表，这是对 BT 网络的破坏，绝对恶意的行为[(ref)](https://github.com/PBH-BTN/PeerBanHelper/issues/309)~~
  * 建议使用客户端名称过滤，主流下载器已全部支持 (PeerID 随机但客户端名称不变)
* ~~`strange_ipv6_block.txt` - 在数据筛选检查过程中发现的一些异常的 IPV6 地址~~
  * 误伤严重
## 协议

PBH-BTN 为所有 BitTorrent 用户免费提供和维护这份规则，本规则使用[知识共享 署名 4.0 国际版 (CC-BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.zh-hans) 许可。以下是本许可的重要内容摘要：

### 您可以自由地

* 共享 — 在任何媒介以任何形式复制、发行本作品 在任何用途下，甚至商业目的。
* 演绎 — 修改、转换或以本作品为基础进行创作 在任何用途下，甚至商业目的。
* 只要你遵守许可协议条款，许可人就无法收回你的这些权利。

### 惟须遵守下列条件：

* 署名 — 您必须给出[适当的署名](https://creativecommons.org/licenses/by/4.0/deed.zh-hans#ref-appropriate-credit) ，提供指向本许可协议的链接，同时[标明是否（对原始作品）作了修改](https://creativecommons.org/licenses/by/4.0/deed.zh-hans#ref-indicate-changes) 。您可以用任何合理的方式来署名，但是不得以任何方式暗示许可人为您或您的使用背书。
* 没有附加限制 — 您不得适用法律术语或者 [技术措施](https://creativecommons.org/licenses/by/4.0/deed.zh-hans#ref-technological-measures) 从而限制其他人做许可协议允许的事情。

## 捐赠

如果这份 IP 规则帮到了你，请考虑[在面包多上支持我们](https://mbd.pub/o/ghostchu)。  
所有收入将用于支付服务运行所需的开销，并激励我们的社区和开发者在反吸血的道路上继续坚持下去。

---

[[Github 仓库]](https://github.com/PBH-BTN/BTN-Collected-Rules)  
Powered by CloudFlare Pages
