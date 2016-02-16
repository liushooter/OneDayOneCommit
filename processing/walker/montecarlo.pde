float montecarlo(){ //蒙特卡洛算法 蒙特卡洛大赌场命名
  while(true){
    float r1 = random(1);
    float probability = r1; // 分配概率

    float r2 = random(1);

    if(r2 < probability) {
      return r1;
    }
  }
}