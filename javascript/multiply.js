function multiply(x){
  console.log(/multiply/ + x);

    return function(y){
      console.log(/return/ + x);
      console.log(/return/ + y);
        return x*y;
    }
}

multiply(2)
multiply(2)()
multiply(2)(3)
