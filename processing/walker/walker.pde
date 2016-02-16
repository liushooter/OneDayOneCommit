float[] randomCounts;

class Walker {
  int x;
  int y;

  Walker(){
    x = width/2;
    y = height/2;
  }

  void display(){
    point(x,y);
  }

  void step(){
    float stepx = random(-1, 1);
    float stepy = random(-1, 1);

    x += stepx;
    y += stepy;
   }

}//

Walker w;

void setup(){
  size(640, 360);
  randomCounts = new float[20];
  w = new Walker();
}


void draw(){
  background(255);
  int index = int(random(randomCounts.length)); // 选择一个随机数, 增加计数
  randomCounts[index]++;
  stroke(0);
  fill(127);
  int w = width / randomCounts.length;

  for(int x=0; x<randomCounts.length; x++){
    rect(x*w, height-randomCounts[x], w-1 , randomCounts[x] ); //绘制矩形
  }

}