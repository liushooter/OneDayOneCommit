class PVector {

  PVector(float x_, float y_) {
    x = x_;
    y = y_;
  }

  void add(PVector v) {
    x = x + v.x;
    y = y + v.y;
  }
} //


void setup() {
  size(200, 200);
  smooth();

}


