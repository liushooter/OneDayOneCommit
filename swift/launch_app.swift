import AppKit // 必须导入，以便使用 NSWorkspace

let path = "/System/Applications/Calculator.app"
let appURL = URL(fileURLWithPath: path)
let conf = NSWorkspace.OpenConfiguration()
conf.createsNewApplicationInstance = true
conf.addsToRecentItems = false

// NSWorkspace.shared.open 是异步操作，
// 为了防止脚本立即退出，我们需要添加一个运行循环。
// 这比在 Xcode 项目中复杂一些。

// 创建一个信号量 (Semaphore) 来等待异步操作完成
let semaphore = DispatchSemaphore(value: 0)

NSWorkspace.shared.open(appURL, configuration: conf, completionHandler: { launchedApp, error in
    if let error {
        print("Could not launch new app: \(error.localizedDescription)")
    } else if let launchedApp {
        print("Launched app process id: \(launchedApp.processIdentifier)")
    }

    // 释放信号量，让脚本继续执行
    semaphore.signal()
})

// 等待信号量，直到 completionHandler 完成
semaphore.wait()

// 脚本执行完毕，计算器应用已启动