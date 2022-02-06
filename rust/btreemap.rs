use std::collections::BTreeMap;

fn main() {
    let mut map: BTreeMap<i64, BTreeMap<String, String>> = BTreeMap::new();
    let mut nest: BTreeMap<String, String> = BTreeMap::new();

    nest.insert("name".into(), "aho".into());

    let ele = map.get(&1).unwrap_or(&nest);

    if let Some(name) = ele.get("name") {
        println!("welcome, {}.", name);
    } else {
        println!("nest is null")
    }

    if let Some(_ele) = map.get(&1) {
        if let Some(name) = _ele.get("name") {
            println!("welcome, {}", name);
        } else {
            println!("map nest is null")
        }
    } else {
        println!("map is null")
    }

    let newmap = newmap();

    let info = newmap.get(&1).and_then(|m| m.get("gender".into()));
    println!("gender: {}", *info.unwrap());
}

fn newmap() -> BTreeMap<i64, BTreeMap<String, String>> {
    let mut map: BTreeMap<i64, BTreeMap<String, String>> = BTreeMap::new();

    map.entry(1)
        .or_default()
        .insert("gender".into(), "lgbtq".into());
    return map;
}
