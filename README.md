# BTN-Collected-Rules

由 BTN 网络统计分析和维护的 BitTorrent 恶意/疑似恶意 IP 地址集合。

![page-views](https://raw.githubusercontent.com/PBH-BTN/views-counter/refs/heads/master/svg/792975044/badge.svg)

> [!NOTE]
> 自 2024/08/21 起，大部分规则现在由 BTN 服务器直接生成更新，更新数据仅包含最近 45 天的活跃数据。当超过 45 天 IP 不活动时，将从列表中自动移除。

## 注意

此项目**不能**作为唯一反吸血手段使用，它无法代替由反吸血程序提供的本地检测能力。它也并非是 PeerBanHelper 的核心 “全量” 数据。此项目的存在一切皆依赖于连接到 BTN 网络的用户。
鼓励您使用在可能的情况下优先使用[PeerBanHelper](https://github.com/PBH-BTN/PeerBanHelper)并[连接到 BTN 网络](https://pbh-btn.github.io/pbh-docs/docs/btn/connect)，以便向本仓库贡献数据。  

## 如何使用

你可以直接在 PeerBanHelper 规则订阅页面选择性订阅这些规则（或者干脆直接订阅 combine/all.txt 大合集）。  
当然，你也可以配合路由器/网关 ACL 或防火墙规则，直接在网关处掐断这些 IP 的连接。  

如果你已经在使用 qBittorrent, BiglyBT, Deluge, BitComet 或者 Vuze/Azureus，请优先使用[PeerBanHelper](https://github.com/PBH-BTN/PeerBanHelper)，该工具不但支持本仓库的规则，且带有更多如启发式检测等高级检测手段。且在加入 BTN 的情况下，可向本仓库自动提交贡献数据。  

## 订阅链接

> [!WARNING]
> 我们正在更新 CloudFlare Pages 的订阅链接。**原 `https://bcr.pbh-btn.ghorg.ghostchu-services.top` 域名的链接将于 2027 年 2 月失效**。**请您及时更新规则域到新的域名 `https://bcr.pbh-btn.com`**。原路径继续保持不变。

以下链接默认均为 `combine/all.txt` 的链接，如果您需要分开订阅，请自行修改。

* [Github Raw (推荐，可能需要科学)](https://raw.githubusercontent.com/PBH-BTN/BTN-Collected-Rules/main/combine/all.txt)
* [CloudFlare Pages (和上面保持同步更新)](https://bcr.pbh-btn.com/combine/all.txt)
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
* `AS58461.txt` 包含 AS58461 自治域 IP 地址，原因：流量异常滥用
* `cevskxsnm-10-idc.txt` 包含某已通过直接证据确认恶意活动的 IDC 服务商的 IP 地址
* `concurrent-downloads-ips.txt` 【BTN更新】包含同时启动大量下载的 IP 地址，数量超过了正常人类可创建的合理范围
* `geoip-blacklist.txt` 【BTN更新】同步 BTN 上的 GeoIP 黑名单 IP 地址列表，通常是因为区域网络被极大量恶意流量占用且对网络正面贡献微乎其微
* `malicious-aria2.txt` 包含部分 Aria2 恶意活动常出现网络段
* `massive-download.txt` 【BTN更新】包含短时间内产生大量下载活动的 IP 地址
* `multi-dial.txt` 由人工维护的恶意 IP 地址列表
* `overdownload-ips.txt` 【BTN更新】包含存在对单一种子的下载量远超过种子本身体积的活动的 IP 地址
* `untrusted-ips.txt` 【BTN更新】同步 BTN 网络上分析确认不可信的 IP 地址

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

如果这份 IP 规则帮到了你，请考虑[在爱发电上支持我们](https://afdian.com/a/Ghost_chu)。  
所有收入将用于支付服务运行所需的开销，并激励我们的社区和开发者在反吸血的道路上继续坚持下去。

---

[[Github 仓库]](https://github.com/PBH-BTN/BTN-Collected-Rules)  
Powered by CloudFlare Pages
