# Nitro System for FH2

[English](README.md) | 中文

为 **Forza Horizon 2**（通过 Azimuth 启动器在 PC 上运行的 Xbox One 版本）加入《速度与激情》(Fast & Furious) 风格的 **NOS**，基于 **FH2 Mod Platform** 制作。

在车库为你的车购买 **NOS 套件**，然后按住 **LB**（或任何你指定的按键）即可喷射 NOS：车辆会被强力推进，排气管喷出蓝色火焰，速度表上出现会逐渐耗尽、末端发光的 NOS 计量条，屏幕边缘泛起蓝光并有速度线飞过，NOS 轰鸣作响，镜头抖动，手柄震动。

<img width="1919" height="1079" alt="Screenshot 2026-10-22 013921" src="https://github.com/user-attachments/assets/15887438-8606-4627-bd2c-25c6a99baa3a" />
<img width="1919" height="1079" alt="Screenshot 2026-10-22 013609" src="https://github.com/user-attachments/assets/134fec85-6992-4515-b108-90b2545a1702" />
<img width="1919" height="1079" alt="Screenshot 2026-10-22 012950" src="https://github.com/user-attachments/assets/6d4a7301-aa29-4d68-ab52-2b827baea2b3" />
<img width="1919" height="1079" alt="Screenshot 2026-10-22 014318" src="https://github.com/user-attachments/assets/38a8e23d-2a2d-4786-af72-a05dc46225dc" />

> [!NOTE]
> 游戏没有简体中文，中文界面是繁体中文，因此 Mods 页面和车库中的文字会以繁体显示（用词与下文相同，例如「NOS 系統」「需要 NOS 套件」）。下文的设置名称后附有英文名称，`FnFNitro.ini` 和英文说明使用的是英文名称。

---

## 功能

- **NOS 在 LB 上，或任何你选择的按键。** 在任何已连接的手柄上按住左肩键，或将它改到其他按键、方向键或扳机（见下方 **NOS 按钮**）。没有键盘按键。
- **真正的储气罐。** 按住 NOS 按钮时 NOS 会消耗，松开后会回充。用完后会锁定，直到你松开按钮并回充约 2 秒为止。
- **加速曲线。** 推力会在短时间内逐渐增强，而不是瞬间全开。
- **紧贴路面。** 推力沿着车头的水平方向，所以车头上扬时不会把你送上天；车辆腾空时（以及落地后的片刻）不会施加推力。
- **只在驾驶时生效。** NOS 只在游戏正在模拟你的车辆、且速度表 HUD 正在运行时才有效，因此在暂停菜单、地图和加载画面中不会生效。游戏暂停时储气罐既不消耗也不回充。（车库和车聚大厅中速度表不会启用，所以也应该不会生效。）
- **NOS 套件车库升级。** NOS 是每辆拥有的车各自购买的零件：**Garage > Upgrades > Custom upgrade > Engine > NOS 套件**。阶段决定储气罐的容量和回充速度；推力在所有阶段都相同（**NOS 加速倍率**）。没有套件的车就没有 NOS，其 NOS 计量条外框也会隐藏。关闭 **需要 NOS 套件** 即可让所有车辆重新拥有 NOS，使用 **NOS 容量** 和 **NOS 回充速度** 设置。（来自 NitroSystem II。）

  | 阶段 | 储气罐 | 回充 | 价格 |
  |---|---|---|---|
  | 原厂 | 无 NOS | | 免费 |
  | NOS 第 1 阶段 | 5 秒 | 每秒 0.20 秒 | 3 000 CR |
  | NOS 第 2 阶段 | 10 秒 | 每秒 0.25 秒 | 6 000 CR |
  | NOS 第 3 阶段 | 20 秒 | 每秒 0.30 秒 | 12 000 CR |
  | NOS 第 4 阶段 | 30 秒 | 每秒 0.40 秒 | 24 000 CR |

  Drivatar（开启 **Drivatar NOS** 时）会获得与你所驾驶车辆的套件相同的储气罐和回充；你的车没有套件时，它们也没有 NOS。
- **画面效果。** NOS 喷射时视野会变宽，屏幕边缘出现脉动的蓝色暗角光晕，蓝色速度线从中央向外飞出，车速越快飞得越快。每一项都可以关闭。（来自 NitroSystem II。）
- **速度表上的 NOS 计量条。** **指针式**和**数字式**速度表都会加上一条分成四段的 NOS 计量条，随使用 NOS 逐渐减少，填充前沿有一个会发光的末端。
- **排气火焰。** 按住 NOS 时，蓝色火焰会从车辆真实的排气管位置喷出，从第一秒就开始（模组驱动游戏自带的回火效果，位置取自车辆模型本身的排气口）。
- **音效、震动和镜头抖动。** 一段先爆发、然后在储气罐耗尽前一直持续的加速音效，以及一段停止音效，两者都由游戏自带的音频从你的车上播放（把无人机飞远，声音就会随距离减弱）（内置在 DLL 中；在 `azimuth.exe` 旁新建 `FnFNitro` 文件夹并放入你自己的 `nos_boost.wav` 和 `nos_stop.wav` 即可替换；你自己的加速音效会从头开始循环）；随加速增强的手柄震动；以及喷射时的镜头抖动。每一项都有独立的设置，见下方。
- **游戏内设置。** 以下所有设置都在 **暂停 > 设置 > MODS**，这些设置以及车库中 NOS 套件的名称都会使用游戏的语言：巴西葡萄牙语、荷兰语、法语、德语、意大利语、日语、韩语、波兰语、俄语、西班牙语（西班牙和墨西哥）以及繁体中文。捷克语和匈牙利语保持英文，与游戏自身的文字一致。Mods 页面在游戏选定语言之前就已生成，所以它使用的是游戏上次运行时的语言（第一次运行时则是 Azimuth 的 Language 设置）：更改游戏语言后，要到下一次启动才会跟着改变。
- **可与车辆模组共存。** **Knight Rider**（霹雳游侠）车辆以及其他修改速度表或车辆类型的模组可以同时运行；列在 `DisabledCars` 中的车辆（默认为 Knight Rider 车辆）没有 NOS 也没有 NOS 计量条，让它们自己的模组使用该按键。安装 **ANNA Drone Mode** 时，无人机飞行期间 NOS 会关闭。其他模组也可以关闭 NOS（见下方 **给模组作者**）。

### 游戏内设置

| 设置 | 范围 | 默认 | 作用 |
|---|---|---|---|
| NOS 系统 (Nitro System) | 开 / 关 | 开 | 开启或关闭 NOS（模组名称仍为 Nitro System）。关闭时也会隐藏 NOS 计量条。 |
| NOS 按钮 (NOS Button) | LB、RB、A、B、X、Y、按下 LS、按下 RS、方向键、Back、Start、LT、RT | LB | 用来喷射 NOS 的按键。立即生效。 |
| NOS 调试信息 (NOS Debug Overlay) | 开 / 关 | 关 | 在游戏画面上绘制调试信息（见下方）。 |
| 抬头显示器主题 (HUD Theme) | 原始 / Fast & Furious | Fast & Furious | 原始为 Forza Horizon 2 的 HUD 加上黄色 NOS 计量条。Fast & Furious 则有青色 NOS 计量条、青色挡位以及青色 ABS / TCS / STM 图标。**需要重启游戏。** |
| 需要 NOS 套件 (Require NOS Kit) | 开 / 关 | 开 | 开：只有安装了 NOS 套件升级的车辆有 NOS，套件阶段决定储气罐和回充。关：所有车辆都有 NOS，使用 NOS 容量和 NOS 回充速度。立即生效。 |
| 无套件时隐藏计量条 (Hide NOS Gauge Without Kit) | 开 / 关 | 开 | 在没有套件的车辆上隐藏 NOS 计量条外框。关闭则保留一个空的外框。立即生效。 |
| NOS 加速倍率 (NOS Boost Multiplier) | 1.0x - 2.0x | 1.6x | 推力强度，适用于所有套件阶段以及 Drivatar。 |
| NOS 容量 (秒) (NOS Tank Capacity) | 5 - 60 | 20 | 满罐 NOS 的秒数。**需要 NOS 套件** 开启时忽略此设置：此时由套件阶段决定储气罐。 |
| NOS 启动时间 (秒) (NOS Buildup Time) | 0.1 - 2.0 | 0.5 | 推力增强到最大所需的时间。 |
| NOS 回充速度 (NOS Recharge Rate) | 0.0 - 1.0 | 0.2 | 未加速时每秒恢复的 NOS 秒数。**需要 NOS 套件** 开启时忽略此设置：此时由套件阶段决定回充。 |
| NOS 音量 (NOS Sound Volume) | 0 - 100 | 50 | 加速和停止音效的音量。游戏自带的音量滑块不会影响它们。从下一次加速开始生效。 |
| NOS 镜头抖动 (NOS Camera Shake) | 0 - 100 | 65 | NOS 喷射时镜头抖动的程度，适用于驾驶舱、引擎盖、保险杠和追尾视角。0 为关闭。立即生效。 |
| NOS 视野加宽 (NOS Wider FOV) | 0 - 30 | 10 | NOS 喷射时视野变宽的程度（%），适用于相同视角。0 为关闭。立即生效。 |
| NOS 蓝色暗角 (NOS Blue Vignette) | 开 / 关 | 开 | NOS 喷射时屏幕边缘出现脉动的蓝色暗角光晕。立即生效。 |
| NOS 速度线 (NOS Speed Lines) | 开 / 关 | 开 | NOS 喷射时蓝色线条向屏幕边缘飞出，速度与车速同步。立即生效。 |
| 所有车辆回火 (Backfire on All Cars) | 开 / 关 | 开 | 让所有车辆都能回火，排气火焰需要此功能（见下方）。**需要重启游戏。** |
| 比赛开始时补满 NOS (Refill NOS on Race Start) | 开 / 关 | 开 | 在比赛开始、退出比赛、更换车辆或快速旅行时补满储气罐。立即生效。 |
| 倒带时返还 NOS (Refund NOS on Rewind) | 开 / 关 | 开 | 倒带时返还从倒带点之后使用的 NOS。立即生效。 |
| NOS 手柄震动 (NOS Controller Rumble) | 开 / 关 | 开 | NOS 喷射时手柄震动。不影响游戏自带的震动。立即生效。 |
| Drivatar NOS | 开 / 关 | 关 | Drivatar 也会使用 NOS，只要可以就会用，不论速度：只有在空中、大幅侧滑或储气罐用完时才会松开（之后和你一样，要等回充到 2 秒的 NOS）。比赛开始前不会加速：你的 HUD 未显示时不会，且要从发车格出发行驶 2 秒后才会。领先你超过 100 米时会滑行，让你能够追上；落后你时则可以自由加速。每辆车都有自己的储气罐，容量和回充都是你所驾驶车辆的 NOS 套件的两倍（该车没有套件时则没有 NOS），推力和启动时间则与你相同。它们的排气管会喷火，加速音效通过游戏自带的音频从车上播放，所以你会从它所在的位置听到，在 150 米外完全消失。最近的 6 辆会以 Drivatar NOS 音量播放。立即生效。 |
| Drivatar NOS 音量 (Drivatar NOS Volume) | 0 - 100 | 25 | 从 Drivatar 车上听到的 NOS 音效音量。0 为静音。立即生效。 |

设置会保存在 `fh2-mods\FnFNitro.ini`：

```ini
[Settings]
NitroEnabled=1
NitroButton=LB
TorqueScale=1.60
Duration=20.0
BuildupTime=0.50
RechargeRate=0.20
SoundVolume=0.50
DrivatarSoundVolume=0.25
CameraShake=0.65
DebugOverlay=0
BackfireOnAllCars=1
RefillOnRaceStart=1
RefundOnRewind=1
DrivatarNitro=0
Rumble=1
HudTheme=FF
DisabledCars=3884
RequireNitrousKit=1
HudHide=1
FovBoost=0.10
VignetteEnabled=1
SpeedLinesEnabled=1

[Upgrade]
Area=1
Price1=3000
Tank1=5
Price2=6000
Tank2=10
Price3=12000
Tank3=20
Price4=24000
Tank4=30
Recharge1=0.20
Recharge2=0.25
Recharge3=0.30
Recharge4=0.40
```

你拥有的每辆车所安装的 NOS 套件，记录在游戏存档旁的 `data\titles\1A96545B\FnFNitro\player-1\FnFNitroGarage.json`（取最后写入存档的那个 `player-N`），并在你安装某个阶段时写入。它特意放在 `saves` 文件夹之外：Azimuth 会校验该文件夹内文件的哈希值，模组自己的文件可能会让存档看起来像是损坏了。备份 `1A96545B` 文件夹时，这个文件会和你的存档一起备份。

```json
{
  "version": 1,
  "cars": [
    { "garageId": 32, "carOrdinal": 2183, "stage": 3 },
    { "garageId": 45, "carOrdinal": 2183, "stage": 0 }
  ]
}
```

`garageId` 是游戏中你拥有的某一辆车的 ID，所以同一车型（`carOrdinal`）的两辆车各有自己的阶段：这里一辆是第 3 阶段，另一辆没有 NOS。`stage` 为 0（无）到 4。如果游戏把已卖出车辆的 `garageId` 分配给了另一个车型，该条目会从 0 重新开始。你可以在游戏关闭时编辑这个文件。旧版本将这些数据存放在 ini 的 `[GarageNitro]` 和 `[GarageCar]` 中，或存放在 `fh2-mods\FnFNitroGarage.json`；这个版本第一次启动时会将它们迁移到新文件中。

关于这个文件的几点说明：

- `HudTheme` 为 `FF`（Fast & Furious，默认）或 `Original`。模组会在启动时以及你更改设置时写入 HUD 文件，游戏则在下次启动时读取它们。

- `NitroButton` 选择用来喷射 NOS 的手柄按键（默认 `LB`）。未知的值会改用 `LB`。在 ini 中请填写名称：

  | # | 名称 | 按键 | # | 名称 | 按键 |
  |---|---|---|---|---|---|
  | 1 | `LB` | 左肩键 | 9 | `DPadUp` | 方向键上 |
  | 2 | `RB` | 右肩键 | 10 | `DPadDown` | 方向键下 |
  | 3 | `A` | A | 11 | `DPadLeft` | 方向键左 |
  | 4 | `B` | B | 12 | `DPadRight` | 方向键右 |
  | 5 | `X` | X | 13 | `Back` | Back / 视图 |
  | 6 | `Y` | Y | 14 | `Start` | Start / 菜单 |
  | 7 | `LS` | 按下左摇杆 | 15 | `LT` | 左扳机 |
  | 8 | `RS` | 按下右摇杆 | 16 | `RT` | 右扳机 |

  请选择游戏在驾驶时没有使用的按键，否则会同时触发两个动作。在 Mods 页面上的更改会立即生效；编辑文件则要到下次启动游戏时才生效。

  如果平台版本低于 2.8.0，Mods 页面无法显示名称，因此 **NOS 按钮** 会是一个使用上表编号的滑块，**抬头显示器主题** 则是一个滑块，1 为原始，2 为 Fast & Furious。
- `[Upgrade]` 设置 NOS 套件：四个阶段的 `Price1`..`Price4`（CR）、`Tank1`..`Tank4`（NOS 秒数，1 到 600）和 `Recharge1`..`Recharge4`（每秒恢复的 NOS 秒数，0.00 到 5.00），以及 `Area`，即该条目所在的升级区域（1 = Engine）。价格、储气罐、回充速度和名称都在启动时读取，所以更改要到下次启动游戏时才生效。（旧版本的 `Boost1`..`Boost3` 已移除：所有阶段的推力都是 NOS 加速倍率。）每辆车安装的阶段记录在 `FnFNitroGarage.json`（见上方）。
- `DisabledCars` 列出没有 NOS 也没有 NOS 计量条的车辆，以游戏的车辆 ID（`Data_Car.Id`）表示，用逗号分隔：`3884` 是 Knight Rider 车辆，它自己的模组使用 LB。留空则让所有车辆都有 NOS。每次更换车辆时，平台日志会显示 `Your car: id ...`，可以用来查出车辆的 ID。Mods 页面上没有对应的选项。
- `BackfireOnAllCars` 即 Mods 页面上的 **所有车辆回火**。开启时，模组会在启动时修改游戏数据库，让所有车辆都能回火，火焰效果需要这个功能。关闭则不改动游戏自身的回火设置：此时火焰只会出现在游戏原本就允许回火的车辆上。更改要到下次启动游戏时才生效。

### 调试信息

开启 **NOS 调试信息** 后，会在游戏窗口左上角绘制一个小面板：NOS 状态和余量、所驾驶车辆的 NOS 套件阶段和车库 ID、模组是否认为你正在驾驶、是否已找到你的车（通过游戏自身的车辆类型，或在得知类型前通过位置）、有多少 Drivatar 正在加速、排气口位置，以及火焰计数。它是覆盖在游戏上的透明窗口，和 FPS 计数器一样，所以游戏必须以**无边框或窗口**模式运行。

---

## 需求

- 运行 Forza Horizon 2 的 **Azimuth** 启动器。
- **FH2 Mod Platform 2.8.0 或更新版本**（Azimuth 文件夹中的 `DWrite.dll`）。你可能已安装的其他模组，例如 ShowFPS 或 Achievements，也使用同一个平台。NOS 套件需要 2.8.0：平台版本较旧时，套件不会加入车库，所有车辆改为都有 NOS。
- **Forza Horizon 2 Extra Options** 为可选。NOS 计量条和 HUD 贴图、蓝色火焰效果、升级图标以及数据库修改（NOS 套件，以及“所有车辆都能回火”）会放到游戏的 `mediaoverride` 文件夹；平台 2.7.3 及更新版本会让游戏自行读取该文件夹，如果安装了 Extra Options 则使用 Extra Options 的方式（请保持其 `EnableMediaOverrides` 开启）。

---

## 安装

以下路径仅为示例。请使用你自己的 Azimuth 文件夹和游戏的 `Mount` 文件夹。

### 从发布版安装（最简单）

1. 从 **Releases** 页面下载 `FnFNitro-<version>.zip` 并解压。
2. 关闭游戏。将压缩包中的 **`azimuth-windows\`** 文件夹复制到你的 Azimuth 文件夹（有 `azimuth.exe` 的那个）。询问是否合并时选择是。
3. 通过 Azimuth 启动游戏。

压缩包内含模组（`FnFNitro.dll`，HUD 文件、火焰效果、升级图标和 NOS 音效都在其中）、FH2 Mod Platform（`DWrite.dll`，负责加载模组；如果你已从其他模组获得了更新的版本，请保留你的）、许可证，以及内容与这些步骤相同的 `INSTALL.txt`。

> [!IMPORTANT]
> `FnFNitro.dll` 要放在 **`fh2-mods`**，即 FH2 Mod Platform 的文件夹。它**不是** Extra Options 模组：不要放在 Extra Options 的 `mods` 文件夹，放在那里不会被加载。如果 `fh2-mods` 还不存在，压缩包会创建它。

**从 1.2 或更旧版本升级：** 那些版本需要你将 HUD 贴图和火焰文件复制到 `Mount\mediaoverride`。现在它们都在 DLL 中，所以不需要再复制 `Mount\`。新版本第一次启动时，会删除它认得的旧副本（只删除与旧发布版逐字节相同的文件，所以你修改过的文件不会被动到），并在 `platform.log` 中写入 `Removed N old HUD/flame file(s)`。旁边残留的 `.bak` 文件是平台对原有文件的备份，你可以自行删除。

### 从源码目录安装

本仓库的 `dist\` 文件夹对应每个文件应放的位置：

| 来源 | 目标 |
|---|---|
| `dist\fh2-mods\FnFNitro.dll` | `D:\Games\FH2\azimuth-windows\fh2-mods\` |
| 平台[发布页面](https://github.com/Trinculo54/fh2-mod-platform/releases)的 `DWrite.dll` | `D:\Games\FH2\azimuth-windows\`（仅在尚未安装平台时） |

通过 Azimuth 启动游戏。打开 `fh2-mods\platform.log`，查找 `loaded FnFNitro.dll` 和 `nitrous upgrade active` 之类的行，之后还有 `Player car located` 和 `Vertical axis learned`，表示模组已找到你的车。

---

## 从源码构建

需要 **Visual Studio 2022**（MSVC C++20）和 **CMake 3.20+**。

```powershell
# 配置
cmake -B build -A x64

# 构建 Release
cmake --build build --config Release

# 打包到 dist\ 并将所有文件复制到你的 Azimuth 和游戏文件夹
powershell -ExecutionPolicy Bypass -File scripts\package.ps1 -AzimuthDir "D:\Games\FH2\azimuth-windows"
```

平台 DLL 不是用 MSVC 构建的：平台需要 llvm-mingw。发布工作流会从 `platform\` 子模块交叉编译它，并以 `DWrite.dll`（Azimuth 1.0.1 及更新版本加载的名称）发布。要更新它，请将子模块切换到新的标签。

### 本地部署脚本

`package.ps1` 会构建、填充 `dist\` 并部署 DLL。`-AzimuthDir` 参数默认为作者的文件夹（`D:\Games\FH2\azimuth-windows`），除非你的路径相同，否则请传入你自己的路径。游戏运行时无法覆盖 DLL，请关闭游戏后再运行一次脚本。

---

## 卸载

请先关闭游戏。**不要删除** `mediaoverride` 中的其他任何东西：其中的 Mods 页面界面、字符串表、车辆 zip 和 `DefaultCache.bin` 属于 FH2 Mod Platform 和你的其他模组，`DWrite.dll` 则是平台本身。

**如果只想关闭模组而不卸载，** 打开 **暂停 > 设置 > MODS** 并关闭 **NOS 系统**（或在 ini 中设置 `NitroEnabled=0`）。

### 1. 删除模组（Azimuth 文件夹）

从 `azimuth-windows` 删除以下内容：

- `fh2-mods\FnFNitro.dll`
- `fh2-mods\FnFNitro.ini`（你保存的设置）
- `data\titles\1A96545B\FnFNitro\`（每辆车安装的 NOS 套件）
- `FnFNitro\` 文件夹，如果你为了使用自己的音效而创建了它

### 2. 启动一次游戏

通过 Azimuth 启动游戏。`Mount\mediaoverride` 中模组的 HUD、火焰和数据库文件是由 FH2 Mod Platform 提供的，当没有任何已安装的模组使用它们时，平台会在启动后不久将其删除：NOS 速度表（`UI\Controls\HUDSpeedometerControl.xaml`，以及 `UI\textures\Anthem\HUD\Speedometer\`、`UI\textures\data_bound\Anthem\HUD\` 和 `UI\textures\data_bound\SpireHUD\` 下的贴图）、火焰效果（`Particles\Systems\Backfire.xml`）、NOS 套件的升级图标（`UI\textures\data_bound\Upgrade_Parts\Custom\`），以及包含 NOS 套件和“所有车辆都能回火”的数据库副本（`stripped\gamedbRC.slt`，只有在其他模组仍修改数据库时才会重新生成）。之后速度表、火焰、车辆回火和车库的升级列表都会恢复原样。打开 `fh2-mods\platform.log`：应该不会再有 `[NitroSystem]` 行。

### 3. 仅限手动安装过 1.2 或更旧版本的情况

那些版本需要你自行将文件复制到 `Mount\mediaoverride`。1.3 及更新版本会在启动时删除它们认得的副本，所以只有在你从未运行过较新版本时才需要处理。如果以下内容仍然存在，请删除（加上 `-WhatIf` 可以只查看会删除哪些内容而不实际删除）：

```powershell
$mo = "D:\Games\FH2\Anthem_1.0.0.64_x64__8wekyb3d8bbwe\Mount\mediaoverride"

$targets = @(
  "$mo\UI\textures\Anthem\HUD\HUD_XPBar_TipGlow.swatchbin",
  "$mo\UI\textures\Anthem\HUD\SkillBarTipGlow.swatchbin",
  "$mo\UI\textures\Anthem\HUD\SkillsLargeGlow.swatchbin",
  "$mo\UI\textures\Anthem\HUD\Speedometer",
  "$mo\UI\textures\data_bound\SpireHUD",
  "$mo\UI\textures\data_bound\SpireHUD.zip",
  "$mo\Particles\Materials\backfire.materialbin",
  "$mo\Particles\Materials\backfire_blue.materialbin",
  "$mo\Particles\Materials\backfire_purple.materialbin",
  "$mo\Particles\Materials\Fire\backfire_blue.materialbin",
  "$mo\Particles\Materials\Fire\carBackfire.materialbin",
  "$mo\Particles\Shaders\backfire"
)
foreach ($t in $targets) {
  if (Test-Path $t) { Remove-Item $t -Recurse -Force } else { "Not found (already gone): $t" }
}
```

---

## 已知限制

- **购买套件会记录在你的存档中。** 每辆车安装的阶段记录在模组自己的文件中，但购买是通过游戏自带的升级商店进行的，所以和其他零件一样会记录在存档里（在已购零件列表中，零件类型 47）。因此游戏会记住你买过的阶段：把车换回已拥有的阶段是免费的，支付的价格也会套用游戏通常的折扣。卸载模组后，这些条目仍会留在存档中，指向已随模组消失的升级数据行；游戏之后会如何处理它们尚未测试，所以卸载前请先备份存档。
- **每位玩家一个文件，在启动时选定。** 模组使用最后写入的 `saves\player-N` 文件夹；在游戏过程中切换玩家，要到下次启动才会被识别。
- **第 4 阶段显示第 3 阶段的图标。** 目前还没有它自己的图片（`icons\stage4.png`）。
- **车库名称的语言会晚一次启动才更新，** 与 Mods 页面相同：名称在启动时生成，使用的是上次游戏的语言。
- **`[Upgrade]` 的更改需要重启。** 各阶段及其说明（“NOS 第 3 阶段：容量 20 秒，1 秒回充 0.30 秒。”）都在启动时生成。
- **隐藏速度表时，屏幕特效会更简单。** 此时蓝色暗角和速度线改画在 HUD 层的画布上（需要平台 2.9.1 或更新），而不是速度表上：暗角是分层的边缘框，速度线是直线条，没有速度表上的渐变和动画。旧版平台上则完全不显示。NOS 仪表本身属于速度表，所以隐藏速度表时不显示；NOS 功能（按键、加速、音效、震动和火焰）仍然有效。

---

## 故障排除

模组的所有信息都会写入 `fh2-mods\platform.log`（每次启动都会重新开始）。有用的行：

- `loaded FnFNitro.dll`，接着是每个已安装 hook 的 `[NitroSystem]` 行：模组正在运行。
- `Player car located` 和 `Vertical axis learned: Y`：模组已找到你的车以及哪个方向是上方。游戏加载后需要驾驶几秒钟才会完成。在找到你的车之前，模组无法区分你的车和 AI 车辆，可能会推动所有正在模拟的车辆，所以在其他车辆旁使用 NOS 前请先等几秒。
- `Camera view matrices hooked` 和 `Camera field of view hooked`：镜头抖动和视野加宽已就绪。
- `nitrous upgrade active: Garage > Upgrades > Custom upgrade > Engine > Nitrous Kit`：NOS 套件已加入车库。`NOS Kit of each car: ...` 会给出车库文件的路径；上车时会出现 `NOS Kit stage on the driven car: 3 (20 s tank, recharges 0.30 s/s)`。
- `The NOS Kit upgrade could not be set up` 或 `the nitrous upgrade is not active`：无法加入套件（平台版本低于 2.8.0，或是它不认识的游戏版本），因此所有车辆都有 NOS。
- `Failed to ...` 或 `Could not hook ...`：某个 hook 安装失败，通常是因为游戏版本不是本模组所针对的版本。

如果没有 NOS 计量条或没有火焰，请确认平台为 2.7.3 或更新版本（或已安装 **Extra Options** 并开启 `EnableMediaOverrides`），并确认 `platform.log` 中有 HUD 文件和 `Backfire.xml` 的 `[NitroSystem] replaces media\...` 行。如果日志说模组无法替换某个文件，说明另一个模组已经在替换它。如果计量条存在但是空的且没有外框，说明你驾驶的车没有 NOS 套件（或列在 `DisabledCars` 中）。

---

## 给模组作者：关闭 NOS

完整说明以及可直接复制的查询线程代码，请见 [docs/MOD_CONTROL.md](docs/MOD_CONTROL.md)（英文）。其他 FH2 Mod Platform 模组可以在需要时关闭玩家的 NOS，并读取 NOS 是否正在喷射以及储气罐的余量。将 [`include/NitroSystemControl.h`](include/NitroSystemControl.h) 复制到你的模组中，并在所有模组启动后查询一次这个开关：

```c
#include "NitroSystemControl.h"

// 在你自己的线程中调用，而不是在 fh2mod_init 中
api->wait_for_mods(10000);
const NitroSystemControl* nos =
    (const NitroSystemControl*)api->get_interface(NITROSYSTEM_CONTROL_NAME, NITROSYSTEM_CONTROL_VERSION);

if (nos) nos->set_blocked("MyMod", 1);   // 关闭玩家的 NOS
if (nos) nos->set_blocked("MyMod", 0);   // 重新开启
```

- `set_blocked(who, on)`：每个模组以自己的名称屏蔽，只要有任何模组屏蔽，NOS 就保持关闭，所以两个模组不会互相撤销。屏蔽期间，NOS 按钮不起作用，正在喷射的 NOS 会立刻停止，NOS 计量条会隐藏；储气罐仍会回充，Drivatar 不受影响。屏蔽会持续到游戏关闭为止。
- `is_blocked()`、`is_active()`（NOS 正在喷射）以及 `nitro_percent()`（储气罐余量，0 到 100）。
- `get_interface` 返回 `NULL` 表示未安装 Nitro System：请在没有它的情况下继续运行。
- 不使用平台接口时，`FnFNitro.dll` 也导出了相同的功能：`FnFNitro_SetBlocked`、`FnFNitro_IsBlocked`、`FnFNitro_IsActive` 和 `FnFNitro_GetNitroPercent`。

`platform.log` 会显示 `NOS blocked by MyMod.` 和 `NOS no longer blocked by MyMod.`，调试信息也会列出正在屏蔽 NOS 的模组。**ANNA Drone Mode** 不需要做这些：Nitro System 会询问它无人机是否正在飞行（日志中的 `ANNA Drone Mode found`），并以它的名称屏蔽 NOS。

---

## 致谢

- **Levilente**，感谢 [NitroSystem II](https://github.com/Levilente/NitroSystem-II)，本模组依据 MIT 许可证使用了其 NOS 套件车库升级（`src/nu_upgrade.h`、`src/nu_sql.h`）、升级图标（`icons/`、`scripts/gen_icons.py`、`scripts/icontools/`）、视野加宽、蓝色暗角和速度线（`hud/HUDSpeedometerControl.xaml`、`scripts/gen_speedlines.py`）。
- **NitroSystem II**，本模组的 Forza Horizon 3 移植版，它发现可以在车辆第一次回火之前就向车辆查询排气口位置。FH2 也是用同样的方式处理，所以火焰能立即出现。
- **[suderek22](https://github.com/suderek22)**，感谢 [FH2_HonkHonk](https://github.com/suderek22/FH2_HonkHonk)。它演示了如何通过游戏自带的 FMOD 音频引擎在游戏世界中的某个位置播放声音，Drivatar 的 NOS 音效就是这样从它们的车上播放的。本模组没有使用 HonkHonk 的代码：本模组用自己的代码调用相同的 FMOD 函数。
- **Deuquan**，感谢 FH2-CameraMods。它指出了哪些镜头函数负责构建驾驶舱、引擎盖、保险杠和追尾视角，NOS 镜头抖动和视野加宽就是在那里应用的。
