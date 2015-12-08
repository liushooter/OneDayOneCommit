React

https://ruby-china.org/topics/26944  还在纠结 Flux 或 Relay，或许 Redux 更适合你



http://camsong.github.io/redux-in-chinese/


https://egghead.io/series/getting-started-with-redux



因为 Flux 本身约定不够细致，如何做异步、如何做同构这些非常普遍的问题，官方都没有给出详细的说明。还有 store，view 里一大堆重复代码，极速膨胀的 action 等问题。这也难免会冒出一堆“改良”性的轮子。
有一些非常闪光，如 Redux，Reflux，Marty。
Reflux 和 Marty 基本上只是去掉重复代码并为现有 Store，Action 增加一些灵活性，用起来比原生 Flux 上手更容易，但是总体二者没有跳出 Flux 的思想，大量依旧采用“传统”的 mixin 方式实现。如果项目不是很复杂可以试试。

至于 Relay，由于需要后端 GraphQL 支持，对于采用 REST 接口开发的遗留项目和前后端分离的大团队来说成本切换有点高。



Dedux  

reflux

#47楼 @steven_yue Reflux 特别灵活，它的 action 设计的太灵活强大了，view 里直接监听 action 这一点瞬间把 Flux 门槛拉的极低，虽然这是标准 Flux 不建议做的。如果不考虑做同构、Time Travel、Do/Undo 这些 Reflux 是不错的选择。



http://blog.keithcirkel.co.uk/how-to-use-npm-as-a-build-tool/
