# ota_smoke_auto
ota update smoke auto test（E115 project）


一.项目框架结构介绍:
1.Config:
  测试框架配置文件:测试用例存放路径，方法加载方式，日志存放路径配置
  待测设备配置文件：url路径，版本号，机器型号
2.Execute:
  测试框架入口
  测试辅助shell脚本
3.Logs:
  记录测试用例和框架运行日志
  记录测试报告（html，json）
  记录待测程序运行日志收集
4.Mylog:
  日志模块封装（warning，error，debug，info）
5.Common:
  通用方法封装
  命令模块（shell脚本执行，cmd命令，gnome命令）
  文件模块（文件搜索，文件解压，文件删除，新增文件，文件夹，动态获取最新文件，读写文件，筛选日志）
  操作事件（启动ubuntu终端，关闭终端，最大化，最小化窗口，鼠标键盘模拟事件，截图）
  通用方法（下载文件，判断测试平台，解析url，检测运行环境）
6.testcases:
  测试用例配置（项目名称，测试类型，测试用例，例如E115/OAT_SMOKE_AUTO_TEST/TEST_LUANCH_OTA）
  测试用例封装（调用api，ui，function已实现方法）
  xml文件（部署测试环境前提，主测试方法，测试环境还原）
  调用pytest测试框架（顺序执行测试用例）
7.testframework:
  测试用例实现（对应具体项目场景，目前E115）
  xml解析，写入用例供框架调用（配置文件）
8.utils:
  保留部分

二.执行方式
  pytest ../Execute/execute.py 项目名称/测试类型/测试用例 ../报告路径（可按照环境切换用例)
  测试：0
  正式：1
  
三.前提：
  1.准备dmtree
  2.准备dmserver
  3.联网

