#### Cargo

##### 新建项目

```
cargo new hyper  --bin

hyper
  ├── Cargo.toml
  └── src
       └── main.rs
```
###### 编译

```
cargo build

├── Cargo.lock
├── Cargo.toml
├── src
│   └── main.rs
└── target
    └── debug
        ├── build
        ├── deps
        ├── examples
        ├── hyper
        ├── hyper.d
        ├── incremental
        └── native
```

###### 执行

`cargo run`

##### 安装依赖

```
cargo install rocket

    Updating registry `https://github.com/rust-lang/crates.io-index`
 		Downloading rocket v0.3.16
```