main() {
  var _keys = contextKeys();

  print("length: " + _keys.length.toString());
  print(_keys);

  prime();
}

List<String> contextKeys() {
  // 5个上下文关键字
  var list = ['on', 'sync', 'async', 'hide', 'show'];

  return list;
}

prime() {
  //函数名不能是 List

  List list = [2, 3, 5, 7];
  list.add(11);
  list.add(13);
  list.add("0x11");
  list.add(["0x13", true]);

  print(list);

  int inx = list.indexOf(5); // 查找5的索引
  print(inx);

  bool result = list.contains(5); // 是否包含5
  print(result);

  list.remove(2); // 移除2
  print(list);
}
