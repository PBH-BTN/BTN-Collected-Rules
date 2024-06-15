# BTN-Collected-Rules

由 BTN 网络统计分析得出的可被安全的加入系统防火墙屏蔽的 IP 地址列表。

## 鸣谢

感谢所有加入 BTN 威胁防护网络计划的所有成员。本仓库的所有 IP 数据均来自使用 PBH 并加入了 BTN 计划的成员提交的匿名数据而整理分析得出的。  
如果这些信息对您有所帮助，请考虑也加入 BTN 计划，并贡献自己的一份力量。

## 更新

这些 IP 地址通过人工的方式不定期手动更新，请关注 commits 是否有新的提交，并视情况更新 IP 集。

## IP 规则说明

* `hp_torrent.txt` 包含被观测到的 `hp/torrent` 的 IP 地址
* `dt_torrent.txt` 包含被观测到的 `dt/torrent` 的 IP 地址
* `go.torrent dev 20181121.txt` 包含被观测到的百度网盘离线下载的 IP 地址
* `0xde-0xad-0xbe-0xef.txt` 包含被观测到的 `ޭ__` 乱码客户端的 IP 地址
* `123pan.txt` 包含被观测到使用 `offline-download (devel) (anacrolix/torrent unknown)` 的 IP 地址，此 UA 由 123 云盘使用
* `multi-dial.txt` 包含被观测到/用户报告的多拨下载的 IP 地址，这些 IP 段下批量部署大量客户端并进行吸血活动
  * ![multi-dial-1](./assets/101.69.63.0-64-p1.png)
  * ![multi-dial-2](./assets/101.69.63.0-64-p2.png)
  * ![multi-dial-3](./assets/101.69.63.0-64-p3.png)
